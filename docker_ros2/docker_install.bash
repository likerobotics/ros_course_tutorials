#!/usr/bin/env bash
set -euo pipefail

INSTALL_NVIDIA=0

usage() {
  echo "Usage: $0 [--nvidia]"
}

while (($#)); do
  case "$1" in
    -n|--nvidia) INSTALL_NVIDIA=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ ! -r /etc/os-release ]]; then
  echo "Cannot identify the operating system." >&2
  exit 1
fi

# shellcheck disable=SC1091
. /etc/os-release
if [[ "${ID}" != "ubuntu" ]]; then
  echo "This installer supports Ubuntu only (detected: ${ID})." >&2
  exit 1
fi

sudo apt-get update
sudo apt-get install -y ca-certificates curl xauth

# Remove packages that conflict with Docker CE, when present.
for package in \
  docker.io docker-compose docker-compose-v2 docker-doc podman-docker \
  containerd runc; do
  if dpkg-query -W -f='${Status}' "${package}" 2>/dev/null \
      | grep -q 'ok installed'; then
    sudo apt-get remove -y "${package}"
  fi
done

sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

ARCH="$(dpkg --print-architecture)"
CODENAME="${UBUNTU_CODENAME:-${VERSION_CODENAME}}"
echo "deb [arch=${ARCH} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu ${CODENAME} stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

sudo apt-get update
sudo apt-get install -y \
  containerd.io \
  docker-buildx-plugin \
  docker-ce \
  docker-ce-cli \
  docker-compose-plugin

sudo systemctl enable --now docker
sudo groupadd --force docker
sudo usermod -aG docker "${USER}"

if [[ ${INSTALL_NVIDIA} -eq 1 ]]; then
  if ! command -v nvidia-smi >/dev/null; then
    echo "NVIDIA driver not found. Install the host driver before the toolkit." >&2
    exit 1
  fi

  curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | sudo gpg --dearmor --yes \
        -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
  curl -fsSL \
    https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
        >/dev/null

  sudo apt-get update
  sudo apt-get install -y nvidia-container-toolkit
  sudo nvidia-ctk runtime configure --runtime=docker
  sudo systemctl restart docker
fi

echo "[*] Docker installation completed."
echo "[*] Log out and back in before running Docker without sudo."


#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTAINER_NAME="ros2_course_jazzy"
IMAGE_NAME="itmo/ros2-course:jazzy"
XAUTH_FILE="/tmp/ros2-course-${UID}.xauth"

USE_NVIDIA=0
USE_HARDWARE=0

usage() {
  echo "Usage: $0 [--nvidia] [--hardware]"
}

while (($#)); do
  case "$1" in
    -n|--nvidia) USE_NVIDIA=1; shift ;;
    --hardware) USE_HARDWARE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

command -v docker >/dev/null || { echo "Docker is not installed." >&2; exit 1; }
command -v xauth >/dev/null || {
  echo "xauth is required for GUI applications: sudo apt install xauth" >&2
  exit 1
}
[[ -n "${DISPLAY:-}" ]] || {
  echo "DISPLAY is not set; an X11/XWayland session is required for GUI tools." >&2
  exit 1
}

touch "${XAUTH_FILE}"
chmod 600 "${XAUTH_FILE}"
XAUTH_DATA="$(xauth nlist "${DISPLAY}" 2>/dev/null | sed -e 's/^..../ffff/')"
if [[ -n "${XAUTH_DATA}" ]]; then
  printf '%s\n' "${XAUTH_DATA}" | xauth -f "${XAUTH_FILE}" nmerge -
else
  echo "Unable to create X11 authorization data for DISPLAY=${DISPLAY}." >&2
  exit 1
fi

if docker container inspect "${CONTAINER_NAME}" >/dev/null 2>&1; then
  echo "[*] Starting existing container ${CONTAINER_NAME}"
  docker start --attach --interactive "${CONTAINER_NAME}"
  exit 0
fi

DOCKER_ARGS=(
  --interactive
  --tty
  --name "${CONTAINER_NAME}"
  --env "DISPLAY=${DISPLAY}"
  --env "QT_X11_NO_MITSHM=1"
  --env "XAUTHORITY=/tmp/.docker.xauth"
  --mount "type=bind,src=${XAUTH_FILE},dst=/tmp/.docker.xauth,readonly"
  --mount "type=bind,src=${ROOT_DIR},dst=/workspace"
  --network host
)

if [[ -e /dev/dri ]]; then
  DOCKER_ARGS+=(--device /dev/dri)
fi

if [[ ${USE_NVIDIA} -eq 1 ]]; then
  DOCKER_ARGS+=(
    --gpus all
    --env "NVIDIA_DRIVER_CAPABILITIES=all"
  )
fi

if [[ ${USE_HARDWARE} -eq 1 ]]; then
  echo "[!] Hardware mode grants the container access to all host devices."
  DOCKER_ARGS+=(--privileged --volume /dev:/dev)
fi

echo "[*] Creating container ${CONTAINER_NAME}"
docker run "${DOCKER_ARGS[@]}" "${IMAGE_NAME}"


#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE_NAME="itmo/ros2-course:jazzy"
FROM_IMAGE="ubuntu:24.04"

usage() {
  echo "Usage: $0 [--from-image IMAGE]"
}

while (($#)); do
  case "$1" in
    --from-image)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      FROM_IMAGE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

echo "[*] Building ${IMAGE_NAME} from ${FROM_IMAGE}"
docker build \
  --build-arg "FROM_IMAGE=${FROM_IMAGE}" \
  --build-arg "USER_NAME=ros" \
  --build-arg "USER_UID=$(id -u)" \
  --build-arg "USER_GID=$(id -g)" \
  --file "${ROOT_DIR}/docker_ros2/Dockerfile" \
  --tag "${IMAGE_NAME}" \
  "${ROOT_DIR}"


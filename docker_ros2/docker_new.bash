#!/usr/bin/env bash
set -euo pipefail

CONTAINER_NAME="ros2_course_jazzy"

if [[ "$(docker inspect --format '{{.State.Running}}' "${CONTAINER_NAME}" 2>/dev/null || true)" != "true" ]]; then
  echo "Container ${CONTAINER_NAME} is not running." >&2
  echo "Start it with: bash docker_ros2/docker_run.bash" >&2
  exit 1
fi

docker exec --interactive --tty "${CONTAINER_NAME}" bash


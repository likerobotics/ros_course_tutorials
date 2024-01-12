#!/usr/bin/env bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
EXEC_PATH=$PWD

cd $ROOT_DIR

if [[ $1 = "--nvidia" ]] || [[ $1 = "-n" ]]
  then
    docker build -t ros_course2023-img -f $ROOT_DIR/docker/Dockerfile $ROOT_DIR \
                                  --network=host \
                                  --build-arg from_image=nvidia/opengl:1.2-glvnd-devel-ubuntu20.04

else
    echo "[!] If you use nvidia gpu, please rebuild with -n or --nvidia argument"
    docker build -t ros_course2023-img -f $ROOT_DIR/docker/Dockerfile $ROOT_DIR \
                                  --network=host \
                                  --build-arg from_image=ubuntu:20.04
fi

cd $EXEC_PATH

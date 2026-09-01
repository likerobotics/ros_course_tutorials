# ROS 2 Jazzy course container

This directory provides an Ubuntu 24.04 development environment for the ROS 2
course. The image includes ROS 2 Jazzy, Gazebo integration, `ros2_control`,
RViz2, Xacro, camera/lidar support, `colcon`, and `rosdep`.

The scripts support Ubuntu hosts with X11 or XWayland. Native macOS and Windows
GUI use is not supported by these scripts; use WSL 2 on Windows or a dedicated
VNC-based ROS container on macOS.

## 1. Install Docker on the host

Run this once on Ubuntu:

```bash
bash docker_ros2/docker_install.bash
```

For a host with an NVIDIA GPU, install a compatible NVIDIA driver first and
then run:

```bash
bash docker_ros2/docker_install.bash --nvidia
```

Log out and back in after installation so membership in the `docker` group
takes effect. The installer also installs `xauth`, which is used to authorize
GUI applications without globally opening the X server.

## 2. Build the course image

From the repository root:

```bash
bash docker_ros2/docker_build.bash
```

The resulting image is named `itmo/ros2-course:jazzy`. A different compatible
Ubuntu 24.04 base can be selected explicitly:

```bash
bash docker_ros2/docker_build.bash --from-image ubuntu:24.04
```

NVIDIA support does not require a separate image build. GPU libraries are
provided at runtime by NVIDIA Container Toolkit.

## 3. Start the container

For CPU or integrated graphics:

```bash
bash docker_ros2/docker_run.bash
```

For NVIDIA graphics:

```bash
bash docker_ros2/docker_run.bash --nvidia
```

The complete repository is mounted at `/workspace`, so `lab1` through `lab5`
are directly available. The container user has the same UID and GID as the host
user, preventing root-owned files in the repository.

The container is persistent. Exiting Bash stops it but does not delete it;
running `docker_run.bash` again restarts the same container. To recreate it
after rebuilding the image, remove the stopped container first:

```bash
docker rm ros2_course_jazzy
bash docker_ros2/docker_run.bash
```

## Additional terminals

While the container is running, open another host terminal and run:

```bash
bash docker_ros2/docker_new.bash
```

## Building laboratory packages

Inside the container:

```bash
cd /workspace
rosdep update
rosdep install --from-paths . --ignore-src --rosdistro jazzy -y
colcon build --symlink-install
source install/setup.bash
```

To build only one package, add `--packages-select PACKAGE_NAME` to the `colcon`
command.

Generated `build/`, `install/`, and `log/` directories are ignored by Git.

## Physical devices

Normal simulation does not require a privileged container. Hardware access is
available explicitly:

```bash
bash docker_ros2/docker_run.bash --hardware
```

This grants broad access to host devices and should be used only for laboratory
work that communicates with physical hardware. Flags can be combined, for
example `--nvidia --hardware`.

## Useful checks

Inside the container:

```bash
ros2 --help
gz sim --versions
ros2 pkg prefix ros_gz_sim
ros2 pkg prefix gz_ros2_control
```

On an NVIDIA host:

```bash
docker run --rm --gpus all ubuntu:24.04 nvidia-smi
```

## Troubleshooting

- `permission denied` for Docker: log out and back in after installation.
- `xauth is required`: run `sudo apt install xauth` on the host.
- `DISPLAY is not set`: start the script from a graphical X11/XWayland session.
- `could not select device driver ... gpu`: repeat the NVIDIA installation and
  confirm `nvidia-ctk runtime configure --runtime=docker` succeeded.
- Changes to the Dockerfile do not affect an existing container. Rebuild the
  image, remove `ros2_course_jazzy`, and start it again.


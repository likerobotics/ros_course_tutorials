ARG FROM_IMAGE=ubuntu:24.04
FROM ${FROM_IMAGE}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG ROS_DISTRO=jazzy
ARG USER_NAME=ros
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV ROS_DISTRO=${ROS_DISTRO}
ENV ROS_DOMAIN_ID=0
ENV RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# Base development tools, locale support, and the Ubuntu repository required by
# ROS desktop packages.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        gnupg2 \
        locales \
        software-properties-common \
        sudo \
    && locale-gen en_US.UTF-8 \
    && add-apt-repository universe \
    && rm -rf /var/lib/apt/lists/*

# Configure the ROS 2 apt repository for Ubuntu Noble.
RUN mkdir -p /usr/share/keyrings \
    && curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
        | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo "$UBUNTU_CODENAME") main" \
        > /etc/apt/sources.list.d/ros2.list

# Install ROS development tools and everything used by the laboratory work.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-colcon-common-extensions \
        python3-numpy \
        python3-opencv \
        python3-rosdep \
        python3-vcstool \
        ros-${ROS_DISTRO}-cv-bridge \
        ros-${ROS_DISTRO}-desktop \
        ros-${ROS_DISTRO}-gz-ros2-control \
        ros-${ROS_DISTRO}-joint-state-publisher-gui \
        ros-${ROS_DISTRO}-ros-gz \
        ros-${ROS_DISTRO}-ros2-control \
        ros-${ROS_DISTRO}-ros2-controllers \
        ros-${ROS_DISTRO}-rmw-fastrtps-cpp \
        ros-${ROS_DISTRO}-xacro \
    && rosdep init \
    && rm -rf /var/lib/apt/lists/*

# Match the host user's IDs so bind-mounted files are not owned by root.
RUN groupadd --gid "${USER_GID}" "${USER_NAME}" \
    && useradd --uid "${USER_UID}" --gid "${USER_GID}" \
        --create-home --shell /bin/bash "${USER_NAME}" \
    && usermod -aG dialout,video "${USER_NAME}" \
    && echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" \
        > "/etc/sudoers.d/${USER_NAME}" \
    && chmod 0440 "/etc/sudoers.d/${USER_NAME}" \
    && echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /etc/bash.bashrc

WORKDIR /workspace
USER ${USER_NAME}

CMD ["bash"]


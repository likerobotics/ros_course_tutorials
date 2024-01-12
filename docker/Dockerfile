ARG from_image
FROM ${from_image}

# Timezone Configuration

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y apt-utils \
                                         lsb-release \
                                         mesa-utils \
                                         net-tools \
                                         build-essential \
                                         wget \
                                         unzip \
                                         curl \
                                         git \
                                         mc \
                                         vim



# Install ROS desktop and Gazebo

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    curl -s 'https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc' | apt-key add - && \
    apt-get update && DEBIAN_FRONTEND=noninteractive \
                      apt-get install -y ros-noetic-desktop-full \
                                         ros-noetic-gazebo-ros-pkgs \
                                         ros-noetic-ros-control \
                                         ros-noetic-gazebo-ros-control \
                                         ros-noetic-teleop-twist-keyboard
    #                                      python3-rosdep\
    #                                      python3-rosinstall \
    #                                      python3-rosinstall-generator \
    #                                      python3-wstool \
    #                                      build-essential \
    # rosdep init && rosdep update && \
    # echo "source /opt/ros/noetic/setup.bash"  >> ~/.bashrc && \
    # echo "source /workspace/devel/setup.bash"  >> ~/.bashrc

# Install extra libraries
RUN apt-get install -y python3-pip
RUN pip install pathlib statistics scipy

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
                      apt-get install -y ros-noetic-ecl-geometry \
                                            ros-noetic-tf2-sensor-msgs \
                                            ros-noetic-move-base-msgs \
                                            ros-noetic-image-proc

RUN apt-get update && apt-get install -y \
                libopencv-dev libx11-dev liblapack-dev libv4l-dev libzbar-dev libpthread-stubs0-dev libsdl-dev libsdl-image1.2-dev \
                libeigen3-dev

# RUN pip install numpy scikit-image 
# RUN pip install pillow 
# RUN pip install opencv-contrib-python
RUN echo "source /opt/ros/noetic/setup.bash"  >> ~/.bashrc
RUN echo "source /workspace/devel/setup.bash"  >> ~/.bashrc
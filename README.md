# ROS 2 Course

Course materials and structured laboratory-work submissions for learning robot
software development with ROS 2.

The course uses **ROS 2 Jazzy** on **Ubuntu 24.04** and **Gazebo Harmonic**.
It introduces ROS 2 communication and tooling before progressing from robot
descriptions to simulation, control, sensors, and hardware integration.

## Course content

The course covers:

- Linux, ROS 2 installation, workspaces, packages, and `colcon`;
- ROS 2 nodes, topics, messages, parameters, namespaces, and launch files;
- quality of service (QoS), ROS time, and command-line tools;
- custom messages, services, and actions;
- TF2, URDF, Xacro, and visualization in RViz2;
- robot simulation with Gazebo and communication through `ros_gz_bridge`;
- joint and mobile-base control with `ros2_control`;
- simulated cameras and lidars and processing their data;
- hardware interfaces and communication with a microcontroller.

## Laboratory works

1. **ROS 2 package and controller** — run two turtlesim instances in separate
   namespaces, control the first turtle through assigned points, and make the
   second turtle follow its pose.
2. **Custom services and actions** — define custom interfaces and separate
   turtle-control behavior into clients and servers. The action part is an
   optional advanced task.
3. **Robot model** — describe a variant-specific mobile robot and manipulator
   using Xacro, publish its state, and visualize its model and TF tree in RViz2.
4. **Robot simulation and control** — simulate a differential-drive robot in
   Gazebo, control its joints with `ros2_control`, and convert `/cmd_vel`
   commands into wheel velocities.
5. **Sensors and autonomous behavior** — add a camera and lidar to a simulated
   robot, create a populated scene, visualize sensor data, and implement a
   clearly observable behavior using sensor feedback.
6. **Hardware integration with `ros2_control`** — create a custom hardware
   interface derived from `hardware_interface::SystemInterface`, register it as
   a plugin, and connect it to the robot through URDF and controller
   configuration. Implement the `read`/`update`/`write` control loop and exchange
   wheel commands and encoder feedback with an Arduino-compatible
   microcontroller using the specified `SET` and `ENC` protocol. The completed
   system must expose its hardware interfaces and controllers through the ROS 2
   control tools and run with simulation time disabled.

Exact variant values and assessment requirements are defined in the course
book. A student's variant is selected using the last digit of their ITMO ISU
ID.

## Repository layout

```text
ros2_course/
├── lab1/    # mybestcontroller
├── lab2/    # lab2_interfaces and lab2_controller
├── lab3/    # my_best_model
├── lab4/    # my_best_robot_simulation_control
├── lab5/    # my_best_robot_simulation_setup
├── lab6/    # my_robot_hardware and hardware-control configuration
└── docker_ros2/
```

The `lab1` through `lab6` directories are submission locations. Package names,
required filenames, and directory paths must remain unchanged because automated
checks rely on them. Skeleton files provide structure only; students must
replace all `TODO(student)` markers with their own implementations.

Do not commit generated workspace artifacts such as `build/`, `install/`, or
`log/`.

## Building a submission

Place the repository inside a ROS 2 workspace or build a selected package from
the repository root. For example:

```bash
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install --packages-select mybestcontroller
source install/setup.bash
```

Run Lab 1 with:

```bash
ros2 launch mybestcontroller lab1.launch.py
```

Other laboratory packages use the launch filenames specified in their
assignments and package documentation.

## Submission rules

- Submit source packages only in the corresponding `labN` directory.
- Preserve all required package and file names.
- Do not include unrelated packages or generated build artifacts.
- Replace template metadata and every student TODO where instructed.
- Ensure the package builds from a clean workspace before submission.
- Keep solutions original; this repository provides submission structure, not
  completed laboratory solutions.

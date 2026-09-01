# Laboratory Work 6: Hardware Integration with ros2_control

## Objective

Integrate a physical mobile robot into ROS 2 by implementing a custom
`ros2_control` hardware interface, configuring controllers, and exchanging
commands and encoder feedback with a microcontroller.

## Submission structure

The hardware plugin package is named `my_robot_hardware` and uses
`ament_cmake`. A submission must contain, at minimum:

```text
lab6/
└── my_robot_hardware/
    ├── config/
    ├── include/my_robot_hardware/
    ├── launch/
    ├── src/
    ├── urdf/
    ├── CMakeLists.txt
    ├── package.xml
    └── plugin_description.xml
```

Additional support packages may be included only when required by the submitted
hardware architecture.

## Hardware interface requirements

- Implement a class derived from `hardware_interface::SystemInterface`.
- Export velocity command interfaces and velocity state interfaces for the left
  and right wheel joints.
- Implement lifecycle initialization and the required interface-export,
  `read()`, and `write()` methods for the installed Jazzy API.
- Register the class with `pluginlib` and export it through
  `plugin_description.xml`.
- Declare and link the `hardware_interface`, `rclcpp`, and `pluginlib`
  dependencies.

## Robot and controller configuration

- Add a `ros2_control` system block to the robot description and reference the
  submitted hardware plugin.
- Configure `controller_manager` with an update rate of 30 Hz unless a justified
  alternative is required.
- Configure a joint-state broadcaster and a differential-drive base controller.
- Launch the physical system with `use_sim_time` set to `false`.

## Microcontroller protocol and control loop

- Send wheel commands using `SET v_left v_right`.
- Receive encoder measurements using `ENC ticks_left ticks_right`.
- Convert encoder measurements into wheel state in `read()`.
- Transmit current wheel commands in `write()`.
- Ensure the complete loop performs read, controller update, and write phases.

## Verification

The running system must expose its interfaces and active controllers through:

```bash
ros2 control list_hardware_interfaces
ros2 control list_controllers
```

The robot must accept motion commands, produce controller outputs, exchange data
with the microcontroller, and report encoder feedback. The independent task is
to support another kinematic configuration and add appropriate QoS settings.
The backbone must not contain the hardware driver, serial protocol
implementation, or custom controller solution.


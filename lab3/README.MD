# Laboratory Work 3: Robot Model

## Objective

Create a mobile robot with a mounted manipulator in Xacro, publish its state,
and visualize its geometry and TF tree in RViz2.

## Submission structure

Submit exactly one ROS 2 package:

```text
lab3/
└── my_best_model/
    ├── config/
    ├── launch/rviz.launch.py
    ├── urdf/robot_model.xacro
    ├── CMakeLists.txt
    └── package.xml
```

Remove unrelated files and packages from `lab3` before submission.

## Model requirements

- Select the variant using the last digit of the student's ITMO ISU ID.
- Implement the assigned total link count, manipulator joint sequence, wheel
  joint count/type, and mobile-base dimensions from Table 12.1 in the book.
- Interpret `R` as revolute, `P` as prismatic, and `C` as continuous.
- Build the model in `urdf/robot_model.xacro`; reusable Xacro macros and include
  files may be added under `urdf/`.
- Maintain a valid connected kinematic tree with consistent parent/child links,
  joint axes, limits where applicable, and non-conflicting names.

## Launch and visualization requirements

`rviz.launch.py` must:

- process and load the Xacro model as `robot_description`;
- start `robot_state_publisher`;
- start `joint_state_publisher_gui`;
- start RViz2 with a package-provided configuration;
- configure RViz2 to display the robot model and TF frames.

## Required launch command

```bash
ros2 launch my_best_model rviz.launch.py
```

The submitted package must install its `launch`, `urdf`, and `config` resources.
The repository backbone must not predefine variant geometry or a completed robot
model.


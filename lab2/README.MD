# Laboratory Work 2: Custom Services and Actions

## Objective

Define custom ROS 2 service and action interfaces and separate turtle-control
behavior into client and server nodes.

## Submission structure

Submit exactly two packages:

```text
lab2/
├── lab2_interfaces/    # ament_cmake interface package
└── lab2_controller/    # ament_python node package
```

Remove unrelated files and packages from `lab2` before submission.

## Part 1: Service

- Create `AISUID.srv` in `lab2_interfaces`, replacing `ISUID` with the student's
  six-digit ITMO ISU ID.
- The request must contain the current `Xcurrent` and `Ycurrent` coordinates.
- The response must provide target distance `Distance` and angular error
  `Angle`. An additional completion flag may be used.
- The server owns the target-point list and computes the errors. The client
  must not know the target coordinates.
- The client obtains the current turtle pose, requests errors while the turtle
  is stationary, and performs closed-loop motion.
- The server advances to the next assigned target when the current target is
  reached. Use the tolerances defined in the course book.
- Provide `service_server.launch.py` and `service_client.launch.py`. The server
  launch file must also start turtlesim.
- Verify the server using both `ros2 service call` and the custom client.

## Part 2: Action (optional advanced task)

- Create `AISUID.action` in `lab2_interfaces`.
- The goal contains a target position, feedback reports distance error, and the
  result reports successful completion.
- The action server controls the turtle; the client sends a goal, displays
  feedback, and reports completion.
- Provide `action_server.launch.py` and `action_client.launch.py`.
- Verify the server using `ros2 action send_goal` and the custom client.

All interface names, package names, and launch filenames form part of the
automated-checking contract. This repository does not provide node logic or
interface definitions as a completed solution.


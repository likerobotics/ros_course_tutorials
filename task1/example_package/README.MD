# HOW TO RUN

Minimal publisher and subscriber package.


some useful commands:
```
cd ~/ros2_jazzy # go to your workspace

colcon build --symlink-install --packages-select example_package # buld

source install/setup.bash # source

ros2 run example_package publisher1 # run your publisher
ros2 run example_package listener1 # run your listener


```

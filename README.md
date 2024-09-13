# ros_course_tutorials
ROS course tutorials: full course from the beginning to the practical use.

> [!WARNING]
> For ITMO University students there is different repository with extended and more relevant materials, but Docker section is same for everybody.

## Docker
### Installation
install docker following the instructions on https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository 

Don't forger to add user to the group docker (https://docs.docker.com/engine/install/linux-postinstall/)

### Start using docker
If you are not interested on Docker, just use the following bash scripts to get ROS inside `docker` folder (`cd docker`) step by step: 

Step 1:
```
xhost +local:root 
```
Step 2:
```
./docker_install.bash
```
Step 3:
```
./docker_build.bash
```
Step 4:
```
./docker_run.bash
```

If you you want to use docker as with all commands, just open the bash scripts in IDE and execude comands in terminal! =)

## First run
from teriman to enter docker container just use `./docker_run.bash`
if u need new bash-script(new terminal) with same docker just open new terminal and use command `./docker_new.bash`



> [!NOTE]
> Some check (for first time):
>	- OS version: `lsb_release -a`
>	- ROS version: `rosversion -d`
	

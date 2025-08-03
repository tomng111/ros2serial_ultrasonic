# ROS2 Serial - HC-SR04 Ultrasonic Sensor
This is a fork of the original code from <ins>docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html</ins>, with some changes.<br />
An Arduino MEGA board is used as the hardware where the data from HC-SR04 is collecting.<br /><br />
ROS2 Humble - Arduino MEGA 2560 - HC-SR04<br />
## Essential Commands<br /> 
- `colcon build --symlink-install`<br />
- `cd <your_workspace>/src`<br />
- `ros2 pkg create --build-type ament_python --license Apache-2.0 <your_package>`<br />
## Arduino Commands<br /> 
- `sudo chmod a+rw /dev/ttyACM0`<br />
## Operating Commands<br /> 
- `source install/setup.bash`<br />
- `ros2 run <your_package> serial`<br />

https://chatgpt.com/share/68c59d93-e0b0-8012-a353-ad0233f00d6b


./ultra_simple --channel --serial /dev/ttyUSB0 115200
rplidar a2m8

roslaunch rplidar_ros view_rplidar .launch

source ~catkin_ws/src/devel/setup.bash



Di Rviz
add laser scan kemudian ubah map menjadi laser


Camera nvgstcapture-1.0 ### Camera Jetson
gst-launch-1.0 v4l2src device=/dev/video1 ! xvimagesink ## Camera CRO-U





vnc server
pass : vtol123
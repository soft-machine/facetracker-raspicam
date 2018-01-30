#This script is useful if you are testing the codes with a separate monitor via ssh to th raspberry
#the results will show on a display connected straight to the raspberry instead of ssh via -X
sudo killall xinit
sudo xinit -- :1 &
export DISPLAY=:1.0

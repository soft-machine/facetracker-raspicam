# facetracker-raspicam

Built on a raspberry pi 3 model B v1.2 with raspbian lite (headless image)

apt-get install python-opencv

run the final code simply this way (if signed in through ssh be sure to add -X to ssh parameters):

python facetracker-raspicam.py

if desire to show results on separate screen while control in ssh see the script restart_x.sh

For information: opencv works with the raspicam here but is slow (3 second delay). more work to be done!

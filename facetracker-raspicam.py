"""This code seems to be working fine for the intended purpose of finding faces and drawing a square around them.
It is however very slow (3 second delay). Still work to be done here"""

import time
import picamera
import numpy as np
import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
time.sleep(1)

while True:
        image = np.empty((480 * 640 * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((480, 640, 3))

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting image
        cv2.imshow('Video', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

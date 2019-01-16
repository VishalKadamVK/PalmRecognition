"""
This file is used for create face dataset
"""

import cv2
import os

closedPalmDetect = cv2.CascadeClassifier('closed_palm.xml')
openPalmDetect = cv2.CascadeClassifier('open_palm.xml')
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    closedPalm = closedPalmDetect.detectMultiScale(gray, 1.3, 5)
    openPalm = openPalmDetect.detectMultiScale(gray, 1.3, 5)
    palm, palmStatus = (openPalm, "Open Palm") if closedPalm == () else (closedPalm, "Closed Palm")
    for(x, y, w, h) in palm:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, palmStatus, (x, y + h), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.waitKey(100)
    cv2.imshow("Hand Recognition", img)
    if (cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()


import os 
import time
import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
screen_width = 640
screen_height = 480  # 480p
cap.set(3, screen_width)
cap.set(4, screen_height)
dim = (screen_width, screen_height)
# filename = str(time.strftime("%H%M%S"))+str('.mp4')
filename = str('123.mp4')

# cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 30, dim)

while (True):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
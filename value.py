# rgb values
# import imageio 
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# import cv2

# im = cv2.imread('dog.jpg')
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# # pix_val = list(im.getdata())
# # print(pix_val)
# cv2.imshow('Gratscale', gray)


# import cv2
# image = cv2.imread('dog.jpg')
# re = cv2.resize(image, (320, 240))
# # cv2.imshow('Original', image)
# gray = cv2.cvtColor(re, cv2.COLOR_BGR2GRAY)
# # cv2.imshow('Grayscale', gray)
# cv2.waitKey()
# # print(type(gray))
# print(gray.shape)

# # for i in range (0, 640):
# #     print(gray[100, i])
# arr = gray[100]
# print(arr)

import cv2
intc = 20
# image = cv2.imread('i.png')
# re = cv2.resize(image, (320, 240))
cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)
while True:
    
    rect, frame = cap.read()
    # cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    dim = gray.shape
    print("dim is {}".format(dim))
    # print(80*dim[0]/100)
    # print(int(math.floor(80*dim[0]/100)))
    print(gray[int(80*dim[0]/100)])
    arr = gray[int(80*dim[0]/100)]
    print(len(arr))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imshow('chess', cap)
cv2.waitKey(0)


# print(arr)
# for i in range (0, 5):
#     arr = gray[i]
#     for j in range (0, 225):
#         if (arr[j] > 200):
#             print(str(i) + "," + str(j))

# j = 0
for j in range (0, len(arr)):
    if (arr[j] < intc):
        # print(str(j) + " val=" + str(arr[j]))
        l = j
        print("left = " + str(l))
        break

for j in range (j, len(arr)):
    if (arr[j] > intc):
        r = j-1
        print('right = ' + str(r))
        break

l_cent = int((l+r)/2)
print("line center = {}".format(l_cent))
f_cent = int(len(arr)/2)
print("frame center = {}".format(f_cent))

if (l_cent < (f_cent-10)):
    print("turn left")
elif (l_cent > (f_cent + 10)):
    print("turn right")
else:
    print("forward")

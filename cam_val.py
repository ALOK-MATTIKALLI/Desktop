import cv2
import time
intc = 50

cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)

while True:
    l=0
    r=0
    rect, frame = cap.read()
    # cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    dim = gray.shape
    arr = gray[int(80*dim[0]/100)]
    rag = int(len(arr)*6/100)
    for j in range (0, len(arr)):
        if (arr[j] < intc):
            l = j
            break
    # print("left = " + str(l))
    for j in range (j, len(arr)):
        if (arr[j] > intc):
            r = j-1
            break
    # print('right = ' + str(r))
    l_cent = int((l+r)/2)
    # print("line center = {}".format(l_cent))
    f_cent = int(len(arr)/2)
    l = (l - f_cent)
    r = (r - f_cent)
    # print(l)
    # print(r)
    # if (l < 0 and r > 0):
    #     print("forward")
    # elif (l<0 and r<0):
    #     print("left")
    # elif(l>0 and r>0):
    #     print("right")

    # print("frame center = {}".format(f_cent))
    # acc = int((((f_cent - l_cent)*1.0)/f_cent)*100)
    # r_val = f_cent - r
    # l_val = f_cent - l
    # print(r_val)
    # print(l_val)
    acc = (((r-l)*1.0)/f_cent)*100
    # print(acc)
    # if (acc > 20):
    #     print("left" + str(acc))
    # elif (acc < -20):
    #     print("right" + str(acc*(-1)))
    # elif ((acc >= -20) and (acc <= 20)):
    #     print("forward")
    # else:
    #     print("stop")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.005)
    

cap.release()
cv2.destroyAllWindows()
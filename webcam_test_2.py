import cv2
cap = cv2.VideoCapture(0)
w = 640
h = 480
cap.set(3, w)
cap.set(4, h)
h_r = int(h*0.80)

while True:

    rect, frame = cap.read()
    # cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    # print(gray[h_r])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # print(frame.shape)
        break

cap.release()
cv2.destroyAllWindows()

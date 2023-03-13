import numpy as np
import cv2 as cv
from motor_control import MotorControl
import time


class VideoProcess:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.pins = [17,27,10,9]
        self.drive = MotorControl(self.pins)


    def video_frame(self, frame_resize=100):
        cap = cv.VideoCapture(self.camera_id)
        prev_circle = None
        def dist(x1, y1, x2, y2): return (x1-x2)**2 + (y1-y2)**2

        while True:
            ret, frame = cap.read()
            frame = self.frame_resize(frame, frame_resize)

            if not ret:
                print("Video read error!")
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (17, 17), 0)

            circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1.2, 150,
                                      param1=90, param2=25, minRadius=75, maxRadius=150)

            if circles is not None:
                circles = np.uint16(np.around(circles))
                chosen = None
                for i in circles[0, :]:
                    if chosen is None:
                        chosen = i
                    if prev_circle is not None:
                        if dist(chosen[0], chosen[1], prev_circle[0], prev_circle[1]) <= dist(i[0], i[1], prev_circle[0], prev_circle[1]):
                            chosen = i

                cv.circle(frame, (chosen[0], chosen[1]), 1, (100, 100, 100), 3)
                cv.circle(frame, (chosen[0], chosen[1]),
                          chosen[2], (0, 255, 255), 3)
                self.motor_drive(frame.shape,chosen)
                prev_circle = chosen

            self.draw_centre_lines(frame)
            cv.imshow("Circles", frame)

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                cap.release()
                break

    def frame_resize(self, image, resize_percent):
        width = int(image.shape[1] * resize_percent/100)
        height = int(image.shape[0] * resize_percent/100)
        dim = (width, height)
        return cv.resize(image, dim, interpolation=cv.INTER_AREA)

    def draw_centre_lines(self, image):
        cv.line(
            image, (0, int(image.shape[0]/2)), (image.shape[1], int(image.shape[0]/2)), (0, 255, 0), 2)
        cv.line(image, (int(image.shape[1]/2), 0),
                (int(image.shape[1]/2), image.shape[0]), (0, 255, 0), 2)
        
    def motor_drive(self, image_size, points):
        # print(image_size, points)
        x, y = int(image_size[1]/2), int(image_size[0]/2)
        print(x,y,(0.6 * image_size[1]), points)
        if points[0] > int(0.6 * image_size[1]):
            self.drive.drive(5,-5)

        elif points[0] < int(0.4 * image_size[1]):
            self.drive.drive(-5,5)

        else:
            self.drive.drive(0,0)
        
        


def main():
    event = VideoProcess(camera_id=0)
    event.video_frame(100)


if __name__ == "__main__":
    main()

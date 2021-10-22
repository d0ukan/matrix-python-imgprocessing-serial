import cv2
import numpy as np
import serial
import keyboard
from time import sleep

# Tracker Types
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
tracker = cv2.TrackerCSRT_create()
# tracker = cv2.TrackerMOSSE_create()

ser = serial.Serial('COM5', 9600)
sleep(3)


def AutoEdge(blur, isg=0.33):
    med = np.median(blur)
    low = int(max(0, (1 - isg) * med))
    hih = int(max(255, (1 + isg) * med))
    edge = cv2.Canny(blur, low, hih)
    return edge


h_px = 360
w_px = 640
cap = cv2.VideoCapture(0)
cap.set(3, w_px)  # horizontal res
cap.set(4, h_px)

success, frame = cap.read()
bbox = cv2.selectROI("Select", frame, False)
tracker.init(frame, bbox)


def drawBoxauto(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 175), 2, 3)
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 175), 2)
    xcenter = x + (w / 2)
    ycenter = y + (h / 2)
    cv2.line(img, (int(x + w / 2), int(y)), (int(x + w / 2), int(y + h)), (0, 225, 0), 2)  # BAK
    cv2.line(img, (int(x), int(y + h / 2)), (int(x + w), int(y + h / 2)), (0, 225, 0), 2)  # BAK
    cv2.circle(img, (int((x + w / 2)), int((y + h / 2))), 3, (220, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x), int(y)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x + w), int(y)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x), int(y + h)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x + w), int(y + h)), 3, (255, 0, 0), 3)  # BAK

    if xcenter < 240:
        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Left")
        # print("*" * 20)
        # eCart.moveL(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        if xcenter < 120:
            ser.write(b'l')
        elif xcenter >= 120 and xcenter < 240:
            ser.write(b'k')

    elif xcenter > 400:
        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Right")
        # print("*" * 20)
        # eCart.moveR(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        if xcenter > 520:
            ser.write(b'r')
        elif xcenter <= 520 and xcenter > 400:
            ser.write(b't')

    elif xcenter >= 240 and xcenter <= 400:
        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Middle")
        # print("*" * 20)
        ser.write(b'm')
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK

    else:

        print("no detection")


def drawBoxmanual(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 175), 2, 3)
    cv2.putText(img, "Tracking", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 175), 2)
    xcenter = x + (w / 2)
    ycenter = y + (h / 2)
    cv2.line(img, (int(x + w / 2), int(y)), (int(x + w / 2), int(y + h)), (0, 225, 0), 2)  # BAK
    cv2.line(img, (int(x), int(y + h / 2)), (int(x + w), int(y + h / 2)), (0, 225, 0), 2)  # BAK
    cv2.circle(img, (int((x + w / 2)), int((y + h / 2))), 3, (220, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x), int(y)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x + w), int(y)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x), int(y + h)), 3, (255, 0, 0), 3)  # BAK
    cv2.circle(img, (int(x + w), int(y + h)), 3, (255, 0, 0), 3)  # BAK

    cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
    cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
    cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK

    ser.write(b's')

    if keyboard.is_pressed('a'):

        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Left")
        # print("*" * 20)
        ser.write(b'a')
        # ser.write(b'200')
        # eCart.moveL(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK


    elif keyboard.is_pressed('d'):

        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Right")
        # print("*" * 20)
        ser.write(b'd')
        # ser.write(b'450')
        # eCart.moveR(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK

    elif keyboard.is_pressed('w'):
        print("*" * 20)
        print("x :", str(int(xcenter)), " wid :", int(h), "Middle : Go Forward")
        # print("*" * 20)
        ser.write(b'w')
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK

    else:

        print("No key pressed")


def drawBoxno(img):
    cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
    cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
    cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK

    ser.write(b's')

    if keyboard.is_pressed('a'):

        print("*" * 20)
        print("Left")
        # print("x :", str(int(xcenter)), " wid :", int(h), "Left")
        # print("*" * 20)
        ser.write(b'a')
        # ser.write(b'200')
        # eCart.moveL(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK


    elif keyboard.is_pressed('d'):

        print("*" * 20)
        print("Right")
        # print("x :", str(int(xcenter)), " wid :", int(h), "Right")
        # print("*" * 20)
        ser.write(b'd')
        # ser.write(b'450')
        # eCart.moveR(15,15)
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK

    elif keyboard.is_pressed('w'):
        print("*" * 20)
        print("Forward")
        # print("x :", str(int(xcenter)), " wid :", int(h), "Middle : Go Forward")
        # print("*" * 20)
        ser.write(b'w')
        cv2.putText(img, "Left", (100, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK
        cv2.putText(img, "Middle", (295, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 0), 2);  # BAK
        cv2.putText(img, "Right", (480, 345), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 220), 2);  # BAK

    else:

        print("No key pressed")


while True:

    while True:  # auto
        timer = cv2.getTickCount()
        success, img = cap.read()
        success, bbox = tracker.update(img)

        ft, img2 = cap.read()  # BAK

        if success:
            drawBoxauto(img, bbox)
        else:
            cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 175), 2)
            drawBoxno(img)

        cv2.rectangle(img, (10, 15), (200, 90), (255, 150, 50), 2)
        cv2.putText(img, "Fps:", (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 150, 0), 2);
        cv2.putText(img, "Status:", (15, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 150, 0), 2);

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        cv2.line(img, (240, 0), (240, 480), (225, 225, 225), 7)  # BAK
        cv2.line(img, (400, 0), (400, 480), (225, 225, 225), 7)  # BAK

        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # BAK
        blur = cv2.GaussianBlur(gray, (3, 3), 0)  # BAK

        auto = AutoEdge(blur)  # BAK

        if fps > 60:
            myColor = (20, 230, 20)

        elif fps > 20:
            myColor = (230, 20, 20)

        else:
            myColor = (20, 20, 230)

        cv2.putText(img, str(int(fps)), (65, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

        cv2.imshow("Camera", img)
        cv2.imshow("CamView", auto)  # BAK

        if keyboard.is_pressed('x'):
            print("Manuel")
            sleep(0.2)
            break
        if cv2.waitKey(1) & 0xff == 27:
            break

    while True:  # manual
        timer = cv2.getTickCount()
        success, img = cap.read()
        success, bbox = tracker.update(img)

        ft, img2 = cap.read()  # BAK

        if success:
            drawBoxmanual(img, bbox)
        else:
            cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 175), 2)
            drawBoxno(img)

        cv2.rectangle(img, (10, 15), (200, 90), (255, 150, 50), 2)
        cv2.putText(img, "Fps:", (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 150, 0), 2);
        cv2.putText(img, "Status:", (15, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 150, 0), 2);

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        cv2.line(img, (240, 0), (240, 480), (225, 225, 225), 7)  # BAK
        cv2.line(img, (400, 0), (400, 480), (225, 225, 225), 7)  # BAK

        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # BAK
        blur = cv2.GaussianBlur(gray, (3, 3), 0)  # BAK

        auto = AutoEdge(blur)  # BAK

        if fps > 60:
            myColor = (20, 230, 20)

        elif fps > 20:
            myColor = (230, 20, 20)

        else:
            myColor = (20, 20, 230)

        cv2.putText(img, str(int(fps)), (65, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

        cv2.imshow("Camera", img)
        cv2.imshow("CamView", auto)  # BAK

        if keyboard.is_pressed('x'):
            print("Auto")
            sleep(0.2)
            break
        if cv2.waitKey(1) & 0xff == 27:
            break
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
ser.close()



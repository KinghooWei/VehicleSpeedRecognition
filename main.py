import cv2
import cv2.cv2
import numpy as np
import math

np.set_printoptions(threshold=np.inf, linewidth=850)


def virtualLoop(img, info):  # info 0旋转中心x 1旋转中心y 2旋转角度 3宽 4高
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    # print(h,w)
    theta = info[2]
    matRotate = cv2.getRotationMatrix2D((info[0], info[1]), theta, 1)
    img = cv2.warpAffine(img, matRotate, (w, h))
    width = info[3]

    height = info[4]
    # cv2.imshow("win", img[a[1]:a[1] + height][a[0]:a[0] + width])
    sum = 0
    for i in range(height):
        for j in range(width):
            sum += img[int(info[1] - width / 2 + j)][int(info[0] - height / 2 + i)]
    mean = sum / width / height
    # print(mean)
    return mean


def paint(img, info):  # info 0旋转中心x 1旋转中心y 2旋转角度 3长 4宽
    x = info[0]
    y = info[1]
    theta = info[2]
    width = info[3]
    height = info[4]
    anglePi = -theta * math.pi / 180.0
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)

    x1 = x - 0.5 * width
    y1 = y - 0.5 * height

    x0 = x + 0.5 * width
    y0 = y1

    x2 = x1
    y2 = y + 0.5 * height

    x3 = x0
    y3 = y2

    x0n = int((x0 - x) * cosA - (y0 - y) * sinA + x)
    y0n = int((x0 - x) * sinA + (y0 - y) * cosA + y)

    x1n = int((x1 - x) * cosA - (y1 - y) * sinA + x)
    y1n = int((x1 - x) * sinA + (y1 - y) * cosA + y)

    x2n = int((x2 - x) * cosA - (y2 - y) * sinA + x)
    y2n = int((x2 - x) * sinA + (y2 - y) * cosA + y)

    x3n = int((x3 - x) * cosA - (y3 - y) * sinA + x)
    y3n = int((x3 - x) * sinA + (y3 - y) * cosA + y)

    cv2.line(img, (x0n, y0n), (x1n, y1n), (0, 0, 255))
    cv2.line(img, (x1n, y1n), (x2n, y2n), (0, 0, 255))
    cv2.line(img, (x2n, y2n), (x3n, y3n), (0, 0, 255))
    cv2.line(img, (x3n, y3n), (x0n, y0n), (0, 0, 255))

    return img


def rotate(img):
    height, width = img.shape[:2]
    des = []

    for i in range(width):
        row = []
        for j in range(height):
            row.append(img[j][i])
        des.append(row)
    return des


cap = cv2.VideoCapture('uusgu-1bxuj.mp4')
velocity = None
k = 0
while 1:
    k += 1
    # get a frame
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (450, 800))  # 调整大小
        loop1 = [285, 585, 40, 40, 7]
        loop2 = [210, 515, 40, 40, 7]
        if k == 1:
            hasEnter = False
            # print(hasEnter)
            initLoop1 = virtualLoop(frame, loop1)  # info 0旋转中心x 1旋转中心y 2旋转角度 3长 4宽
            initLoop2 = virtualLoop(frame, loop2)
        else:
            laterLoop1 = virtualLoop(frame, loop1)
            laterLoop2 = virtualLoop(frame, loop2)

            change1 = abs(laterLoop1 - initLoop1)
            change2 = abs(laterLoop2 - initLoop2)
            if change1 > 25 and hasEnter == False:
                hasEnter = True
                enterFrame = k
                print("车辆通过第一条虚拟线圈")
            if change2 > 25 and hasEnter == True:
                hasEnter = False
                outFrame = k
                velocity = 1080 / (outFrame - enterFrame)
                time = 38 / (velocity * 10 / 36)
                print("车辆通过第二条虚拟线圈")
                print("时速：", velocity, "Km/s")
                print("预计", time, "s后撞线\n")
        if hasEnter:
            frame = cv2.putText(frame, "The vehicle has passed the first virtual coil", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
        elif velocity is not None:
            frame = cv2.putText(frame, "The vehicle has passed the second virtual coil", (10, 35),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
            frame = cv2.putText(frame, "The speed is " + str('%.2f' % velocity) + "Km/s", (10, 55),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
            frame = cv2.putText(frame, "Expect the car to hit the line in " + str('%.2f' % time) + "s", (10, 75),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
        frame = paint(frame, loop1)
        frame = paint(frame, loop2)
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

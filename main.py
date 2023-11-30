import cv2 
import os
import winsound
import time

gradient = " .:;+=xX$&"

def color2text(color: list[int]):
    return gradient[int(round(sum(color) / len(color) / 255 * 9))]

cam = cv2.VideoCapture("【東方】Bad Apple!! ＰＶ【影絵】 [FtutLA63Cp8].webm")
while True:
    x,y = os.get_terminal_size()
    ret, frame = cam.read()

    if not ret:
        break

    pixels = cv2.resize(frame, (x,y), interpolation=cv2.INTER_LINEAR)

    for col in pixels:
        for pixel in col:
            print(color2text(pixel), end="")
        print()

    time.sleep(0.03)

    # cv2.namedWindow("good apple", cv2.WINDOW_NORMAL)
    # cv2.imshow("good apple", frame)

cam.release()
cv2.destroyAllWindows()
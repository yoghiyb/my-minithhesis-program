import cv2 as cv
import numpy as np


def b_reduct(src=0):
    cam = cv.VideoCapture(src)
    fgbg = cv.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cam.read()
        fgmask = fgbg.apply(frame)

        cv.imshow('Ori', frame)
        cv.imshow('fg', fgmask)

        k = cv.waitKey(1) & 0xff
        if k == 27:
            break

    cam.release()
    cv.destroyAllWindows()


# b_reduct()

def thresholding(src=0):
    cam = cv.VideoCapture(src)

    while True:
        ret, frame = cam.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # t_ret, thres = cv.threshold(gray, 12, 255, cv.THRESH_BINARY)
        thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
        cv.imshow('Ori', frame)
        cv.imshow('thres', thres)

        k = cv.waitKey(1) & 0xff
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()


# thresholding()

def color_filtering(src=0):
    cam = cv.VideoCapture(src)

    while True:
        _, frame = cam.read()
        # rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_red = np.array([30, 150, 50])
        upper_red = np.array([255, 255, 180])

        mask = cv.inRange(hsv, lower_red, upper_red)
        res = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow('frame', frame)
        cv.imshow('mask', mask)
        cv.imshow('res', res)

        k = cv.waitKey(1) & 0xff
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()
color_filtering()

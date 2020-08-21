import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import PIL.Image, PIL.ImageTk
import ctypes

cigarette = cv2.CascadeClassifier('classifiers/cigarette-detect.xml')
faced = cv2.CascadeClassifier('classifiers/face-detect.xml')

cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faced.detectMultiScale(gray, 1.3, 5)
    cigarettes = cigarette.detectMultiScale(gray, 1.5, 8)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for x_, y_, w_, h_ in cigarettes:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(img, (x_, y_), (x_ + w_, y_ + h_), (0, 0, 255), 2)
            # if x in range(x_, x_ + w_) and y in range(y_, y_ + h_):
            #     cv2.imwrite("save_%s_%s.jpg" % (x, y), img)
    # for x, w, y, h in cigarettes:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('test', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()

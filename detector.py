import mysql.connector
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.read("dataTrain/trainingData.xml")
cascadePath = "classifiers/face-detect.xml"
face = cv2.CascadeClassifier(cascadePath)
rokok = cv2.CascadeClassifier("classifiers/rokok-detect.xml")

def getProfile(Id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="facebase"
    )
    cmd = "SELECT * FROM mhs WHERE id=" + str(Id)
    cursor = conn.cursor()
    cursor.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


# def detect(video_source=0):
#     cam = cv2.VideoCapture(video_source)
#     width, height = 100, 100
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     while True:
#         ret, im = cam.read()
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         faces = face.detectMultiScale(gray, 1.3, 5)
#         rokoks = rokok.detectMultiScale(gray, 1.5, 10)
#         for (x, y, w, h) in faces:
#             id, conf = recognizer.predict(cv2.resize(gray[y:y + h, x:x + w], (width, height)))
#             cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             cv2.imwrite('img_hasil/frame.jpg', gray)
#             if conf < 3500:
#                 profile = getProfile(id)
#                 if (profile != None):
#                     kepercayaan = "{0:.2f}%".format(round(100 - (conf / 100)), 2)
#                     cv2.putText(im, kepercayaan, (x, y), font, 1.0, (0, 255, 0))
#                     cv2.putText(im, str(profile[1]), (x, y + h + 30), font, 1.0, (0, 255, 0))
#                     cv2.putText(im, str(profile[2]), (x, y + h + 60), font, 1.0, (0, 255, 0))
#                     cv2.putText(im, str(profile[3]), (x, y + h + 90), font, 1.0, (0, 255, 0))
#             else:
#                 cv2.putText(im, "Tidak dikenali", (x, y + h + 30), font, 1.0, (0, 255, 0))
#
#         for (x, y, w, h) in rokoks:
#             cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 0), 2)
#             # cv2.imwrite('rokok.jpg', gray[y:y + h, x:x + w])
#
#         cv2.imshow('Detector', im)
#         k = cv2.waitKey(1) & 0xff
#         if k == 27:
#             break
#     cam.release()
#     cv2.destroyAllWindows()

# detect('D:/py/skripsi/video/rowing.mp4')
# detect()

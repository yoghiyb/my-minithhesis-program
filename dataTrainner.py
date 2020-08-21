import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.EigenFaceRecognizer_create()
# recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'

def getImagesWhitID(path):
    width_d, height_d = 100, 100
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePaths in imagePaths:
        faceImg = Image.open(imagePaths).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID =int(os.path.split(imagePaths)[-1].split('.')[1])
        faces.append(cv2.resize(faceNp, (width_d,height_d)))
        IDs.append(ID)
        cv2.imshow("Trainner", faceNp)
        cv2.waitKey(10)
    return IDs, faces

def Train():
    Ids, faces = getImagesWhitID(path)
    recognizer.train(faces, np.array(Ids))
    recognizer.save('dataTrain/trainingData.xml')
    # recognizer.save('dataTrain/trainingDataLBPH.xml')
    cv2.destroyAllWindows()

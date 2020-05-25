import cv2
from model import FacialExpressionModel
import numpy as np 
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
model = FacialExpressionModel("model.json","ModelWeights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

class VidCamera(object):
    def __init__(self):
        self.Video = cv2.VideoCapture(0)

    def __del__(self):
        self.Video.release()

    def get_frame(self):
        _, fr = self.Video.read()
        gray_fr = cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray_fr,1.3,5)

        for x,y,w,h in faces:
            fc = gray_fr[y:y+h,x:x+w]

            roi = cv2.resize(fc,(48,48))
            predict = model.predict_emotions(roi[np.newaxis,:,:,np.newaxis])
            cv2.putText(fr,predict,(x,y),font,1,(255,255,0),2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)

        _,jpeg = cv2.imencode('.jpg',fr)
        return jpeg.tobytes()
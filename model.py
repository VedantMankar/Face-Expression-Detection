from tensorflow.keras.models import model_from_json
import numpy as np 
import tensorflow as tf 


class FacialExpressionModel(object):
    emotions_list = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprise"]

    def __init__(self,model_json_file,model_weights_file):
        with open("model.json","r") as json_file:
            loaded_modeljson = json_file.read()
            self.loaded_model = model_from_json(loaded_modeljson)
        
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model._make_predict_function()

    def predict_emotions(self,img):
        self.pred = self.loaded_model.predict(img)
        return FacialExpressionModel.emotions_list[np.argmax(self.pred)]



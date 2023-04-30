# Face-Expression-Detection
## Project Description
  <br>This Project is built to detect the facial expressions of humans. Today with an increase in AI, various systems have been built on recognizing people's expressions and hence reccomend them some products based on it.The first step to build such systems wis to identify peoples emotions which is performed here.Here a model has been trained on 7 universal expressions which are 1)Happy, 2) Sad , 3)Surprise , 4) Neutral , 5)Angry , 6) Fear, 7)Disgust <br>
 ## Dataset Description
  The dataset was taken from kaggle challenge for [Facial Expression Recognition](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge)
  
## Data Preprocessing
The dataset consisted of
7164 happy images
4982 neutral images
3993 angry images
436 disgust images
3205 surprise images
4103 fear images
4938 sad images

To help the model learn better, Data Augmentation was done. The images were flipped horizontally and vertically, rotated and split into training and validation set.
  
  
## Building Model
 We used 2D Convolutional Networks to for training on the images. The model structure is shown below
 
 ![image](https://user-images.githubusercontent.com/51293708/235333637-74ea5e8b-d6d8-4d8f-bd84-c9bd3bfdaa85.png)



## Model Performance
The model achieved a validation accuracy of 61.48%. The model was saved in a pickle file

## Building a web app to capture real time facial expressions

*  model.py : Loads the model with its weights and predicts the facial expression
*  camera.py : Captures real time video of your face. Extracts the facial features using harrcascade classifier. Displays the type of your facial expression
*  main.py : A flask app which uses both of the above files and runs on a localhost server

## Running the model

Download the following files 
model.json
ModelWeights.h5
haarcascade_frontalface_default.xml


run the following line
python main.py



  
  
  
  
  
  
  
  
  
  
  


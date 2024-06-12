import pandas as pd
import os
import cv2
from datetime import datetime

count = 1
countFolder = 0

#GET CURRENT DIRECTORY PATH
path = 'DataCollected/IMG001'
myDirectory = os.path.join(os.getcwd(), path)
# print(myDirectory)

# CREATE A NEW FOLDER BASED ON THE PREVIOUS FOLDER COUNT
while os.path.exists(os.path.join(myDirectory,{str(countFolder)})):
        countFolder += 1
newPath = myDirectory +"/"+str(countFolder)
os.makedirs(newPath)

# SAVE IMAGES IN THE FOLDER
def saveData(img):
    if(count % 10 == 0):
        count = 0
        countFolder = 1
        os.makedirs(myDirectory +"/"+str(countFolder))
    
    fileName = os.path.join(newPath,f'image_{count}.jpg')
    cv2.imwrite(fileName, img)


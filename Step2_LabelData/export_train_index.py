import os 
import cv2 
import numpy as np 
from main_label import label_lanes
import random

path_truth = 'D:/dataset_test/truth/'
path_image = 'D:/dataset_test/image/'

s = ''

#folders = ['IMG003', 'IMG005', 'IMG008']
# folders = ['IMG011', 'IMG012', 'IMG013'] # train
folders = ['IMG014']

for folder in folders:
    path_IMG = path_image + folder + '/'
    lst_image =os.listdir(path_IMG)
    for folder_name in lst_image:
        images_file_name = os.listdir(path_IMG + folder_name + '/')
        if len(images_file_name) != 5:
            print(folder)
            print(folder_name)
            print(images_file_name)
        for filename_image in images_file_name:
            s += path_IMG + folder_name + '/' + filename_image + ' '
        s += path_truth + folder + '/' + folder_name + '.jpg' + '\n'

file_txt = 'val_index.txt'
with open(file_txt, 'w') as file:
    file.write(s)

# print(s)
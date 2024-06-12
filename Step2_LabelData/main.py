import os 
import cv2 
import numpy as np 
from main_label import label_lanes

sub_path = 'IMG014'
sub_path_label = 'IMG014_Label'


path = f'D:/University/SuaKichThuocAnh/{sub_path}/'
path_new = f'./{sub_path_label}/'

for item in os.listdir(path):
    item_path = os.path.join(path, item)
    print(item_path)

    filename_label = item_path + f'/image_3.jpg'
    new_filename_label = path_new + item + '.jpg'
    print('new: ',new_filename_label)

    label_lanes(filename_label, new_filename_label)



    # label_lanes(filename = filename_label, )
    
    

# stt = 8

# for _ in range(7):
#     fullname = path + f'lane_{stt}.jpg'
#     print(fullname)
#     fullname_new = path_new + f'lane_{stt}.jpg'
#     label_lanes(filename = fullname, filename_new = fullname_new)
#     stt += 15
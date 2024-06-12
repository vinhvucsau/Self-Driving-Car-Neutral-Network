from torch.utils.data import Dataset
from PIL import Image
import torch
import config
import torchvision.transforms as transforms
import numpy as np
from sklearn import preprocessing

def readTxt(file_path):
    img_list = []
    with open(file_path, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
            item = lines.strip().split()
            img_list.append(item)
    file_to_read.close()
    return img_list

class RoadSequenceDatasetList(Dataset):

    def __init__(self, img_list, transforms):

        self.img_list = img_list
        self.dataset_size = len(self.img_list)
        self.transforms = transforms
    def __len__(self):
        return self.dataset_size

    def __getitem__(self, idx):
        image_list = self.img_list[idx]
        data = []
        for i in range(len(image_list)): 
            data.append(torch.unsqueeze(self.transforms(Image.fromarray(image_list[i])), dim=0))
        data = torch.cat(data, 0)

        sample = {'data': data}

        return sample



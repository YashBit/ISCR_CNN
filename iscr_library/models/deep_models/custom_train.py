import matplotlib.pyplot as plt
from pandas.core.common import flatten
import copy
import numpy as np
import random

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data import Dataset, DataLoader
from torch.utils.data import DataLoader

import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2

import glob
from tqdm import tqdm
from torch.autograd import Variable 
from dataset import CustomDatasetFromFile


####################################################
#       Create Train, Valid and Test sets
####################################################

def createImagesAndLabels(path_to_train_images, path_to_test_images):
    train_data_path = path_to_train_images #images/train
    test_data_path = path_to_test_images #images/test

    train_image_paths = [] #to store image paths in list
    classes = [] #to store class values

    #1.
    # get all the paths from train_data_path and append image paths and class to to respective lists
    # eg. train path-> 'images/train/A/4321ee6695c23c7b.jpg'
    # eg. class -> 26.Pont_du_Gard
    for data_path in glob.glob(train_data_path + '/*'):
        classes.append(data_path.split('/')[-1]) 
        train_image_paths.append(glob.glob(data_path + '/*'))
        
    train_image_paths = list(flatten(train_image_paths))
    random.shuffle(train_image_paths)

    print('train_image_path example: ', train_image_paths[0])
    print('class example: ', classes[0])

    #2.
    # split train valid from train paths (80,20)
    train_image_paths, valid_image_paths = train_image_paths[:int(0.8*len(train_image_paths))], train_image_paths[int(0.8*len(train_image_paths)):] 

    #3.
    # create the test_image_paths
    test_image_paths = []
    for data_path in glob.glob(test_data_path + '/*'):
        test_image_paths.append(glob.glob(data_path + '/*'))

    test_image_paths = list(flatten(test_image_paths))

    print("Train size: {}\nValid size: {}\nTest size: {}".format(len(train_image_paths), len(valid_image_paths), len(test_image_paths)))
    return (train_image_paths, valid_image_paths,test_image_paths )


#######################################################
#                  Visualize Dataset
#         Images are plotted after augmentation
#######################################################

def visualize_augmentations(dataset, idx=0, samples=10, cols=5, random_img = False):
    
    dataset = copy.deepcopy(dataset)
    #we remove the normalize and tensor conversion from our augmentation pipeline
    dataset.transform = A.Compose([t for t in dataset.transform if not isinstance(t, (A.Normalize, ToTensorV2))])
    rows = samples // cols
    
        
    figure, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(12, 8))
    for i in range(samples):
        if random_img:
            idx = np.random.randint(1,len(train_image_paths))
        image, lab = dataset[idx]
        ax.ravel()[i].imshow(image)
        ax.ravel()[i].set_axis_off()
        ax.ravel()[i].set_title(idx_to_class[lab])
    plt.tight_layout(pad=1)
    plt.show()    

#######################################################
#                  Define Dataloaders
#######################################################
train_path= '/images/train/'
test_path = '/images/test/'
train_image_paths, valid_image_paths,test_image_paths = createImagesAndLabels(train_path, test_path)

train_dataset = CustomDatasetFromFile(train_image_paths,train_transforms)
valid_dataset = CustomDatasetFromFile(valid_image_paths,test_transforms) #test transforms are applied
test_dataset = CustomDatasetFromFile(test_image_paths,test_transforms)

visualize_augmentations(train_dataset,np.random.randint(1,len(train_image_paths)), random_img = True)

train_loader = DataLoader(
    train_dataset, batch_size=64, shuffle=True
)

valid_loader = DataLoader(
    valid_dataset, batch_size=64, shuffle=True
)


test_loader = DataLoader(
    test_dataset, batch_size=64, shuffle=False
)


#Any model class imported here 
model = MnistCNNModel()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for i, (images, labels) in enumerate(train_loader):
    images = Variable(images)
    labels = Variable(labels)
    # Clear gradients
    optimizer.zero_grad()
    # Forward pass
    outputs = model(images)
    # Calculate loss
    loss = criterion(outputs, labels)
    # Backward pass
    loss.backward()
    # Update weights
    optimizer.step()
    break

print('A single forward-backward pass is done!')
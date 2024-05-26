# install pytorch and matplotlib albumentations captum

# pip install matplotlib albumentations captum

# /path/to/dataset/
#     ├── class1/
#     │   ├── image1.jpg
#     │   ├── image2.jpg
#     │   └── ...
#     ├── class2/
#     │   ├── image1.jpg
#     │   ├── image2.jpg
#     │   └── ...
#     ├── class3/
#     │   ├── image1.jpg
#     │   ├── image2.jpg
#     │   └── ...
#     └── ...


import os
import cv2
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from albumentations import Compose, Normalize, Resize, HorizontalFlip, VerticalFlip, RandomRotate90, RandomBrightnessContrast
from albumentations.pytorch import ToTensorV2
from captum.attr import IntegratedGradients, visualization as viz

class CustomDatasetFromFile(Dataset):
    def __init__(self, image_paths, class_to_idx, transform=None):
        self.image_paths = image_paths
        self.class_to_idx = class_to_idx
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_filepath = self.image_paths[idx]
        image = cv2.imread(image_filepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        label = image_filepath.split('/')[-2]
        label = self.class_to_idx[label]
        if self.transform:
            image = self.transform(image=image)['image']

        return image, label

class Model:
    def __init__(self, model_name, n_classes, train=True, pretrain_imagenet=True, fine_tuning=True, dataset_path=None, hyparams=None):
        self.model_name = model_name
        self.n_classes = n_classes
        self.train = train
        self.pretrain_imagenet = pretrain_imagenet
        self.fine_tuning = fine_tuning
        self.dataset_path = dataset_path
        self.hyparams = hyparams if hyparams is not None else {}

        # Initialize model
        self._initialize_model()

        # Specify the device
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Move to the specified device
        self.model = self.model.to(self.device)

        # Load dataset if path is provided
        if self.dataset_path:
            self._load_datasets()

        # Initialize optimizer and loss function
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.hyparams.get('learning_rate', 0.001))

    def _initialize_model(self):
        if self.model_name == 'vgg16':
            self.model = models.vgg16(pretrained=self.pretrain_imagenet)
            if not self.fine_tuning:
                for param in self.model.parameters():
                    param.requires_grad = False
            n_inputs = self.model.classifier[6].in_features
            self.model.classifier[6] = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, self.n_classes), nn.LogSoftmax(dim=1))

        elif self.model_name == 'resnet50':
            self.model = models.resnet50(pretrained=self.pretrain_imagenet)
            if not self.fine_tuning:
                for param in self.model.parameters():
                    param.requires_grad = False
            n_inputs = self.model.fc.in_features
            self.model.fc = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, self.n_classes), nn.LogSoftmax(dim=1))

        elif self.model_name == 'googlenet':
            self.model = models.googlenet(pretrained=self.pretrain_imagenet)
            if not self.fine_tuning:
                for param in self.model.parameters():
                    param.requires_grad = False
            n_inputs = self.model.fc.in_features
            self.model.fc = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, self.n_classes), nn.LogSoftmax(dim=1))

    def _load_datasets(self):
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset path {self.dataset_path} does not exist.")

        image_paths = []
        class_names = sorted(os.listdir(self.dataset_path))
        for class_name in class_names:
            class_dir = os.path.join(self.dataset_path, class_name)
            if os.path.isdir(class_dir):
                for image_name in os.listdir(class_dir):
                    image_paths.append(os.path.join(class_dir, image_name))

        # Create a label encoder
        class_to_idx = {class_name: idx for idx, class_name in enumerate(class_names)}

        # Split dataset into training, validation, and testing
        train_paths, test_paths = train_test_split(image_paths, test_size=0.2, stratify=[path.split('/')[-2] for path in image_paths])
        train_paths, val_paths = train_test_split(train_paths, test_size=0.25, stratify=[path.split('/')[-2] for path in train_paths])  # 0.25 x 0.8 = 0.2

        train_transform = Compose([
            Resize(224, 224),
            HorizontalFlip(),
            VerticalFlip(),
            RandomRotate90(),
            RandomBrightnessContrast(),
            Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
            ToTensorV2()
        ])

        test_transform = Compose([
            Resize(224, 224),
            Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
            ToTensorV2()
        ])

        self.train_dataset = CustomDatasetFromFile(image_paths=train_paths, class_to_idx=class_to_idx, transform=train_transform)
        self.val_dataset = CustomDatasetFromFile(image_paths=val_paths, class_to_idx=class_to_idx, transform=test_transform)
        self.test_dataset = CustomDatasetFromFile(image_paths=test_paths, class_to_idx=class_to_idx, transform=test_transform)

        self.train_loader = DataLoader(self.train_dataset, batch_size=self.hyparams.get('batch_size', 32), shuffle=True, num_workers=4)
        self.val_loader = DataLoader(self.val_dataset, batch_size=self.hyparams.get('batch_size', 32), shuffle=False, num_workers=4)
        self.test_loader = DataLoader(self.test_dataset, batch_size=self.hyparams.get('batch_size', 32), shuffle=False, num_workers=4)

    def train_model(self, num_epochs):
        self.model.train()
        for epoch in range(num_epochs):
            running_loss = 0.0
            for images, labels in self.train_loader:
                images, labels = images.to(self.device), labels.to(self.device)

                # Zero the parameter gradients
                self.optimizer.zero_grad()

                # Forward pass
                outputs = self.model(images)
                loss = self.criterion(outputs, labels)

                # Backward pass and optimize
                loss.backward()
                self.optimizer.step()

                running_loss += loss.item()

            avg_loss = running_loss / len(self.train_loader)
            val_loss, val_accuracy = self.evaluate(self.val_loader)
            print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {avg_loss:.4f}, Val Loss: {val_loss:.4f}, Val Accuracy: {val_accuracy:.2f}%")

    def evaluate(self, loader):
        self.model.eval()
        running_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in loader:
                images, labels = images.to(self.device), labels.to(self.device)

                outputs = self.model(images)
                loss = self.criterion(outputs, labels)
                running_loss += loss.item()

                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        avg_loss = running_loss / len(loader)
        accuracy = 100 * correct / total
        return avg_loss, accuracy

    def test_model(self):
        test_loss, test_accuracy = self.evaluate(self.test_loader)
        print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.2f}%")

    def visualize_augmentations(self, num_images=5):
        self.model.eval()
        dataiter = iter(self.train_loader)
        images, labels = dataiter.next()
        images = images[:num_images]

        fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
        for i in range(num_images):
            image = images[i].numpy().transpose((1, 2, 0))
            image = np.clip(image * 0.229 + 0.485, 0, 1)
            axes[i].imshow(image)
            axes[i].axis('off')
        plt.show()

    def visualize_heatmaps(self, num_images=5):
        self.model.eval()
        dataiter = iter(self.test_loader)
        images, labels = dataiter.next()
        images, labels = images[:num_images], labels[:num_images]

        ig = IntegratedGradients(self.model)
        attributions = ig.attribute(images.to(self.device), target=labels.to(self.device))

        for i in range(num_images):
            _ = viz.visualize_image_attr_multiple(
                np.transpose(attributions[i].cpu().detach().numpy(), (1, 2, 0)),
                np.transpose(images[i].cpu().detach().numpy(), (1, 2, 0)),
                ["original_image", "heat_map"],
            )

# Example usage
dataset_path = '/path/to/dataset'
hyparams = {
    'batch_size': 64,
    'learning_rate': 0.001
}

model_instance = Model(
    model_name='vgg16',
    n_classes=3,
    train=True,
    pretrain_imagenet=True,
    fine_tuning=False,
    dataset_path=dataset_path,
    hyparams=hyparams
)

# Train the model
model_instance.train_model(num_epochs=10)

# Test the model
model_instance.test_model()

# Visualize augmentations
model_instance.visualize_augmentations(num_images=5)

# Visualize heatmaps
model_instance.visualize_heatmaps(num_images=5)

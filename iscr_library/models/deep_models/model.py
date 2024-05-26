from torchvision import models
import torch.nn as nn
import torch

class Model:
    def __init__(self, model_name, n_classes, train_on_gpu):
        if model_name == 'vgg16':
            self.model = models.vgg16(pretrained=True)

            # Freeze early layers
            for param in self.model.parameters():
                param.requires_grad = False
            n_inputs = self.model.classifier[6].in_features

            # Add on classifier
            self.model.classifier[6] = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, n_classes), nn.LogSoftmax(dim=1))

        elif model_name == 'resnet50':
            self.model = models.resnet50(pretrained=True)

            # Freeze early layers
            for param in self.model.parameters():
                param.requires_grad = False
            n_inputs = self.model.fc.in_features

            # Add on classifier
            self.model.fc = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, n_classes), nn.LogSoftmax(dim=1))

        elif model_name == 'googlenet':
            self.model = models.googlenet(pretrained=True)

            # Freeze early layers
            for param in self.model.parameters():
                param.requires_grad = False
            n_inputs = self.model.fc.in_features

            # Add on classifier
            self.model.fc = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, n_classes), nn.LogSoftmax(dim=1))

        # Specify the device
        self.device = torch.device('cuda' if train_on_gpu and torch.cuda.is_available() else 'cpu')
        
        # Move to the specified device
        self.model = self.model.to(self.device)

# Example usage
# model_instance = Model('vgg16', 10, train_on_gpu=True)
# or
# model_instance = Model('resnet50', 10, train_on_gpu=True)
# or
# model_instance = Model('googlenet', 10, train_on_gpu=True)

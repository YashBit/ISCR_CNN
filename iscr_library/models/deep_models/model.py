from torchvision import models
import torch.nn as nn
class Model:
    def __init__(self, model_name, n_classes, train_on_gpu):
        if model_name == 'vgg16':
            model = models.vgg16(pretrained=True)

            # Freeze early layers
            for param in model.parameters():
                param.requires_grad = False
            n_inputs = model.classifier[6].in_features

            # Add on classifier
            model.classifier[6] = nn.Sequential(
                nn.Linear(n_inputs, 256), nn.ReLU(), nn.Dropout(0.2),
                nn.Linear(256, n_classes), nn.LogSoftmax(dim=1))

        # Move to gpu and parallelize
        if train_on_gpu:
            model = model.to('cuda')

        return model
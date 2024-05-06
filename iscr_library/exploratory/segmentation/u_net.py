"""

    U NET IMPLEMENTATION THROUGH ABHISHEK THAKUR

"""

# IMPORT

import torch
import torch.nn as nn

def double_conv(in_c, out_c):
    conv = nn.Sequential(
        nn.Conv2d(in_c, out_c, kernel_size = 3),
        nn.ReLU(inplace = True),
        nn.Conv2d(out_c, out_c, kernel_size = 3),
        nn.ReLU(inplace = True)
    )

    return conv 

def crop_img(t1, target_tensor):
    target_size = target_tensor.size()[2]
    tensor_size = t1.size()[2]
    delta = tensor_size - target_tensor
    delta = delta // 2
    return t1[:, :, delta:tensor_size - delta]


class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.max_pool_2x2 = nn.MaxPool2d(kernel_size = 2, stride = 2)
        self.down_conv_1 = double_conv(1, 64)
        self.down_conv_2 = double_conv(64, 128)
        self.down_conv_3 = double_conv(128, 256)
        self.down_conv_4 = double_conv(256, 512)
        self.down_conv_5 = double_conv(512, 1024)
        self.up_trans_1 = nn.ConvTranspose2d(in_channels = 1024, 
                                             out_channels=512, 
                                             kernel_size=2, 
                                             stride=2)
        

    def forward(self, image):
        # Encoder 
        x1 = self.down_conv_1(image)
        print(x1.size())
        x2 = self.max_pool_2x2(x1)
        x3 = self.down_conv_2(x2)
        x4 = self.max_pool_2x2(x3)
        x5 = self.down_conv_3(x4)
        x6 = self.max_pool_2x2(x5)
        x7 = self.down_conv_4(x6)
        x8 = self.max_pool_2x2(x7)
        x9 = self.down_conv_5(x8)
        print(x9.size())

        # Decoder 
        x = self.up_trans_1(x9)
        print(x.size())
        print(x7.size())

   

if __name__ == "__main__":
    image = torch.rand((1, 1, 572, 527))
    model = UNet()
    model.forward(image)

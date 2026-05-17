# 依赖引入
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
import numpy as np
from torchvision import datasets, transforms

# 自定义dataset类
class MstCustomDataset(Dataset):
    def __init__(self, root, train=True, transform=None, target_transform=None):
        super().__init__()
        """
            root: 外部数据集所在目录
           train:,True表示训练集，False表示测试集
           transform：可选转换函数
        """
        self.root = root
        self.train = train
        self.transform = transform

        # 根据tranin加载数据集
        if train:
            self.images_file = os.path.join(root, 'train_images.npy')
            self.labels_file = os.path.join(root, 'train_label.npy')
        else:
            self.images_file = os.path.join(root, 'test_images.npy')
            self.labels_file = os.path.join(root, 'test_label.npy')

        self.images = np.load(self.images_file)
        self.labels = np.load(self.labels_file)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        image = self.images[index]
        label = self.labels[index]

        image = Image.fromarray(image.astype('uint8'), mode='L')

        # 转换
        if self.transform:
            image = self.transform(image)

        return image,label
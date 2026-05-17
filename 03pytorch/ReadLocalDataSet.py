# 依赖引入
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
import numpy as np
from torchvision import datasets, transforms
import pandas as pd


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

        return image, label


class CustomMNISTImageDataset(Dataset):
    def __init__(self, root, train=True, transform=None,):
        self.root_dir = root
        self.train = train
        self.transform = transform

        # 数据目录和标签文件
        if train:
            self.data_dir = os.path.join(root, 'train')
            self.label_dir = os.path.join(root, 'train.csv')
        else:
            self.data_dir = os.path.join(root, 'test')
            self.label_dir = os.path.join(root, 'test.csv')

        # 读取为dataframe
        self.labels_df = pd.read_csv(self.label_dir)

    def __len__(self):
        return len(self.labels_df)

    def __getitem__(self, index):
        # 后续使用self.data[ids]索引一个python列表会报错，原生python列表不支持tensor作为索引
        # 做数据类型安全转换，确保ids是python原生数据类型
        if torch.is_tensor(index):
            index = index.tolist()

        # 获取文件名和标签
        row = self.labels_df.iloc[index]
        filename, label = row['filename'], row['label']

        # 构建完整路径 、 加载图像
        img_path = os.path.join(self.data_dir, filename)
        image = Image.open(img_path).convert('L') # 转为灰度图像

        # 转换
        if self.transform:
            image = self.transform(image)

        return image, label
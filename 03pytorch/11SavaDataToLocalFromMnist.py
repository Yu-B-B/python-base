# 保存MNIST数据到本地

import numpy as np
import os
import torch
from torchvision import datasets, transforms
from PIL import Image
import pandas as pd


# 定义目录结构
def create_directory_structure():
    base_dir = './mnist_images'
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'test'), exist_ok=True)

    # 为每个数字（类别）创建目录
    for i in range(10):
        os.makedirs(os.path.join(base_dir, 'train', str(i)), exist_ok=True)
        os.makedirs(os.path.join(base_dir, 'test', str(i)), exist_ok=True)

    return base_dir


# 保存数据为图像文件
def save_mnist_images():
    base_dir = create_directory_structure()

    # 定义转换和加载数据集
    transform = transforms.ToTensor()
    train_dataset = datasets.MNIST('./mnist_images', train=True, transform=transform, download=True)
    test_dataset = datasets.MNIST('./mnist_images', train=False, transform=transform, download=True)

    # 保存训练数据
    print(f'开始保存训练数据')
    train_labels = []
    test_labels = []
    for i, (image, label) in enumerate(train_dataset):
        # 转换数据格式
        image_pil = transforms.ToPILImage()(image)

        # 保存图像到对应类别文件夹
        # 1、给定图像保存路径,全是文件夹的各级名称
        image_path = os.path.join(base_dir, 'train', str(label), f'{i:05d}.png')
        image_pil.save(image_path)
        # 记录文件名和标签
        train_labels.append([f'{label}/{i:05d}.png', label])
        if (i + 1) % 10000 == 0:
            print(f'已保存{i + 1}张训练图像')

    for i, (image, label) in enumerate(test_dataset):
        # 转换数据格式
        image_pil = transforms.ToPILImage()(image)

        # 保存图像到对应类别文件夹
        # 1、给定图像保存路径,全是文件夹的各级名称
        image_path = os.path.join(base_dir, 'test', str(label), f'{i:05d}.png')
        image_pil.save(image_path)
        # 记录文件名和标签
        test_labels.append([f'{label}/{i:05d}.png', label])
        if (i + 1) % 1000 == 0:
            print(f'已保存{i + 1}张测试图像')

    # 保存标签信息到csv文件
    train_labels_df = pd.DataFrame(train_labels, columns=['filename', 'label'])
    test_labels_df = pd.DataFrame(test_labels, columns=['filename', 'label'])
    # 使用pandas将label保存为其他格式
    train_labels_df.to_csv(os.path.join(base_dir, 'train.csv'), index=False)
    test_labels_df.to_csv(os.path.join(base_dir, 'test.csv'), index=False)

    print(f'数据已经保存到：{base_dir}')
    print(f'训练样本数：{len(train_labels)}')
    print(f'测试样本数：{len(test_labels)}')


save_mnist_images()

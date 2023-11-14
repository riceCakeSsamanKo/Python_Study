import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import variable
import torch.nn.functional as F

import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 데이터 셋 다운로드
train_dataset = torchvision.datasets.FashionMNIST("/Users/jeonmin/Documents/study/080289/chap05/data", download=True,
                                                  transform=transforms.Compose([transforms.ToTensor()]))
test_dataset = torchvision.datasets.FashionMNIST("/Users/jeonmin/Documents/study/080289/chap05/data", download=True,
                                                 train=False, transform=transforms.Compose([transforms.ToTensor()]))

# DataLoader()를 사용해서 원하는 크기의 배치 단위로 데이터를 불러옴.
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=100)  # train_dataset에서 100개 단위로 데이터를 묶어서 불러온다.
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=100)

labels_map = {0: 'T-shirt', 1: "Trouser", 2: "Pullover",
              3: "Dress", 4: "Coat", 5: "Sandal",
              6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle Boot"}  # 이미지 레이블 클래스

fig = plt.figure(figsize=(8, 8))  # 출력할 이미지의 가로 세로 길이. (단위 inch)
columns = 4
rows = 5
for i in range(1, columns * rows + 1):
    img_xy = np.random.randint(len(train_dataset))  # train_dataset의 길이에서 임의의 랜덤한 숫자 생성
    img = train_dataset[img_xy][0][0, :, :]
    fig.add_subplot(rows, columns, i)
    plt.title(labels_map[train_dataset[img_xy][1]])
    plt.axis("off")
    plt.imshow(img, cmap='gray')
plt.show()


class FashionDNN(nn.Module):
    def __init__(self):
        super(FashionDNN, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=256)
        self.drop = nn.Dropout(0.25)  # 파라미터 비율만큼 텐서의 값이 0이된다. 0이 되지 않는 값들은 기존 값에 (1/(1-p))만큼 곱해져 커진다.
        self.fc2 = nn.Linear(in_features=256, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=10)

    # 순전파 메서드
    def forward(self, input_data):
        out = input_data.view(-1, 784)  # 넘파이의 reshape. input_data의 크기를 (?, 784)로 변경하라. -1은 파이토치에게 알아서 차원을 맞추라는 의미
        out = F.relu(self.fc1(out)) # 은닉층 1
        out = self.drop(out)  # 과 최적화 방지를 위한 drop out(25%)
        out = F.relu(self.fc2(out))  # 은닉층 2
        out = F.relu(self.fc3(out))  # 은닉층 3
        return out


dnn = FashionDNN()
dnn.forward(train_da)

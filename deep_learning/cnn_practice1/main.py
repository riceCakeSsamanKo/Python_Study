import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# 데이터 셋 다운로드
root = "E:/study/Python-Practice/deep_learning/learning_data"
train_dataset = torchvision.datasets.FashionMNIST(root, download=True,
                                                  transform=transforms.Compose([transforms.ToTensor()]))
test_dataset = torchvision.datasets.FashionMNIST(root, download=True,
                                                 train=False, transform=transforms.Compose([transforms.ToTensor()]))

# DataLoader()를 사용해서 원하는 크기의 배치 단위로 데이터를 불러옴.
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=100)  # train_dataset에서 100개 단위로 데이터를 묶어서 불러온다.
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=100)

labels_map = {0: 'T-Shirt', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat', 5: 'Sandal', 6: 'Shirt',
              7: 'Sneaker', 8: 'Bag', 9: 'Ankle Boot'}

fig = plt.figure(figsize=(8, 8))
columns = 4
rows = 5
for i in range(1, columns * rows + 1):
    img_xy = np.random.randint(len(train_dataset));
    img = train_dataset[img_xy][0][0, :, :]
    fig.add_subplot(rows, columns, i)
    plt.title(labels_map[train_dataset[img_xy][1]])
    plt.axis('off')
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
        out = F.relu(self.fc1(out))  # 은닉층 1
        out = self.drop(out)  # 과 최적화 방지를 위한 drop out(25%)
        out = F.relu(self.fc2(out))  # 은닉층 2
        out = F.relu(self.fc3(out))  # 은닉층 3
        return out


learning_rate = 0.001
model = FashionDNN()
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
print(model)

'''cnn을 이용한 모델 학습'''
num_epochs = 5
count = 0
loss_list = []
iteration_list = []
accuracy_list = []

predictions_list = []
labels_list = []

for epoch in range(num_epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        train = Variable(images.view(100, 1, 28, 28))
        labels = Variable(labels)

        outputs = model(train)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        count += 1

        if not (count % 50):
            total = 0
            correct = 0
            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)
                labels_list.append(labels)
                test = torch.autograd.Variable(images.view(100, 1, 28, 28))
                outputs = model(test)
                predictions = torch.max(outputs, 1)[1].to(device)
                predictions_list.append(predictions)
                correct += (predictions == labels).sum()
                total += len(labels)

            accuracy = correct * 100 / total
            loss_list.append(loss.data)
            iteration_list.append(count)
            accuracy_list.append(accuracy)

        if not (count % 500):
            print("Iteration: {}, Loss: {}, Accuracy: {}%".format(count, loss.data, accuracy))

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
print(device)  # gpu가 있다면 gpu에서 없다면 cpu에서 처리함

root = "E:/study/Python_Study/deep_learning/learning_data"

# train_dataset[a] = (pixels, label)
train_dataset = torchvision.datasets.MNIST(root=root, train=True, download=True,
                                           transform=transforms.Compose([transforms.ToTensor()]))
test_dataset = torchvision.datasets.MNIST(root=root, train=False, download=True,
                                          transform=transforms.Compose([transforms.ToTensor()]))

# DataLoader()를 사용해서 원하는 크기의 배치 단위로 데이터를 불러옴.(100개씩)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=100)  # train_dataset에서 100개 단위로 데이터를 묶어서 불러온다.
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=100)


# 랜덤 데이터 출력
def show_random_datas():
    fig = plt.figure(figsize=(8, 8))
    columns = 4
    rows = 5
    for i in range(1, columns * rows + 1):
        img_xy = np.random.randint(len(train_dataset))
        img = train_dataset[img_xy][0][0, :, :]
        fig.add_subplot(rows, columns, i)
        plt.title(train_dataset[img_xy][1])
        plt.axis('off')
        plt.imshow(img, cmap='gray')
    plt.show()

# show_random_datas()


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        # hidden_layer1 (data size: 32x14x14)
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        # hidden_layer2 (data size: 64x6x6)
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        # hidden_layer3 (data size: 128x2x2)
        self.layer3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer1_feature_size = 32 * 14 * 14
        self.layer2_feature_size = 64 * 6 * 6
        self.layer3_feature_size = 128 * 2 * 2

        self.fc1 = nn.Linear(in_features=self.layer2_feature_size, out_features=600)
        self.drop = nn.Dropout(0.25)
        self.fc2 = nn.Linear(in_features=600, out_features=120)
        self.fc3 = nn.Linear(in_features=120, out_features=10)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        # out = self.layer3(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.drop(out)
        out = self.fc2(out)
        out = self.fc3(out)

        return out


model = CNN()
model.to(device)
print(model)

learning_rate = 0.001

'''loss 함수'''
criterion = nn.CrossEntropyLoss()

'''optimization 함수'''
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
# optimizer = torch.optim.Adagrad(model.parameters(), lr=learning_rate)
# optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

num_epochs = 3
count = 0
loss_list = []
iteration_list = []
accuracy_list = []

predictions_list = []
labels_list = []

for epoch in range(num_epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        train = images.view(100, 1, 28, 28)

        outputs = model(train)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()

        # 역전파 적용
        loss.backward()
        # 파라미터 갱신
        optimizer.step()
        count += 1

        if not (count % 5):
            total = 0
            correct = 0

            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)
                labels_list.append(labels)
                test = images.view(100, 1, 28, 28)

                # model을 통해서 얻은 결과 값
                outputs = model(test)

                # label에 대한 추정값
                predictions = torch.max(outputs, 1)[1].to(device)
                predictions_list.append(predictions)

                # 만일 정답이라면 correct를 증가해줌
                correct += (predictions == labels).sum()
                total += len(labels)

            # 정확도
            accuracy = correct * 100 / total

            loss_list.append(loss.item())
            iteration_list.append(count)
            accuracy_list.append(accuracy.item())

        # iterantion에 따른 loss와 accuracy 출력
        if not (count % 100):
            print("Iteration: {}, Loss: {}, Accuracy: {}%".format(count, loss.data, accuracy))

# 학습 결과 그래프 출력
fig, ax1 = plt.subplots(figsize=(8, 6))

ax1.set_xlabel('Iterations')
ax1.set_ylabel('Accuracy', color='blue')
line1 = ax1.plot(iteration_list, accuracy_list, label='Accuracy', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Loss', color='red')
line2 = ax2.plot(iteration_list, loss_list, label='Loss', color='red')
ax2.tick_params(axis='y', labelcolor='red')

lines = line1 + line2
labels = [l.get_label() for l in lines]
plt.title('Result')

plt.legend(lines, labels, loc='best')
plt.grid(True)
plt.show()
plt.show()

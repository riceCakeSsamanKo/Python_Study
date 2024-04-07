import numpy as np
import matplotlib.pyplot as plt

X = np.array([1.74, 1.52, 1.38, 1.28, 1.86])
y = np.array([71, 55, 46, 38, 88])

W = 0
b = 0

lr = 0.01
epochs = 10000

n = float(len(X))  # num of data

# Gradient Descent
for i in range(epochs):
    y_pred = W * X + b  # f(x)

    dW = (2 / n) * np.sum(X * (y_pred - y))
    db = (2 / n) * np.sum(y_pred - y)

    W = W - lr * dW
    b = b - lr * db

# 계산된 Weight(slope)와 b(bias) 출력
print(f"W= {W}, b= {b}")

# 선형 회귀로 찾아낸 선형 그래프
y_pred = W * X + b

plt.scatter(X, y)
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')
plt.show()

import matplotlib.pylab as plt
from sklearn import linear_model

# Generate a linear regression model.
reg = linear_model.LinearRegression()
# The data can be made as a list in Python or as an array in Numpy.
X = [[0], [1], [2]]  # Must be made in 2D
y = [3, 3.5, 5.5]  # y = x + 3
# Train
reg.fit(X, y)

# reg.coef_  # the slope
# array([1.25])
# reg.intercept_  # the bias
# 2.7500000000000004
# reg.score(X, y)
# 0.8928571428571429
# reg.predict([[5]])
# array([8.])

# Draw the training data and the y value as a scatter plot.
plt.scatter(X, y, color='black')
# Calculate the prediction value using the training data as input.
y_pred = reg.predict(X)
# Draw a graph with the training data and the prediction value.
# A straight line with a calculated slope and bias is drawn.
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()

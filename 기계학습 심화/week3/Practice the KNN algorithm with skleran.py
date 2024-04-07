from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
print(iris.data[:5])

print(iris.feature_names) # features
print(iris.target) # label

X = iris.data
y = iris.target

# Divide into 8:2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

print(X_train.shape) # 120 x 4
print(X_test.shape) # 30 x 4

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test, y_pred)
print(scores)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# 0 = setosa, 1 = versicolor, 2 = virginica
classes = {0: "setosa", 1: "versicolor", 2: "virginica"}

# Lets's present new data that we haven't seen yet.
# 임의로 생성한 두개의 꽃 데이터
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X_new = [[3, 4, 5, 2],
         [5, 4, 2, 2]]
y_predict = knn.predict(X_new)

# predicted label
print(y_predict[0]) # 1 : versicolor
print(y_predict[1]) # 0 : setosa

import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs
import numpy as np

# we create 40 separation point
X, y = make_blobs(n_samples=400, centers=2, random_state=6)

# fit the model, don't regularize for illustration purpose
clf = svm.SVC(kernel='linear', C=1000)  # 그냥 sklearn의 svm 메서드로 쉽게 svm을 사용할 수 있다.
clf.fit(X, y)


# Function to display SVM result
def show_plt(x, y, svm1, title):
    plt.scatter(x[:, 0],x[:,1], c=y, s=30, cmap=plt.cm.Paired)

    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = svm1.decision_function(xy).reshape(XX.shape)

    # margins decision boundary
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

    # Support vector
    ax.scatter(svm1.support_vectors_[:, 0], svm1.support_vectors_[:, 1], s=60, facecolors='r')
    plt.title(title)
    plt.show()

show_plt(X,y,clf,"SVM Classification Result")
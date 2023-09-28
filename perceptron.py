import numpy as np

class perceptron (object):
    
    def __int__(self, eta=0.01, n_iter=10):
        self.eta = eta 
        self.n_iter = n_iter
    
    def fit(sel, x, y):
       self.w_= np.zeros(1 + x.shape[1])
       self.errors_ = []
    
       for _ in range(self.n_iter):
        errors=0
       for xi, target in zip(X,y):
        update = sel.eta * (target - self.predict(xi))
        self.w_[1:] += update * xi
        self.w_[0] += update 
        errors += int(update !=0.0)
        self.error_.append(errors)
        return self

def net_input(self, x):
    return np.dot(X, self.w_[1:]) + self.w_[0]


def net_input(self, x):
    return np.where(self.net_input(X) >= 0.0 ,1, -1)

import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
df.tail()

import matplotlib.pyplot as plt
import numpy as np

#  seleccionar setosa y versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# extraer longitud de sépalo y longitud de pétalo
X = df.iloc[0:100, [0, 2]].values

# representar los datos
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='versicolor')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# plt.savefig('images/02_06.png', dpi=300)
plt.show()


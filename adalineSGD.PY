from numpy.random import seed
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class AdalineSGD(object):

    def __init__ (self, eta=0.01, n_iter=50, random_state=1):
        self.eta=eta
        self.n_iter=n_iter
        self.w_inicialized = False
        self.random_state=random_state
        if random_state:
            seed(random_state)

    def _inicialize_weigths(self,m):
        self.w=np.zeros(m + 1) 
        self.w_inicialized =True

    def update_weights(self, xi, target):
        output = self.net_input(xi)
        eror= target - output
        self.w_[0]+= self.eta * xi.dot(error)
        self.w_[1:]+= self.eta * error 
        cost = 0.5 * error ** 2
        return cost

    def _shuffle(self, X, y):
        seq = np.random.permutation(len(y))
        return X[seq], y[seq]
    
    def fit (self, X, y):
        self.w_inicialize_weigths(X.shape[1])
        self.cost_ = []

        for i in range (self.n_iter):
            if self._shuffle:
                X, y =self._shuffle(X,y)
            cost = []
            for xi, target in zip(X,y):
                cost.append(self._update_weights(xi, target))
            avg_cost= sum(cost)/len(y)
        return self
    
    def partial_fit(self, X, y):
        if not self.w_inicialized:
            self._inicialize_weigths(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X,y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X,y)
        return self
    
    def net_input(self,X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        return X
    
    def predict (self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1 ,-1)
    

   


        
                


import numpy as np


class Perceptron:
    '''Perceptron classifier

    Parameters
    __________
    eta : float
        learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.
    random_state: int
        Random number generator seed for random weight
        initialization

    Attributes
    __________
    w_ : 1d_array
        Weights after fitting
    b_ : Scaler
        Bias unit after fitting

    errors_ : list
        Number of misclassifications (updates) in each epoch
    '''

    def __init__(self, eta=0.01, n_iter=50, random_state=1) -> None:
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        '''Fit training data.

        Parameters
        __________
        X : {array-like}, shape = [n_example, n_features]
            Training vectors, where n_example is the number of 
            example and n_features is the number of features.
        y : array-like, shape = [n_examples]
            Target values

        Returns
        _______
        self : object

        '''
        # Initial weight vector contains small random numbers drawn from
        # normal distribution std 0.01
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,
                              size=X.shape[1])
        self.b_ = np.float_(0.)
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        '''Calculate net input'''
        return np.dot(X, self.w_) + self.b_

    def predict(self, X):
        '''Return class label after unit step'''
        return np.where(self.net_input(X) >= 0.0, 1, 0)


class AdalineGD:
    '''ADAptive linear NEuron classifier

    Parameters
    __________
    eta : float
        learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.
    random_state: int
        Random number generator seed for random weight
        initialization

    Attributes
    __________
    w_ : 1d_array
        Weights after fitting
    b_ : Scaler
        Bias unit after fitting
    losses_: list
        Mean squared error loss function values in each epoch.
    '''
    def __init__(self, eta=0.01, n_iter=50, random_state=1) -> None:
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        '''Fit training data.

        Parameters
        __________
        X : {array-like}, shape = [n_example, n_features]
            Training vectors, where n_example is the number of 
            example and n_features is the number of features.
        y : array-like, shape = [n_examples]
            Target values

        Returns
        _______
        self : object

        '''
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01,
                              size=X.shape[1])
        self.b_ = np.float_(0.)
        self.losses_ = []

        for _ in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_ += self.eta * 2.0 * X.T.dot(errors)/ X.shape[0]
            self.b_ += self.eta * 2.0 * errors.mean()
            loss = (errors**2).mean()
            self.losses_.append(loss)
        return self

    def net_input(self, X):
        '''Calculate net input'''
        return np.dot(X, self.w_) + self.b_

    def activation(self, X):
        '''Compute linear activation'''
        return X

    def predict(self, X):
        '''Return label after unit step'''
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0 )

import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


class Network:
    def __init__(self, sizes):
        self.layer_num = len(sizes)
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(a, b)
                        for a, b in zip(sizes[1:], sizes[:-1])]

    def forward(self, a):

        for w, b in zip(self.weights, self.biases):
            a = sigmoid(np.dot(w, a) + b)

        return a

    def SGC(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)
            ]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1}/ {2}".format(j,
                                                   self.evaluate(test_data), n_test))
            else:
                print("Epoch {} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np]

import math

sig = lambda x: 1 / (1 + math.pow(math.e, -x))

weights = [0.5, -0.3, -0.04, 0.2, 0.06, -0.15]
i1 = 1
i2 = 0.5
actual = 1

def forward(w, i1, i2):
    """
    :param w: list, the weights for the NN
    :param i1: float, the first input
    :param i2: float, the second input
    :return: float, o1
    :return: float, h1
    :return: float, h2
    :return: float, b1
    """
    h1 = w[0] * i1 + w[1] * i2
    h2 = w[2] * i1 + w[3] + i2

    b1 = sig(h1) * w[4] + sig(h2) * w[5]

    return sig(b1), h1, h2, b1

def backward(w, i1, i2, actual, o1, h1, h2, b1, alpha):
    """
        :param w: float, the first input
        :param i1: float, the second input
        :param i2: float, the actual value
        :param actual: float, what the NN predicted
        :param o1: float, h1
        :param h1: float, h2
        :param h2: float, b1
        :param alpha: float, the learning rate
        :return: list of floats, the updated weights
        """
    delta = o1 - actual
    w[5] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h2) * delta
    w[4] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h1) * delta
    w[3] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h2) * (1 - sig(h2)) * i2 * w[5] * delta
    w[2] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h2) * (1 - sig(h2)) * i1 * w[5] * delta
    w[1] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h1) * (1 - sig(h1)) * i2 * w[4] * delta
    w[0] -= alpha * sig(b1) * (1 - sig(b1)) * sig(h1) * (1 - sig(h1)) * i1 * w[4] * delta
    return w

for i in range(100000):
    o1, h1, h2, b1 = forward(weights, i1, i2)
    print("for the %i epoch, the prediction is %f"  % (i, o1))
    weights = backward(weights, i1, i2, actual, o1, h1, h2, b1, 0.1)




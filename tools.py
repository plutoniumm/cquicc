import numpy as np
from math import isnan
from numpy import format_float_positional, abs as np_abs, array, uint8, float32, mean, unpackbits, random
from torch import sum, norm, sqrt, abs
from qiskit.circuit.random import random_circuit


def getRandCircuit(n):
    return random_circuit(
        n,
        random.randint(0, n*8),
        measure=True
    ).decompose(reps=1)


def getBitwise(memory, size):
    memory = array([int(str(bit), size) for bit in memory], dtype=uint8)

    memory = mean(
        array(
            [unpackbits(bit) for bit in memory]
        ), axis=0).astype(float32)

    return memory

def fmt(x):
    return format_float_positional(x, precision=4)
    # test


def rtol(a, b):
    return np_abs((b/a)-1) < 0.005


def get(tens):
    return [fmt(x) for x in tens.detach().numpy()[0]]


def distance(x, y):
    # compute the inner products for the batch of vectors
    inner_prod = sum(x * y, dim=1)
    # compute the norms for the batch of vectors
    norm_x = norm(x, dim=1)
    norm_y = norm(y, dim=1)

    # compute the distances for the batch of vectors
    distance = sqrt(norm_x**2 - 2*inner_prod + norm_y**2)
    return 0.0001 if distance == 0 else distance


def my_loss(pred, ideal, noisy):
    return abs(distance(pred, ideal) / distance(noisy, ideal))


def PCTLoss(x, scale=1):
    if (isnan(x)):
        return 100
    else:
        if (scale == 1):
            return int(x * 100 / 8)
        else:
            return float(int(x * scale * 100 / 8)) / scale

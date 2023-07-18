from qiskit import QuantumCircuit
from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit_machine_learning.neural_networks import EstimatorQNN

import torch
import torch.nn as nn
import torch.nn.functional as F

def create_qnn():
    feature_map = ZZFeatureMap(9)
    ansatz = RealAmplitudes(9, reps=1)
    qc = QuantumCircuit(9)
    qc.compose(feature_map, inplace=True)
    qc.compose(ansatz, inplace=True)

    print(qc)

    # REMEMBER TO SET input_gradients=True FOR ENABLING HYBRID GRADIENT BACKPROP
    qnn = EstimatorQNN(
        circuit=qc,
        input_params=feature_map.parameters,
        weight_params=ansatz.parameters,
        input_gradients=True,
    )
    return qnn


# qnn4 = create_qnn()

class MyConv2d(nn.Module):
    def __init__(self, n_channels, out_channels, kernel_size, dilation=1, padding=0, stride=1):
        super(MyConv2d, self).__init__()

        self.kernel_size = (kernel_size, kernel_size)
        self.kernal_size_number = kernel_size * kernel_size
        self.out_channels = out_channels
        self.dilation = (dilation, dilation)
        self.padding = (padding, padding)
        self.stride = (stride, stride)
        self.n_channels = n_channels
        self.weights = nn.Parameter(torch.Tensor(self.out_channels, self.n_channels, self.kernal_size_number))

    def forward(self, x):
        width = self.calculateNewWidth(x)
        height = self.calculateNewHeight(x)
        windows = self.calculateWindows(x)

        result = torch.zeros(
            [x.shape[0] * self.out_channels, width, height], dtype=torch.float32, device=device
        )

        for channel in range(x.shape[1]):
            for i_convNumber in range(self.out_channels):
                xx = torch.matmul(windows[channel], self.weights[i_convNumber][channel])
                xx = xx.view(-1, width, height)
                result[i_convNumber * xx.shape[0] : (i_convNumber + 1) * xx.shape[0]] += xx

        result = result.view(x.shape[0], self.out_channels, width, height)
        return result

    def calculateWindows(self, x):
        windows = F.unfold(
            x, kernel_size=self.kernel_size, padding=self.padding, dilation=self.dilation, stride=self.stride
        )

        windows = windows.transpose(1, 2).contiguous().view(-1, x.shape[1], self.kernal_size_number)
        windows = windows.transpose(0, 1)

        return windows

    def calculateNewWidth(self, x):
        return (
            (x.shape[2] + 2 * self.padding[0] - self.dilation[0] * (self.kernel_size[0] - 1) - 1)
            // self.stride[0]
        ) + 1

    def calculateNewHeight(self, x):
        return (
            (x.shape[3] + 2 * self.padding[1] - self.dilation[1] * (self.kernel_size[1] - 1) - 1)
            // self.stride[1]
        ) + 1

device = 'cpu'
conv = MyConv2d(3, 1, 3)
x = torch.randn(1, 3, 24, 24)
out = conv(x)
out.mean().backward()
print(conv.weights.grad)
from qiskit import QuantumCircuit
from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit_machine_learning.neural_networks import EstimatorQNN

from torch.nn.functional import unfold
from torch.nn import Parameter, Module
from torch import matmul, Tensor, randn, zeros, float32

class Quanv(Module):
    def __init__(self, in_chan, out_chan, kernel_size=3):
        super(Quanv, self).__init__()

        self.kernel_size = (kernel_size, kernel_size)
        self.kernal_size_number = kernel_size * kernel_size
        self.out_chan = out_chan
        self.in_chan = in_chan
        self.weights = Parameter(Tensor(
            self.out_chan, self.in_chan, self.kernal_size_number
        ))

    def forward(self, x):

        return 1

# print("Testing Quanv")
# conv = Quanv(3, 1, 3)
# x = randn(1, 3, 24, 24)
# out = conv(x)
# out.mean().backward()
# print(conv.weights.grad)
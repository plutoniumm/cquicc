from qiskit import QuantumCircuit
from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit_machine_learning.neural_networks import EstimatorQNN

from torch.nn.functional import unfold
from torch.nn import Parameter, Module
from torch import matmul, Tensor, randn, zeros, float32

# def create_qnn():
#     feature_map = ZZFeatureMap(9)
#     ansatz = RealAmplitudes(9, reps=1)
#     qc = QuantumCircuit(9)
#     qc.compose(feature_map, inplace=True)
#     qc.compose(ansatz, inplace=True)

#     print(qc)

#     qnn = EstimatorQNN(
#         circuit=qc,
#         input_params=feature_map.parameters,
#         weight_params=ansatz.parameters,
#         input_gradients=True,
#     )
#     return qnn

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
        width = self.calculateNewWidth(x)
        height = self.calculateNewHeight(x)
        windows = self.calculateWindows(x)

        result = zeros([
            x.shape[0] * self.out_chan, width, height
        ], dtype=float32)

        for channel in range(x.shape[1]):
            for i_convNumber in range(self.out_chan):
                xx = matmul(
                    windows[channel], self.weights[i_convNumber][channel]
                )
                xx = xx.view(-1, width, height)
                result[
                    i_convNumber * xx.shape[0] :
                        (i_convNumber + 1) * xx.shape[0]
                ] += xx

        return result.view(x.shape[0], self.out_chan, width, height)

    def calculateWindows(self, x):
        windows = unfold(x, kernel_size=self.kernel_size)
        windows = windows.transpose(1, 2).contiguous().view(
            -1, x.shape[1], self.kernal_size_number
        )

        return windows.transpose(0, 1)

    def calculateNewWidth(self, x):
        return ((x.shape[2] - self.kernel_size[0]) // 1) + 1

    def calculateNewHeight(self, x):
        return ((x.shape[3] - self.kernel_size[1]) // 1) + 1

# print("Testing Quanv")
# conv = Quanv(3, 1, 3)
# x = randn(1, 3, 24, 24)
# out = conv(x)
# out.mean().backward()
# print(conv.weights.grad)
from torch.nn import (
    Linear,
    Sequential,
    Module,
    ReLU
)
from torch import cat


class AutoDenoiser(Module):
    def __init__(self):
        super(AutoDenoiser, self).__init__()
        self.encoder = Sequential(
            # 8 quasi probabilities + 1 value for qubit count
            Linear(9, 8),
            ReLU(),
            Linear(8, 8),
            ReLU(),
            Linear(8, 6),
            ReLU(),
            Linear(6, 4),
            ReLU(),
        )
        self.decoder = Sequential(
            Linear(4, 6),
            ReLU(),
            Linear(6, 8),
            ReLU(),
            Linear(8, 8)  # Last relu is redundant
        )

    def forward(self, x, qubits):
        # x_in will be 8
        x = self.encoder(
            cat([
                x,
                qubits.view(-1, 1)
            ], dim=1)
        )
        return self.decoder(x)

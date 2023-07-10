from numpy import array, float32
import pandas as pd
from torch import tensor
from torch.utils.data import Dataset


def parseRow(x):
    return array([
        float32(element) for element in x.strip()[1:-1].split(",")
    ]).astype(float32)


class QDataSet(Dataset):
    def __init__(self, csv_path):
        super().__init__()
        self.csv_path = csv_path
        self.load_data()

    def load_data(self):
        df = pd.read_csv(self.csv_path)

        ideal_rows = df["ideal"].apply(parseRow)
        noisy_rows = df["noisy"].apply(parseRow)

        self.qubits = tensor(df["qubits"].values)
        self.ideal = tensor(ideal_rows)
        self.noisy = tensor(noisy_rows)

    def __len__(self):
        return len(self.qubits)

    def __getitem__(self, idx):
        return {"qubits": self.qubits[idx],
                "ideal": self.ideal[idx],
                "noisy": self.noisy[idx]}

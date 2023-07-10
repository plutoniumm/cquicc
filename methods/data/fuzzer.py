import numpy as np
import warnings
import pandas as pd
from tqdm.auto import tqdm

def addNoise(value):
    pct = np.random.uniform(0.05, 1) / 100; # 0.05% to 1% noise
    stdv = np.abs(value * pct)
    return value + np.abs(np.random.normal(0, stdv)).astype(np.float32)


def fuzzIdeal(row, qubits):
    row = np.flip(row)
    new_row = [0.0001 for _ in range(len(row))]
    # we index in reverse
    for i in range(qubits):
        ele = row[i] # extracted because lists are pass by ref
        new_row[i] = addNoise(ele)

    new_row = np.array(np.flip(new_row)).astype(np.float32)
    print(new_row)
    return new_row.tolist()


CLEANED_PATH = "./pandad/cleaned1.csv"


def parseRow(x):
    return [
        float(element) for element in x.strip()[1:-1].split(",")
    ]

def getFile():
    df = pd.read_csv(CLEANED_PATH)
    # df["noisy"] = df["noisy"].apply(parseRow)
    print(f"Before converting to list {df.iloc[0]}")
    df["ideal"] = df["ideal"].apply(parseRow)

    return df

def convert_to_string(bs_list):
    if (type(bs_list) != float):
        return ("[" + (",".join([str(x) for x in bs_list])) + "]")

def to_csv(df):
    # df["noisy"] = df["noisy"].apply(convert_to_string)
    df["ideal"] = df["ideal"].apply(convert_to_string)
    df.to_csv("./pandad/fuzzy1.csv", index=False)


def run():
    df = getFile()
    df.dropna(inplace=True)
    appending_bs = []
    # print(f"After converting to list: {df.iloc[0]}")

    for i in tqdm(range(len(df))):
        ideal_row = df["ideal"].iloc[i]
        qubits = df["qubits"].iloc[i]
        noisy_row = df["noisy"].iloc[i]

        for _ in range(4):
            append_bs_bs = [qubits]

            row_list = list(fuzzIdeal(ideal_row, qubits))

            if (row_list == [0.0 for _ in range(8)]):
                print(row_list)

            append_bs_bs.append(row_list)
            append_bs_bs.append(noisy_row)

            appending_bs.append(append_bs_bs)


    df_to_append = pd.DataFrame(appending_bs, columns=df.columns)

    df = pd.concat([df, df_to_append], axis=0)
    print(len(df), len(df.iloc[0]))

    to_csv(df)
    return 0

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    run()
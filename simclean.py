import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from tools import fmt

CLEANED_PATH = f"./pandad/clean_sim.csv"
EPS = 0.0001

PATH = f"./data/sim_sim.csv"

if __name__ == "__main__":
    df_list = []
    counter = 0

    df_temp = pd.read_csv(PATH)

    df_temp.drop(labels=["index", "sys_noisy",
                  "sys_ideal"], inplace=True, axis=1)

    # for each row
    for i in tqdm(range(len(df_temp))):
        to_drop = [x.strip()
                    for x in df_temp["noisy"].iloc[i][1:-1].split(",")]

        qbits = df_temp["qubits"].iloc[i]
        rando = ["0.5" for _ in range(qbits)]

        # checks if all the qubits are perfectly random
        if (
            df_temp["noisy"].iloc[i] != df_temp["ideal"].iloc[i]
            and
            rando == to_drop[-qbits:]
        ):
            counter += 1
            continue

        ideal_stuff = [x.strip()
                        for x in df_temp["ideal"].iloc[i][1:-1].split(",")]

        # checks if ideals are all 0.0
        if (ideal_stuff == ["0.0" for _ in range(len(ideal_stuff))]):
            counter += 1
            continue

        # convert all 0.0000 to 0.0001 to avoid division by 0
        # this would be in both ideal and noisy
        converted_noisy = [float(x) for x in to_drop]
        converted_ideal = [float(x) for x in ideal_stuff]
        for n in range(len(converted_noisy)):
            if (converted_noisy[n] == 0. or str(converted_noisy[n]) == "0.0"):
                converted_noisy[n] += EPS
            if (converted_ideal[n] == 0. or str(converted_ideal[n]) == "0.0"):
                converted_ideal[n] += EPS

        # Convert them back to a string
        ideal_str = "[" + ",".join([fmt(x) for x in np.array(converted_ideal, dtype=np.float32)]) + "]"
        noisy_str = "[" + ",".join([fmt(x) for x in np.array(converted_noisy, dtype=np.float32)]) + "]"

        # construct the list
        l = df_temp.iloc[i]
        l["ideal"] = ideal_str
        l["noisy"] = noisy_str

        df_list.append(l.values.tolist())

    # Remove duplicate vectors (treating bitwise qubits as a dimension)
    df = pd.DataFrame(df_list, columns=df_temp.columns).drop_duplicates()
    df.to_csv(CLEANED_PATH, index=False)
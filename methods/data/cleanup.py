import pandas as pd
from tqdm.auto import tqdm

CLEANED_PATH = f"./pandad/cleaned1.csv"
EPS = 0.0001

def getFile(index):
    PATH = f"./data/set_{str(index)}.csv"
    return PATH


def run():
    df_list = []
    counter = 0

    for j in range(1,5): # reads set_1, set_2, set_3
        df_temp = pd.read_csv(getFile(j));
        print(f"RUNING ON {j}")
        df_temp.drop(labels=["index", "sys_noisy", "sys_ideal"], inplace=True, axis=1)
        print(f"Running on set {j}");

        # for each row
        for i in tqdm(range(len(df_temp))):
            to_drop = [x.strip() for x in df_temp["noisy"].iloc[i][1:-1].split(",")];

            # print(to_drop)

            items = df_temp["qubits"].iloc[i];

            rando = ["0.5" for _ in range(items)];

            if(i%25 == 0):
                print(f"Running on {i}th row");

            #checks if all the qubits are perfectly random
            if  (
                df_temp["noisy"].iloc[i] != df_temp["ideal"].iloc[i]
                and
                rando == to_drop[-items:]
            ):
                counter += 1
                continue;

            ideal_stuff = [x.strip() for x in df_temp["ideal"].iloc[i][1:-1].split(",")]

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
            ideal_str = "[" + ",".join([str(x) for x in converted_ideal]) + "]"
            noisy_str = "[" + ",".join([str(x) for x in converted_noisy]) + "]"

            # construct the list
            l = df_temp.iloc[i]
            l["ideal"] = ideal_str
            l["noisy"] = noisy_str

            df_list.append(l.values.tolist())

    # Remove duplicate vectors (treating bitwise qubits as a dimension)
    df = pd.DataFrame(df_list, columns=df_temp.columns).drop_duplicates()
    print(f"What remained = {len(df)}")
    df.to_csv(CLEANED_PATH, index=False);
    print(f"Dropped columns = {counter}")

if __name__ == "__main__":
    run()
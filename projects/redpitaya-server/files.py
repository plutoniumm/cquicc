import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

def process_xy(csv_str):
    csv_str = StringIO(csv_str)
    df = pd.read_csv(csv_str, sep=",", names=['x','y'])
    df = df.dropna()

    x = df['x'].to_numpy();
    y = df['y'].to_numpy();

    print(x,"\n",y)

    max_val = max(max(x), max(y))
    plt.xticks(range(0, max_val + 1))
    plt.yticks(range(0, max_val + 1))

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot')
    plt.grid(True)

    imgdata = StringIO()
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    svg_data = imgdata.getvalue()

    return svg_data
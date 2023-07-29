import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import StringIO, BytesIO

def process_xy(csv_str):
    csv_str = StringIO(csv_str)
    df = pd.read_csv(csv_str, sep=",", names=['x','y'])
    df = df.dropna()

    x = df['x'].to_numpy()[1:]
    y = df['y'].to_numpy()[1:]

    print(x,"\n",y)

    plt.plot(x, y)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    png = base64.b64encode(buffer.read()).decode()

    data_uri = 'data:image/png;base64,{}'.format(png)
    return data_uri
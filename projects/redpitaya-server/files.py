import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import StringIO, BytesIO

def process_xy(csv_str):
    csv_str = StringIO(csv_str)
    df = pd.read_csv(csv_str, sep=",", names=['x','y'])
    df = df.dropna()

    x = df['x'][1:].astype(float)
    y = df['y'][1:].astype(float)

    print(x,"\n",y)

    plt.plot(x, y)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot: Iteration 5')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    png = base64.b64encode(buffer.read()).decode()

    data_uri = 'data:image/png;base64,{}'.format(png)
    return data_uri

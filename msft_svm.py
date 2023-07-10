# https://github.com/microsoft/ML-For-Beginners/blob/main/7-TimeSeries/3-SVR/README.md
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from lib.utils import log, report, warn

WINDOW = 5 # moving window size
TIME_SCALE = "H" # time scale of data
TIME_COL = "timestamp" # name of col w/ timestamps
DATA_FILE = "data/energy.csv" # path to data file
plot_tests = False # plot test/train data

def getData(file):
  df = pd.read_csv(file, parse_dates=[TIME_COL])
  df.index = df[TIME_COL]

  # reindex
  df = df.reindex(pd.date_range(
    min(df.index), max(df.index), freq=TIME_SCALE
  ))
  df = df.drop(TIME_COL, axis=1)
  return df

data = getData(DATA_FILE)

TRAIN_START = '2014-11-01 00:00:00'
TEST_START = '2014-12-30 00:00:00'

"""PLOT T/T SPLIT"""
# data[(data.index < TEST_START) & (data.index >= TRAIN_START)][['load']] \
#   .rename(columns={'load':'train'}) \
#   .join(data[(data.index >= TEST_START)][['load']] \
#   .rename(columns={'load':'test'}), how='outer') \
#   .plot(y=['train', 'test'], figsize=(15, 8), fontsize=12)

# plt.xlabel(TIME_COL, fontsize=12)
# plt.ylabel('load', fontsize=12)
# plt.show()


train = data[(data.index < TEST_START) & (data.index >= TRAIN_START)][['load']]
test = data[(data.index >= TEST_START)][['load']]
log("Test/Train Shapes (before windows): {}/{}".format(test.shape, train.shape))

# scale data & convert to np arrays
scaler = MinMaxScaler(feature_range=(-1, 1))
train['load'] = scaler.fit_transform(train)
test['load'] = scaler.transform(test)
train_data = train.values
test_data = test.values

# with timesteps
train_data = np.array([
  [j for j in train_data[i:i+WINDOW]]
    for i in range(0,len(train_data)-WINDOW+1)
])[:,:,0]
test_data = np.array([
  [j for j in test_data[i:i+WINDOW]]
    for i in range(0,len(test_data)-WINDOW+1)
])[:,:,0]
log("Windowed Test/Train Shapes: {}/{}".format(test_data.shape, train_data.shape))

# x,y & test/train
x_train, y_train = train_data[:,:WINDOW-1], train_data[:,[WINDOW-1]]
x_test, y_test = test_data[:,:WINDOW-1], test_data[:,[WINDOW-1]]
# log table of test/train vs x/y using pandas
shape_df = pd.DataFrame([
    [x_train.shape, y_train.shape],
    [x_test.shape, y_test.shape]
  ],
  columns=['x', 'y'],
  index=['train', 'test']
)
log("Final Data Shape")
print(shape_df)

model = SVR(
  kernel='rbf', cache_size=4096,
  gamma=.5, C=10, epsilon=.05
)
model.fit(x_train, y_train[:,0])
log("Model Trained")

# predict
y_train_pred = model.predict(x_train).reshape(-1,1)
y_test_pred = model.predict(x_test).reshape(-1,1)
log("Predictions Made with Y pred T/T shapes: {}/{}" .format(
  y_train_pred.shape, y_test_pred.shape
))

# invert predictions and orig values back
y_train_pred = scaler.inverse_transform(y_train_pred)
y_test_pred = scaler.inverse_transform(y_test_pred)
y_train = scaler.inverse_transform(y_train)
y_test = scaler.inverse_transform(y_test)
log("Post Pred Inverted Data Shapes")
shape_df = pd.DataFrame([
    [y_train.shape, y_train_pred.shape],
    [y_test.shape, y_test_pred.shape]
  ],
  columns=['orig', 'pred'],
  index=['train', 'test']
)

# Model performance
train_timestamps = data[(data.index < TEST_START) & (data.index >= TRAIN_START)]\
  .index[WINDOW-1:]
test_timestamps = data[(data.index >= TEST_START)]\
  .index[WINDOW-1:]
log("Train/Test Timestamp Shapes: {}/{}".format(
  train_timestamps.shape, test_timestamps.shape
))

# plot preds on train
if plot_tests:
  plt.figure(figsize=(15, 8))
  plt.plot(train_timestamps, y_train, color='blue', label='Actual', alpha=.5, linewidth=2)
  plt.plot(train_timestamps, y_train_pred, color='red', label='Predicted', alpha=.5, linewidth=2)
  plt.title('Train Data')
  plt.xlabel(TIME_COL, fontsize=12)
  plt.ylabel('load', fontsize=12)
  plt.legend(loc='upper left')
  plt.show()

# MAPE
def mape(actual, pred):
  return np.mean(np.abs((actual - pred) / actual)) * 100

report("Train MAPE: {:.2f}%".format(mape(y_train, y_train_pred)))

# plot preds on test
if plot_tests:
  plt.figure(figsize=(15, 8))
  plt.plot(test_timestamps, y_test, color='blue', label='Actual', alpha=.5, linewidth=2)
  plt.plot(test_timestamps, y_test_pred, color='red', label='Predicted', alpha=.5, linewidth=2)
  plt.title('Test Data')
  plt.xlabel(TIME_COL, fontsize=12)
  plt.ylabel('load', fontsize=12)
  plt.legend(loc='upper left')
  plt.show()

report("Test MAPE: {:.2f}%".format(mape(y_test, y_test_pred)))
warn("Checking Full Dataset performance")
# this is important since we mutated the data above
data = getData(DATA_FILE)
data = data[['load']]
data = scaler.transform(data)

data_windowed = np.array([
  [j for j in data[i:i+WINDOW]]
    for i in range(0,len(data)-WINDOW+1)
])[:,:,0]
log("Full Data Windowed Shape: {}".format(data_windowed.shape))

X, Y = data_windowed[:,:WINDOW-1], data_windowed[:,[WINDOW-1]]
log("Full Data X/Y Shapes: {}/{}".format(X.shape, Y.shape))

Y_pred = model.predict(X).reshape(-1,1)
Y_pred = scaler.inverse_transform(Y_pred)
Y = scaler.inverse_transform(Y)

# plot
plt.figure(figsize=(15, 8))
plt.plot(Y, color='blue', label='Actual', alpha=.5, linewidth=2)
plt.plot(Y_pred, color='red', label='Predicted', alpha=.5, linewidth=2)
plt.title('Full Data')
plt.xlabel(TIME_COL, fontsize=12)
plt.ylabel('load', fontsize=12)
plt.legend(loc='upper left')
plt.show()

report("Full Data MAPE: {:.2f}%".format(mape(Y, Y_pred)))
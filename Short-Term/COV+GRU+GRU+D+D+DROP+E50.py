# -*- coding: utf-8 -*-

from math import sqrt
import tensorflow as tf
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv1D, GRU,LSTM
from tensorflow.keras.losses import mean_squared_error
from numpy.core._multiarray_umath import concatenate
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# supervised监督学习函数


def series_to_supervised(data, columns, n_in, n_out, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('%s%d(t-%d)' % (columns[j], j + 1, i))
                  for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('%s%d(t)' % (columns[j], j + 1)) for j in range(n_vars)]
        else:
            names += [('%s%d(t+%d)' % (columns[j], j + 1, i))
                      for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        clean_agg = agg.dropna()
    return clean_agg
    # return agg

for i in range(0,5):
    dataset = pd.read_csv(
        'Machine_usage_groupby.csv')

    dataset_columns = dataset.columns
    values = dataset.values


    # 归一化处理
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # from sklearn.preprocessing import StandardScaler

    # scaler = StandardScaler()
    # # print(values)
    # scaled = scaler.fit_transform(values)
    scaled = values
    input=192
    output=48
    # mean_values = scaler.mean_

    # 监督学习
    reframed = series_to_supervised(scaled, dataset_columns, input, output)
    values = reframed.values

    # 学习与检测数据的划分
    n_train_hours = 20000
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]
    # print(train)

    # 监督学习结果划分
    train_x, train_y = train[:, 0:input], train[:, input:input+output]
    test_x, test_y = test[:, 0:input], test[:, input:input+output]


    # 为了在LSTM中应用该数据，需要将其格式转化为3D format，即[Samples, timesteps, features]
    train_X = train_x.reshape((train_x.shape[0], 1, train_x.shape[1]))
    test_X = test_x.reshape((test_x.shape[0], 1, test_x.shape[1]))

    model = Sequential()
    model.add(Conv1D(filters=32, kernel_size=3,
                     strides=1, padding="causal",
                     activation="relu"))
    model.add(
        GRU(
            32,
            input_shape=(
                train_X.shape[1],
                train_X.shape[2]),
            return_sequences=True))
    model.add(GRU(16, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(16, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(output))
    model.compile(loss=tf.keras.losses.Huber(),
                  optimizer='adam',
                  metrics=["mse"])
    history = model.fit(
        train_X,
        train_y,
        epochs=50,
        batch_size=72,
        verbose=2)


    import csv
    import  numpy
    out = open(str(i)+"out1.csv", "a", newline='')
    csv_writer = csv.writer(out, dialect="excel")
    # make the prediction
    yHat = model.predict(test_X)
    # yHat = scaler.inverse_transform(yHat)
    # test_y = scaler.inverse_transform(test_y)
    for j in range(0, len(yHat)):
        csv_writer.writerow(numpy.concatenate((yHat[j], test_y[j])))
    model.save(str(i)+'192-48.h5')
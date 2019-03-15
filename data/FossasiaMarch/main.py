import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense

dataset = pd.read_csv('irisSLP.csv')
dataset = pd.DataFrame(dataset)
print (dataset.columns)
dataset = dataset.values

dataset = np.array(dataset)

X = dataset[:, :4]
types = dataset[:, -1]

y = []

for i in range(len(types)):
    if types[i] == 'Iris-setosa':
        y.append([1, 0])
    elif types[i] == 'Iris-virginica':
        y.append([0, 1])

y = np.array(y)

print (X.shape, y.shape)

model = Sequential()
model.add(Dense(2, input_shape=[4, ], activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse', 'accuracy'])
model.summary()

hist = model.fit(X, y, epochs=100)
print (hist.__dict__)
losses = (hist.__dict__['history']['loss'])
accs = (hist.__dict__['history']['acc'])
epochs = np.arange(100)

plt.plot(epochs, losses, color='#5f27cd')
plt.plot(epochs, accs, color='#5f27cd')
plt.show()
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(1)

X_data
Y_data

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=150, batch_size=10)

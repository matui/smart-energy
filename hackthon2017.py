from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
import sys
import csv
import numpy as np

np.random.seed(1)

features = []
answers = []

with open(sys.argv[1], 'r') as csvfile:
    all_rows = csv.reader(csvfile)
    my_rows = []
    for row in all_rows:
         my_rows.append(row)
    for idx,row in enumerate(my_rows):
        if idx!=0:
            for slot in range(0,9):
                if float(row[5+slot])==0.0 and float(row[6+slot])==0.0 and float(row[7+slot])==0.0:
                    continue
                features.append([float(x)/47840395.93 for x in row[5+slot:8+slot]])
                answers.append(float(row[8+slot])/47840395.93)

for idx,row in enumerate(features):
    print row,answers[idx]

model = Sequential()
model.add(Dense(100, input_dim=3, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(20, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(features, answers, epochs=10, batch_size=10)

predictions = model.predict(features,batch_size=10)
for x in predictions:
    print x[0]*47840395.93

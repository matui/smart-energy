from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Dropout
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
            for slot in range(0,7):
                if float(row[5+slot])==0.0 and float(row[6+slot])==0.0 and float(row[7+slot])==0.0:
                    continue
                features.append([float(x)/10000000.0 for x in row[5+slot:10+slot]])
                answers.append(float(row[10+slot])/10000000.0)
with open(sys.argv[2], 'r') as csvfile:
    all_rows = csv.reader(csvfile)
    my_rows = []
    for row in all_rows:
         my_rows.append(row)
    for idx,row in enumerate(my_rows):
        if idx!=0:
            for slot in range(0,7):
                if float(row[5+slot])==0.0 and float(row[6+slot])==0.0 and float(row[7+slot])==0.0:
                    continue
                features.append([float(x)/10000000.0 for x in row[5+slot:10+slot]])
                answers.append(float(row[10+slot])/10000000.0)

with open(sys.argv[3], 'r') as csvfile:
    all_rows = csv.reader(csvfile)
    my_rows = []
    for row in all_rows:
         my_rows.append(row)
    for idx,row in enumerate(my_rows):
        if idx!=0:
            for slot in range(0,7):
                if float(row[5+slot])==0.0 and float(row[6+slot])==0.0 and float(row[7+slot])==0.0:
                    continue
                features.append([float(x)/10000000.0 for x in row[5+slot:10+slot]])
                answers.append(float(row[10+slot])/10000000.0)

#for idx,row in enumerate(features):
#    print row,answers[idx]

model = Sequential()
model.add(Dense(500, input_dim=5, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.13))
model.add(Dense(300, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.11))
model.add(Dense(100, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(50, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(10, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(features, answers, epochs=10, batch_size=10)

predictions = model.predict(features,batch_size=32)
i=0
s=''
for x in predictions:
    if i%7==0:
        print s
        s=''
    s+='{0:10} , '.format(x[0]*10000000.0)
    i+=1

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Dropout
import sys
import csv
import numpy as np

np.random.seed(1)

#Training Data
features = []
answers = []
county = []
town = []
code = []
testers = []
with open(sys.argv[1], 'r') as csvfile:
    all_rows = csv.reader(csvfile)
    my_rows = []
    for row in all_rows:
         my_rows.append(row)
    for idx,row in enumerate(my_rows):
        if idx!=0:
            county.append(row[1])
            town.append(row[2])
            code.append(row[0])
            for slot in range(0,24):
                features.append([float(x)/10000000.0 for x in row[3+slot:15+slot]])
                answers.append(float(row[15+slot])/10000000.0)
            testers.append([float(x)/10000000.0 for x in row[27:-1]])



features = np.asarray(features)
answers = np.asarray(answers)
testers = np.asarray(testers)
print "features",np.shape(features)
print "answers",np.shape(answers)
print "testers",np.shape(testers)

model = Sequential()
model.add(Dense(400, input_dim=12,kernel_initializer='normal', activation='relu'))
model.add(Dense(200, input_dim=12,kernel_initializer='normal', activation='relu'))
model.add(Dense(100,kernel_initializer='normal', activation='relu'))
model.add(Dense(50,kernel_initializer='normal', activation='relu'))
model.add(Dense(25,kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(features, answers, epochs=10, batch_size=32)

predictions = model.predict(testers,batch_size=32)
for i,x in enumerate(predictions):
    print county[i],town[i],code[i],int(x[0]*10000000)

with open(sys.argv[2],'w') as w:
    for i,x in enumerate(predictions):
        s = county[i] + "," + town[i] + "," + str(int(x[0]*10000000))
        w.write(s)
        w.write("\n")

'''
i=0
s=''
for x in predictions:
    if i%24==0:
        print s
        print " "
        s=''
    s+='{0:10} , '.format(int(x[0]*10000000))
    i+=1
'''

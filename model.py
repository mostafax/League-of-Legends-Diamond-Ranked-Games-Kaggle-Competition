import pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import keras
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical

#data Loading
data_set = pd.read_csv('high_diamond_ranked_10min.csv')


#data Normalization
std = StandardScaler()
std.fit(data_set)
data_set = pd.DataFrame(std.transform(data_set),columns=data_set.columns)

#data split
target=data_set['blueWins']
target=to_categorical(target, 2)
features = data_set.iloc[:,2:].values
x_train,x_test,y_train,y_test = train_test_split(features,target,test_size=0.2, random_state=42,shuffle=True)

#model define
model = keras.Sequential()
model.add(Dense(20,activation='relu',kernel_initializer='uniform',input_dim=38))
model.add((Dense(2,activation='sigmoid',kernel_initializer='uniform')))

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),loss='binary_crossentropy', metrics=['accuracy',])
#model train
model.fit(x_train, y_train, batch_size=32, epochs=80,validation_data=(x_test, y_test))
predictions = model.predict(x_test)

#model test
print(model.evaluate(x_test, y_test))

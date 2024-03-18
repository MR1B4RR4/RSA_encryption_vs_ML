import pandas as pd	
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
from Crypto_algorithm import *






df['encrypted_pad'] = pad_sequences(df['encrypted'].tolist(), maxlen = max_sequence_length, padding='post').tolist()


df = df.drop(['word', 'token_cut','encrypted'], axis=1)

X_reshaped = np.array(df['encrypted_pad'].tolist()).reshape((len(df), max_sequence_length, 1))

y = np.array(df['token']).astype(float)


# # Divide the Dataframe into 2 parts (train, test)

# X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.2, random_state=42)

# # Creating the model

# input_dim = X_train.shape[1] 
# output_dim = 1  

# model = Sequential()
# model.add(LSTM(units=50, activation='relu', input_shape=(input_dim, 1)))
# model.add(Dense(output_dim))
# model.compile(optimizer=Adam(learning_rate=0.001, clipvalue=0.5), loss='mean_squared_error')

# # Training the model
# model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# #model.save('model_keras.h5') 

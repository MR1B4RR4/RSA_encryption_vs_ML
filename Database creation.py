import pandas as pd	
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
from Crypto_algorithm import *

# Creating the Dataframe and token for words

file = open("text_file.txt", "r")
content_text = file.read()
file.close()
content_text_characters = content_text.split()
df = pd.DataFrame(content_text_characters).rename(columns={0: "word"})
df['token'] = df['word'].apply(lambda x: map_string_to_numbers(x))
df['token_cut'] = df['token'].apply(lambda x: separate_number_into_pairs(x))

# Encrypting the Dataframe

ex_public_key, ex_private_key =  RSA_generate(7,11) #small primes should be easy to crack right?
df['encrypted'] = df['token'].apply(lambda x: RSA_encryption(x, ex_public_key))

# Dataframe for use
max_sequence_length = max(df['encrypted'].apply(len))
df['encrypted_pad'] = pad_sequences(df['encrypted'].tolist(), maxlen=max_sequence_length, padding='post').tolist()

df = df.drop(['word', 'token_cut','encrypted'], axis=1)


# Divide the Dataframe into 2 parts (train, test)

X_train, X_test, y_train, y_test = train_test_split(df['encrypted_pad'], df['token'], test_size=0.2, random_state=42)

# Creating the model

input_dim = len(X_train.iloc[0])
output_dim = 1  

model = Sequential()

model.add(LSTM(units=50, activation='relu', input_shape=(input_dim, 1)))

model.add(Dense(output_dim))

model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

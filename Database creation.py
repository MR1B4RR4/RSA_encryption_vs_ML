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

df = df[df['token'].apply(lambda x: x.strip() != '')]  # Esto elimina cadenas vacías o espacios

# Removing the tokens that are too long
mean_sequence_length = np.mean(df['encrypted'].apply(len))
std_sequence_length = np.std(df['encrypted'].apply(len)) / 2  

max_sequence_length = int(np.floor(mean_sequence_length + std_sequence_length))

df['token_length'] = df['token'].apply(lambda x: len(x))
df = df[df['token_length'] <= max_sequence_length]

#Ready for EDA

df.to_excel('DF_for_EDA.xlsx')
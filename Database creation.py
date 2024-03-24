import pandas as pd	
import numpy as np
from Crypto_algorithm import *

# Creating the Dataframe and token for words
#Opening file example

file = open("text_file.txt", "r")
content_text = file.read()
file.close()

#Function for spliting sample
def split_text_into_chunks(text, chunk_size=8):
    # Splits the given text into chunks of the specified size, including spaces and punctuation.
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

#Creating DF for the model

content_text_characters =  content_text.split()   #split_text_into_chunks(content_text, chunk_size=8)

df = pd.DataFrame(content_text_characters).rename(columns={0: "word"})

df['token'] = df['word'].apply(lambda x: map_string_to_numbers(x))
df['token_cut'] = df['token'].apply(lambda x: separate_number_into_groups_of_four(x))
# Encrypting the Dataframe

ex_public_key, ex_private_key =  RSA_generate(83,109) #small primes should be easy to crack right?
df['encrypted'] = df['word'].apply(lambda x: RSA_encryption(x, ex_public_key))


df['token_length'] = df['token'].apply(lambda x: len(x))

#EDA
df.to_excel('DF_for_EDA.xlsx')




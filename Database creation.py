import numpy as np
import pandas as pd	
import ast
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
df['encrypted_length'] = df['encrypted'].apply(lambda x: len(x))



print(df)

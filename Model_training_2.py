import pandas as pd	
import numpy as np
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor

from Crypto_algorithm import *


df = pd.read_excel('DF_for_model_training_2.xlsx')
df = df.drop('Unnamed: 0',axis=1)


X = df['encrypted']

y = df['token']


#Divide the Dataframe into 2 parts (train, test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the model

predictor = TabularPredictor(label='token', path='autogluon_models_2').fit(train_data=pd.concat([X_train, y_train], axis=1))

performance = predictor.evaluate(pd.concat([X_test, y_test], axis=1))

print(performance)
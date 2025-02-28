import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("fitness_data.csv")

#Data processing (checking and replacing the missing features)

#print(df.isnull().sum()) #printing out all the missing values

mode_gender = df['Gender'].mode()[0] #finding the most frequent gender
#print(mode_gender)
df['Gender'].fillna(mode_gender, inplace=True)
#print(df['Gender'].isnull().sum())
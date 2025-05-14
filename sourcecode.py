 import pandas as pd

import numpy as np


df = pd.read_csv('customer_satisfaction.csv')

df = df.drop_duplicates()

df.fillna(df.median(numeric_only=True), inplace=True)


for col in df.select_dtypes(include='object').columns:

    df[col].fillna(df[col].mode()[0], inplace=True)


df['yes_no_column'] = df['yes_no_column'].map({'yes': 1, 'no': 0})

numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: np.where(x > x.mean() + 3*x.std(), x.median(), x))
 
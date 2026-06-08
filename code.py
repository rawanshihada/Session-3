import pandas as pd

df = pd.read_csv('./Data/researchers.csv')

df.shape 
df.head() 
df.dtypes 
df.isnull().sum() 
df.describe()
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
print(df.info())

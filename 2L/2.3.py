import pandas as pd
df = pd.read_csv('adult.csv')
print(df.head(10))
print(df.tail(5))
print(df.shape)
print(df.describe())

print(df.iloc[13:17])

print(df[df['workclass'] == 'State-gov'].head(10))

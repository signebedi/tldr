import pandas as pd


df = pd.read_csv('output.csv')

df.head()

# df = df.loc[df.tld.isin(['com','org', 'io', 'net', 'ly'])]
df = df.loc[df.tld.isin(['com','org', 'io', 'net'])]

df.to_csv('further.csv', index=False)
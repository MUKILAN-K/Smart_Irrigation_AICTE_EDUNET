import pandas as pd

df = pd.read_csv("csvflie.csv")

print("First 10 rows:\n")
print(df.head(10))

print("Last 3 rows:\n")
print(df.tail(3))

print("Dataset shape (rows, columns):\n")
print(df.shape)

print("Column names:\n")
print(df.columns)

print("Data types of each column:\n")
print(df.dtypes)

print("Info about dataset:\n")
df.info()

df = df.drop('Unnamed: 0', axis=1)
print("Dropped 'Unnamed: 0' column.\n")

print("First 5 rows after drop:\n")
print(df.head())

print("Statistics summary:\n")
print(df.describe())

X = df.iloc[:, 0:20]
y = df.iloc[:, 20:]

print("Sample rows from features (X):\n")
print(X.sample(5))

print("Sample rows from labels (y):\n")
print(y.sample(5))

print("Shape of Features (X):\n", X.shape)
print("Shape of Labels (y):\n", y.shape)

print("Random rows from full dataframe:\n")
print(df.sample(5))


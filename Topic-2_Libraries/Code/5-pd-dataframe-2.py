import pandas as pd

d = {
    "one": [1.0, 2.0, 3.0],
    "two": [11.0, 12.0, 13.0]
}

df = pd.DataFrame(d, index=['a', 'b', 'c'])
print(df)
print(df.shape)

print(df.columns)
print(df.index)

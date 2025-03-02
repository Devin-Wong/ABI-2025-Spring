import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0, 4.0], index = ['a', 'b', 'c', 'd']),
    "two": pd.Series([11.0, 12.0, 13.0], index = ['d', 'b', 'c'])
}

df = pd.DataFrame(d)
print(df)
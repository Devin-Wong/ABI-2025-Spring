import pandas as pd

d = {
    "Name": ["Jack", "Ben", "Mary", "Jin"],
    "HW": [99.0, 98.0, 97.0, 89.0],
    "Exam": [90.0, 91.0, 79.0, 80.0],
}

df = pd.DataFrame(d)

# df = df.set_index("Name")
# print(df)

df.index = ['a', 'b', 'c', 'd']
print(df)
print(df.shape)
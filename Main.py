import pandas as pd

data = {'type': ['x', 'x', 'y'],
        'A': [1, 0, 1],
        'B': [0, 0, 0],
        'C': [1, 1, 1]}

# Create an index labeled as 'idx'
index = [0, 1, 2]

# Create a DataFrame
df = pd.DataFrame(data, index=index)
df.index.name = 'idx'
print(df)
sorted = df.groupby('type')
last_row = sorted.apply(lambda x: x.loc[x.index.max()])
column = sorted.apply(lambda x: x.index.max())
last_row["org_index"] = column.values
print(column)
print(last_row)

a = df.columns

print(a)
original_string = "Hello, World!"

# Reverse the string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print(reversed_string)
b = 'CCC'
c = b.lower()
print(c)
first_column_values = df.iloc[:, 1].values
print(first_column_values)
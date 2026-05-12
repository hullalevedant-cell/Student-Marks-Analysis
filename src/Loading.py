import pandas as pd

data = pd.read_csv('data/Students.csv')
df = pd.DataFrame(data)

print('\n')
print('Dataset of the students is as follows :- ') 
print('\n')
print(df)
print('\n')
print('Shape of the dataset :-')
print(df.shape)
print('\n')
print('Column names :-')
print(df.columns)
print('\n')
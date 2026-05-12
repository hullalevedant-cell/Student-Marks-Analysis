import pandas as pd

data = pd.read_csv('data/Students.csv')
df = pd.DataFrame(data)

df['Total'] = df['maths_marks'] + df['science_marks'] + df['english_marks'] + df['social_studies_marks'] + df['language_marks']
df['Percentage'] = (df['Total'] / 500) * 100

sorted = df.sort_values(by='Percentage', ascending=False, inplace=False).reset_index(drop=True)

print(sorted)
print('\n')

topper_name = sorted.loc[0, 'student_name']
topper_percentage = sorted.loc[0, 'Percentage']
print(f"the topper of the class is {topper_name} , with a whopping {topper_percentage} percentage !!!")
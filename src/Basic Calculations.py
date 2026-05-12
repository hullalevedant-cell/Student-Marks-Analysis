import pandas as pd

data = pd.read_csv('data/Students.csv')
df = pd.DataFrame(data)

def get_grade(percentage):
    if(percentage >= 90):
        return 'A'
    elif(percentage >= 80):
        return 'B'
    elif(percentage >= 70):
        return 'C'
    elif(percentage < 35):
        return 'F'
    else:
        return 'D'

print(df) # to be removed later

df['Total'] = df['maths_marks'] + df['science_marks'] + df['english_marks'] + df['social_studies_marks'] + df['language_marks']
df['Percentage'] = (df['Total'] / 500) * 100
df['Status'] = ['pass' if x > 35 else 'fail' for x in df['Percentage']]
df['Grade'] = df['Percentage'].apply(get_grade)
print(df)
import pandas as pd

df = pd.read_csv("data.txt", sep=",")

print(df)

Subjects = ["Math", "Physics", "Chemistry", "English"]


highest_math_sorted = df.sort_values("Math", ascending=False)
maths_topper_name = highest_math_sorted['Name'].iloc[0]  
maths_topper_marks = highest_math_sorted['Math'].iloc[0]
print(f"Maths topper is --> {maths_topper_name} : {maths_topper_marks}")

highest_physics_sorted = df.sort_values("Physics", ascending=False)
physics_topper_name = highest_physics_sorted['Name'].iloc[0]  
physics_topper_marks = highest_physics_sorted['Physics'].iloc[0]
print(f"Physics topper is --> {physics_topper_name} : {physics_topper_marks}")

highest_chemistry_sorted = df.sort_values("Chemistry", ascending=False)
chemistry_topper_name = highest_chemistry_sorted['Name'].iloc[0]  
chemistry_topper_marks = highest_chemistry_sorted['Chemistry'].iloc[0]
print(f"Chemistry topper is --> {chemistry_topper_name} : {chemistry_topper_marks}")

highest_english_sorted = df.sort_values("English", ascending=False)
english_topper_name = highest_english_sorted['Name'].iloc[0]  
english_topper_marks = highest_english_sorted['English'].iloc[0]
print(f"English topper is --> {english_topper_name} : {english_topper_marks}")





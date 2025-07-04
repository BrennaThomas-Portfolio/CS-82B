# CS 82B
# Module 3 Lab 1: Data & Pandas
# BRENNA THOMAS


'''file = open('data.csv', 'r', encoding='utf-8')

header = file.readline().strip().split(',')
print("Header:", header)

data = []
lines = file.readlines()
for line in lines:
    row = line.strip().split(',')
    data.append(row)

print("Data:")
for row in data:
    print(row)

file.close()'''

import pandas as pd
import seaborn as sns




# load the Titanic dataset read_csv()
titanic_df =  titanic_df = pd.read_csv("titanic.csv")

print(titanic_df.columns)

# create a new column is_child
titanic_df['is_child'] =  titanic_df['is_child'] = titanic_df['Age'] < 18 

# create a new column family_size
titanic_df['family_size'] =  titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1

# display the first 5 rows of the DataFrame
print(titanic_df.head())



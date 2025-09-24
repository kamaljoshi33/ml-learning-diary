# 1. Label encoding - it will replace  every text with number. like(data-1, text-2) 
#  2. one-hot encoding - it is done for unique values




# This is label encoding 
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {
    'name': ['kamal', 'joshi', 'user', 'testData', 'user'],
    'age': [14, 25, 45, 18, 95],
    'gender': ['male', 'female', 'male', 'female', 'sss']
}

df = pd.DataFrame(data)
print(df)

create_copy = df.copy()
le = LabelEncoder()
create_copy['Gender_encoded'] = le.fit_transform(create_copy['gender'])
print(create_copy[['name','gender', 'Gender_encoded']])












# one code encoding 

df_encoded = pd.get_dummies(create_copy, columns=['name'])

print(df_encoded)
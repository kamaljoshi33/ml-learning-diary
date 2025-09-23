# 👉These are the 4 step for data preprocessing :-
#  1.Handling missing data -
# 2.Encoding categorical values - 
# 3.Feature Scaling - 
# 4.Split data - 



# it is necessay to do step of preprocessing or clean data 


# handling missing data :-
# dropna() - if you need to remove any row or column if missing value is present then use this.
# fillna(value) - if nan value is present and we need to update that value then we can use this to update this nan value
# isnull.sum() - it will find total number of missing values in a column.


import pandas as pd
import json

data = {
    "id": [1, 2, 2, None, 5, 5],
    "name": ["Alice", "Bob", "Bob", None, "Eve", "f"],
    "age": [25, 30, 30, None, 29, 29]
}

df = pd.DataFrame(data)

data_quality_report ={
    "null_count" : df.isnull().sum().to_dict(),     #get the total number of null
    "duplicate_row" : df[df.duplicated()].to_dict(orient="records"),     #find the duplicate data 
    "duplicate_count" : int(df.duplicated().sum()),          #duplicate count
    "unique_values" : {col : df[col].nunique() for col in df.columns},    #so it count unique values.
    "data_types": df.dtypes.astype(str).to_dict(),
    "missing_percentage": (df.isnull().mean() * 100).to_dict(),
    "drop_null_values" : df.dropna().to_dict(),    #drop null rows
    "update_null_values" : df.fillna(400).to_dict(),    
    "missing_percentage": (df.isnull().mean() * 100)           
    # "update_null_in_colum" : df['age'].fillna(500)

}
print(json.dumps(data_quality_report, indent=10))
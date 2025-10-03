import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

read_file = pd.read_json(r"C:\Users\kamal joshi\Desktop\python\data.json")
x = read_file[['hour']]
y = read_file['marks']

model = LinearRegression()
model.fit(x,y)
print(read_file)
predicted_model = model.predict(x)
mae = mean_absolute_error(y, predicted_model)
mse =mean_squared_error(y,predicted_model)
rmse = root_mean_squared_error(y,predicted_model)

# new_prediction = float(input('enter a hour : '))
# new_PRe = model.predict(new_prediction)
# print("prediction is : {new_PRe}")



print("mae",mae)
print("mse",mse)
print("rmse",rmse)

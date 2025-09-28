# accuracy = correct_Pred / total_pred
# precision = it used when false statement avoid
# recall = it is used in to match possible cases
# F1 score = precision and recall balance output help.

# 😀code
# sklearn.metrics = it is used for score the result
# from sklearn.metrics import accuracy_score, precision_score, recall_score,f1_score
# # True answer [what actually happend]
# y_true = [1,0,1,1,0,1,0]
# # model prediction [hwat is gussed]
# y_pred = [1,0,1,0,0,1,1]

# # evaluated
# print('accuracy', accuracy_score(y_true,y_pred)) #accuracy is not enough when data is unbalance
# print('Precision', precision_score(y_true,y_pred)) #a
# print('Recall', recall_score(y_true,y_pred)) #missing case should majorly used
# print('f1 score', f1_score(y_true,y_pred))






# confusion matrix =
# 1. true positive - correct guess
# 2. ture negative - correct guess
# 3. flase positve - false guess
# 4. flase negative - flase guess

# from sklearn.metrics import confusion_matrix
# y_true = [1,0,1,1,0,1,0,0,1,0]
# y_pred = [1,0,1,0,0,1,1,0,1,0]
# cm = confusion_matrix(y_true,y_pred)
# print(cm)

# output                  [[4 1]   4 is true negative,   1 is false positive
#                          [1 4]]   1 is false negative  4 is true positive










# 👉MAE - mean absolute error
# 1. take the mistake difference
# 2.remove teh minus SyntaxWarning
# 3. add the difference
# 4. divide them by total 
# 5. get on an average 




#👉 MSE - mean square error
# 1. get mistake  and square them
# 2. add them
# 3. divide total 



# 👉RMSE = root mean square error 


from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error
import numpy as np

# real score
real_score  = [90,60,80,100]

# model guess
predited = [85,70,70,95]

mae = mean_absolute_error(real_score,predited)
mse = mean_squared_error(real_score,predited)
rmse = root_mean_squared_error(real_score, predited)
rmse_by_numpy = np.sqrt(mse)

print('mae',mae)   # get simple mark error or small data
print('mse',mse)    # used in large scale. it detect the big mistake
print('rmse',rmse)   # used to know what is the erro in real unit 
print('rmse_by_numpy',rmse_by_numpy)


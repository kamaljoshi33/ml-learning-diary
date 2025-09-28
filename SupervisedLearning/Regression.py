#  Regression 

# 1.Linear Regression - help to predict the number 
# -find the patter
# -straight line relation between input and output
# Y= mx+c

# 😀code
# from sklearn.linear_model import LinearRegression
# x=[[1],[2],[3],[4],[5]]
# y=[40,50,60,70,80]
# model = LinearRegression() 
# model.fit(x,y)
# hour = float(input('Enter how many hour you studies ='))
# predicted_marks = model.predict([[hour]]) # 2d list . it will always in 2d array like 
# print('on the basis of input u can get marks ', predicted_marks)




# 👉note
# -it not about the line, it about story
# - u can use 5 rows to predicit data u dont need big data always
# - accuracy is not always goal





# classifiction  :- it is differnet form regression.
# it always provide output 1 or 0 (yes or no).


# 😀code
# from sklearn.linear_model import LogisticRegression
# a=[[1],[2],[3],[4],[5]]
# b=[0,0,1,1,1]
# model = LogisticRegression()
# model.fit(a,b)
# hour =float(input('enter the hour :'))
# result = model.predict([[hour]])[0]
# print(result)
# if result == 1:
#     print('u are pass ')
# else:
#     print('u need more learning')









# K&n regression  - nearset data check and giver predication accoring to nearest one 


# 😀code
# from sklearn.neighbors import KNeighborsClassifier
# x = [
#     [180,7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [330,9],
#     [360,9.5]
# ]
# # 0->apple 1->orange predication
# y = [0,0,0,1,1,1]
# mode = KNeighborsClassifier(n_neighbors=3) #how much neighbors it will take to predict
# mode.fit(x,y)
# weight = float(input('enter the weight = '))
# size = float(input('enter the size = '))
# prediction = mode.predict([[weight, size]])[0]   # 0 is passed here because at 0 of output we will get actual output
# if prediction == 0 :
#    print('this is an apple')
# else : 
#     print('this is an orange ')




# decision tree classifier =
from sklearn.tree import DecisionTreeClassifier
x = [
    [7,2], #apple
    [8,3], #apple
    [9,8], #orange
    [10,9] #orange
]
y = [0, 0, 1, 1]  # 0=Apple, 1=orange
modell = DecisionTreeClassifier()
modell.fit(x,y)

size = float(input('enter the fruit size ='))
shade = float(input('enter the color shade [1-10] = '))
result = modell.predict([[size, shade]])[0]
if result == 0:
    print('this is apple')
else :
    print('this is orange')



# overfiting - deep analysis. model learn deeply to predict outcome
# underfiting - not have deep analysis. mode is under learning 
# goodfiting - it have leaning multiple things but not provide sometime acurate output and need more to learn




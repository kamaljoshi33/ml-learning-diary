# Median = Middle value when numbers are sorted.
# If odd count → the middle number.
# If even count → average of two middle numbers.


number  = [10,20,30,40,50,60,70]
number.sort()
n = len(number)
if n % 2 == 1:
    median = number[n // 2]
else:
    median = (number[n // 2]+number[n // 2]) / 2

print(median)
# Mode = Most frequent number in the list.

numbers = [10, 20, 30, 40, 50, 60, 70]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num , 0) + 1
mode = max(frequency, key=frequency.get)
print("Mode:", mode)
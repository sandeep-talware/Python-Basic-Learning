numbers = [5,2,4,10,4,4,9,11]
large = 0
for number in numbers:
    if number > large:
        large = number
print(f"Largest number from array in {large}")

numbers = [5,2,4,10,1,15,9,11]
large = numbers[0]
for number in numbers:
    if number > large:
        large = number
print(f"Largest number from array in {large}")
small = numbers[0]
for number in numbers:
    if number < small:
        small = number
print(f"Smallest number from array in {small}")

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for col in row:
        print(col,end=" ")
    print()

numbers = [3,5,7,9,2,10,22]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(0,8)
print(numbers)

numbers = [3,5,7,9,2,10,22]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(0,8)
print(numbers)
numbers.remove(7)
print(numbers)
numbers.pop()
print(numbers)
print(f"Index of  9 : {numbers.index(9)}")
print(f"number 2 is present in list : {2 in numbers}")
print(f"number 19 is present in list : {19 in numbers}")
numbers.sort()
print(f"Sorted Acending list : {numbers}")
numbers.reverse()
print(f"Sorted desending list : {numbers}")
numbers2=numbers.copy()
numbers.clear()
print(numbers)
print(numbers2)

numbers = [3,5,7,9,2,10,22,2,9,10]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
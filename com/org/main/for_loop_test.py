for item in 'Python':
    print(item)

for item in ['Python',"Java",'CPP']:
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)

prices = [10,20,30]
sum = 0
for price in prices:
    sum += price
print(sum)

i = 1
for x in range(4):
    for  y in range(4):
        print(f"{i}({x},{y})")
        i += 1

numbers = [5,2,5,2,2]
for number in numbers:
    str = ""
    for num in range(number):
        str += "X"
    print(str)

numbers = [5,2,5,2,2]
for number in numbers:
    for num in range(number):
        print("X",end="")
    print()
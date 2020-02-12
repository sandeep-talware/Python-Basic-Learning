# name=input("What is your name? ")
# favorite_color=input("What is your color? ")
# print(name +" like " + favorite_color)

weight_lbs=input("Weight in pounds : ")
weight_kgs=float(weight_lbs)*0.45
print(weight_kgs)
birth_year=input('Birth Year : ')
print(type(birth_year))
age=2019-int(birth_year)
print(type(age))
print('Age : '+str(age))


# Number
print(10+2)
print(10/3)
print(10//3)
x=(10+3)*2
print('x: '+str(x))

#import math

print(math.ceil(2.9))
print(math.floor(2.9))
x=2.9
print(round(x))
print(abs(-3.8))

#import math

is_good_credit=False
price=1000000
if (is_good_credit):
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f'Down payment required is ${down_payment}')
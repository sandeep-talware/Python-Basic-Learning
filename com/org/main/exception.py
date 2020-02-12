try:
    age = int(input("Enter age : "))
    print(age)
    income=20000
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print("Age can not be zero.")
except ValueError:
    print("Enter only numerical value.")

has_high_income=True
has_good_credit=True
if(has_high_income and has_good_credit):
    print("Eligible for loan")
else:
    print("Not eligible for loan")

name="Sandeep"
if(len(name)<3):
    print("Name must be greater than 3")
elif (len(name)>50):
    print("name must be less than 50")
else:
    print("name looks good")

weight = float(input("Weight : "))
unit = input("(L)bs or (K)g ")
if unit.lower() == 'l':
    weight *= 0.453592
    weight_str = str(weight) + " pounds."
elif unit.lower() == 'k':
    weight *= 2.20462
    weight_str = str(weight) + " Kgs."
else:
    weight_str = "Wrong choice"
print(f"you are {weight_str}")

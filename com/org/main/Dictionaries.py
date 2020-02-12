# Key Value pair
# it is case sensitive in terms of kay name as well
# dict[not_preseny_key] will throw error but dict.get(not_present_key) do not throw error

Customer = {
    "name":"John Smith",
    "age":27,
    "is_verified":True
}
print(Customer)
print(Customer["name"])
print(Customer.get("name"))
Customer["name"]='Jon Snow'
print(Customer.get("name"))
Customer["birthdate"]="Aug 22 1991"
print(Customer.get('birthdate'))

digit = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
    '0':'Zero'
}

phone=input("Enter Phone number : ")
for ch in phone:
    print(digit[ch], end=" ")
finalString = ""
for char in phone:
    finalString += digit.get(char,"!")+" "
print(finalString)
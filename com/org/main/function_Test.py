# Positional arguments in which order of parameters are matter i.e. change in passing argument will change behaviour
def gretings():
    print("Hi, Brother")
    print("Have Breakfast?")


print("Start")
gretings()
print("Finish")


def gretings_with_para(first_name,last_name):
    print(f'Hi, {first_name} {last_name}')
    print("Have Breakfast?")


print("Start")
gretings_with_para("Sandeep","Talware")
print("Finish")


# Keywords argument
# If you are using combination of both Keyword and positional argument then first pass positional argument then pass Keyword argument
def gretings_with_para_keywords(first_name,last_name):
    print(f"Hi, {first_name} {last_name} !")
    print("Have Breakfast?")


print("Start")
gretings_with_para_keywords(last_name="Talware", first_name="Sandeep")
print("Finish")


# Function with return statement, by default it return None
def square(number):
    return number*number


print(square(3))


def emojiMessage(message):
    emojis = {
        ":)": "😊",
        ":(": "😥"
    }
    words=message.split(" ")
    outstring=""
    for word in words:
        outstring += emojis.get(word,word)+" "
    return outstring


print(emojiMessage(input("Enter Message : ")))


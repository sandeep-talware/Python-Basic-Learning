# for windows 10 to get emoji list need to press "Windows key + >" or "windows key + ;"

emojis = {
    ":)":"😊",
    ":(":"😥"
}
message=input("Enter message : ")
words=message.split(" ")
outString=""
for word in words:
    outString += emojis.get(word,word)+" "
print(outString)
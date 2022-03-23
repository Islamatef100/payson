import string
import random
# i need password contain 30% upper letter and 30% lower letter and 20% digits and 20% punctuation
l3=list(string.digits)
l1=list(string.ascii_uppercase)
l2=list(string.ascii_lowercase)
l4=list(string.punctuation)
numberOfCharacter=input("how many number of character: ")
while True:
    try:
        convert_string_to_number=int(numberOfCharacter)
        if convert_string_to_number<6:
            numberOfCharacter = input("plz enter number more than six. ")
        else:
            break
    except:
        numberOfCharacter = input("plz enter correct number again. ")
random.shuffle(l1) # rearrange rundom number of list
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)
password=[]
firstPart=round(convert_string_to_number*(30/100))
secondPart=round(convert_string_to_number*(20/100))
for i in range(firstPart):
    password.append(l1[i])
    password.append(l2[i])

for i in range(secondPart):
    password.append(l3[i])
    password.append(l4[i])
lastpassword=""
for i in password:
    lastpassword+=i    # to get string
print(lastpassword)

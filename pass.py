import string
import random
length=int(input("enter password length: "))
print('''enter
1. digits
2. uppercase
3. lowercase
4.symbol
5.exit''')
list=""

while True:
    x=int(input("enter your choice :"))

    if x==1:
        list +=string.digits
    elif x==2:
        list +=string.ascii_uppercase
    elif x==3:
        list +=string.ascii_lowercase
    elif x==4:
        list +=string.punctuation
    elif x==5:
        break
    else:
        print("invalid")
password=[]
for i in range(length):
    x=random.choice(list)
    password.append(x)
print("password is "+"".join(password))


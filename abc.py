import random
import string

length=int(input("length  :"))
list=""

while True:
    choice=int(input("enter youe chice:"))
    if choice==1:
        list +=string.digits
    elif choice==2:
        list +=string.ascii_letters
    elif choice==3:
        list+=string.punctuation
    elif choice==4:
        break
    else:
        print("invalid choice")
password =[]
for i in range(length):
    x=random.choice(list)
    password.append(x)
print("the password"+"".join(password))

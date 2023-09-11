import string
import random
length = int(input("enter the password length :"))
print('''choice 
1.digits
2. lower_letter
3. upper_letter
4. special symbol
5. exit''')
list=""
while 0==0:
    choice=int(input("enter your choice : "))
    if choice==1:
        list +=string.digits
    elif choice==2:
        list +=string.ascii_lowercase
    elif choice==3:
        list +=string.ascii_uppercase
    elif choice==4:
        list +=string.punctuation
    elif choice==5:
        break
    else:
        "invalid choice"
password =[]
for i in range(length):
    x=random.choice(list)
    password.append(x)
print("password is:"+"".join(password))


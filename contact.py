import json
import time
file = open("contact_manager.json", "r")
x = list(json.load(file))
def add_contact():


    name=input("enter your name")
    number = input("enter your number")
    address = input("enter your address")

    y={
        "name":name,
        "number": number,
        "address": address
    }
    x.append(y)
    writefile=open("contact_manager.json","w")
    writefile.write(json.dumps(x))

def show_contact():
    for i in range(0,len(x)):
            print(x[i]['name'] + "\t" + x[i]['number'] +"\t" +x[i]['address'])
            file.close()

while 0==0:
    print('''select your choice
    1. add_contact
    2. show contact
    3. exit''')

    req=int(input("enter your choice : "))
    if req==1:
        add_contact()
    elif req == 2:
        show_contact()
    elif req == 3:
        exit(0)
    else:
        print("invalid")
        time.sleep(2)
        print("\n\n\n")
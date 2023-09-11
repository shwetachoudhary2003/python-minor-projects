import json
def search_contact(x):
    file=open("contact_manager.json","r")
    data= list(json.load(file))
    for i in range(0,len(data)):
        if data[i]['name'] == x:
            result= data[i]['name'] +"\t" +data[i]['number'] + "\t" + data[i]['address']
            break
        else:
            result= 'invalid'
    print(result)
    file.close()
x=input("enter the number you want to search.")
search_contact(x)

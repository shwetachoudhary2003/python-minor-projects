def check(x):
    savenumber = 5
    if(int(x)==savenumber):
        return "true"
    else:
        return "false"

for i in range(1,4):
    userinput=int(input("enter guess number :"))
    if(check(userinput)=="true"):
        print("sucess")
        break

    else:
        print("try again")
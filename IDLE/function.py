
def fullName(fName,lName):
    print(fName+' '+ lName)


fullName('Ruhul','Amin')

def add(n1,n2):
    return n1+n2

for i in range(0,20,1):
    if i%2 is 0:
        print(add(12,i))
    else:
        print("Odd")
        

def result(name="ruhul",schore="122"):
    print(name  , " Schored " , schore)

result()
result("sakib",122)

def summation(arg1,arg2):
    if(type(arg1)!=type(arg2)):
        print("provide a valid info")
        return -1
    else:
        return arg1+arg2

print(summation('12',11))

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

def touple(name="some name",*marks):
    if(name == "some name"):
        name="Ruhul amin"
        print(name)
        print(marks)
    else:
        print(marks)

touple("some name",(1,2,3,3,4))

def models(name,*marks):
    if name == "ruhul":
        print("####################")
        for x in marks:
            print(x)

models("ruhul",(12,32,33,4))

def myResult(name,**marks):
    for name,marks in marks.items():
        print(name, " => " , marks)

myResult("Ruhul",ruhul=12,sakib=43,sajid=54,abid=322)

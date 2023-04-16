
num = int(input('Enter a Number'))

if num<0:
    print("Number is lessthen 0")
elif num==0:
    print("Number is Zero")
else:
    print("Number is positive")


valMax=int(input('Enter a number'))

if valMax>10:
    if valMax**2>100:
        if valMax**3>1000:
            print('Good Number!')
        else:
            print('Not Good Number!')
    else:
        print('Close to good numbe')
else:
    print('Bad Number')
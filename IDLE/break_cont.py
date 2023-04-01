
a = [1,2,3,4,5]
for i in a:
    if i == 3:
        break
    else:
        print(i)
        i+=1
print("############")
while i in a:
    if i == 1:
        continue
    else:
        print(i)
        i+=1

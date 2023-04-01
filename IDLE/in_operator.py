
#list in python
a = [1,2,3,4,5]
#set in python
b = {1,2,3,4,5}
#touple in python
c =(1,2,3,4,5)
#dictionary in python
d = {
    'name':'ruhul amin',
    'email':'r@gmail.com'
}
#string in python
e = '01234'
print(0 in a)
print(1 in b)
print('name' in d)
print('x' in e)

for x in a: print(x)
print('The values')
for x in d.values():print(x)
print('The keys')
for x in d.keys():print(x)

myDictionary = {
    'name':'Ruhul AMin',
    'email':'r@gmail.com',
    'contact':'01322352864'
}
print("My dictionary  :")
for key,item in myDictionary.items():
    print(key, " => " , item)
for x in range(6):
    print(x*x)
for x in a:
    print(x)
print('#################3')
for i in range(1,40,4):
    print(i)
else:
    print("Finished")
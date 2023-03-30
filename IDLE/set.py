
myset = {1,2,3,1,1}
print(myset)
myset.add(12)
print(myset)
print(len(myset))
myset.update([1222,12,42])
print(myset)
myset.remove(12)
myset.clear()
#using constructor
val = set(('ruhul','max'))
print(val)

a = {1,2,3,4}
b = {2,4,5,7,8}
c = a.union(b)
print(c)
d = a.intersection(b)
print(d)
e = a - b
print(e)
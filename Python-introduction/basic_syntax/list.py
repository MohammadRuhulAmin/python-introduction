names=['ruhul','amin','sakib']
print(names)
print(names[-1])
print(names[1])
names.append("Mumtahina")
names.append("Tamim")
print(names)
print(names[-1])
ages=[12,22,1,123]
ages.append(12)

mix = names.extend(ages)
print(names)
print(names,ages)
print(names,ages,mix)


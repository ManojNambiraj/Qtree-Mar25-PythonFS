# Tuple - (Unchangable)

myTup = ("apple", "banana", "grapes", 100, True, "apple")

# print(myTup[-3])
# print(len(myTup))
print(type(myTup))

mylist = list(myTup)

print(type(mylist))

mylist[1] = "kiwi"

print(mylist)

mytup2 = tuple(mylist)

mytup2.remove(True)

print(mytup2)
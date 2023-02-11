myList = [1,2,3,4,5]
myList[3] = 44
print(myList)

myList.insert(0,22)
print(myList)
myList.append(33)
print(myList)
newList = [77,87,97]
myList.extend(newList)

print(myList)
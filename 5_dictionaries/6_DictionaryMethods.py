dictionary = {
    'age' : 20
}

# dictionary.clear()

# newDict = dictionary.copy()
# print(newDict)

dicti = {}.fromkeys([1,2,3],0)
print(dicti)

# print(dictionary.get('name'))
# print(dictionary.items())
# print(dictionary.keys())

# print(dictionary.setdefault('name','ssnf'))

newDict = {
    'place' : 'Chennai',
    'Gender' : 'Male'
}

dictionary.update(newDict)
print(dictionary)

print('place' in dictionary)
theDict = {
    1 : True,
    2 : True
}
# print(all(theDict))

print(any(theDict))

print(len(dictionary))

print(sorted(dictionary, reverse=True))
print(sorted(dictionary, key=len))
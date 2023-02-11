a = ['a','b','c','d','e']

# print('a' in a)

print(a.index('a'))

def searching(tuple, val):
    for i in range(0, len(tuple)):
        if tuple[i] == val:
            return i
    return 'there was an error'

print(searching(a, 'd'))
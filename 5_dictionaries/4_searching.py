myDict = {
    'name' : 'shaam',
    'age' : 20
}

def searching(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'There was an error'
print(searching(myDict, 20))
from array import *
arr1 = array('i',[1,2,3,4,5])

def sorter(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    else:
        return 'There is no such value'

print(sorter(arr1, 3))
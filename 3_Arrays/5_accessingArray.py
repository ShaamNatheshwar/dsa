from array import *

arr1 = array('i',[1,2,3,4,5])

def access(array,index):
    if index > len(array):
        print('There is an error')
    else:
        print(array[index])

access(arr1,4)
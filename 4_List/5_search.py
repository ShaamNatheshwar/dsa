a = [10,20,30,40,50,60]

# if 20 in a:
#     print(a.index(20))
# else:
#     print('There was an error')

def searching(list, value):
    for i in list:
        if i == value:
            print(list.index(value))
    return 'There was nothing'
searching(a, 20)
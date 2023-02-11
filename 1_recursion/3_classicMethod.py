def first():
    second()
    print('One')

def second():
    third()
    print('two')
def third():
    print('Third')
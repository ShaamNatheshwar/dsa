#Russian Doll
# A simple russian doll example for recursion
def russianDoll(doll):
    if doll == 1:
        print('All dolls are opened')
    else:
        russianDoll(doll-1)

russianDoll(5)

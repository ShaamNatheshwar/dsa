# print(112/10)
# print(112%10)
# print(112//10)

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'There is an error'
    if n == 0:
        return 0
    else:
        return (n%10) + sumOfDigits(n//10)

print(sumOfDigits(229))
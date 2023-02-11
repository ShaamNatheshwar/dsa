def factorial(n):

    assert n >= 0 and int(n) == n, 'The number has to positive integer no float or decimals '
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(10))
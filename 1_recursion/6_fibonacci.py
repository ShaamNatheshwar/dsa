def fib(n):
    assert n >= 0 and int(n) == n, 'There was an error'
    if n in [0,1]:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))
def recursive(n):
    if n < 1:
        print('Less than one')
    else:
        recursive(n-1)
        print(n)
recursive(5)

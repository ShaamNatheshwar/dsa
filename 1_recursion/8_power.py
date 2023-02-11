def pow(base, exp):
    assert int(exp) == exp, 'There is an error'
    if exp == 0:
        return 1
    elif exp <= 0:
        return 1/base * pow(base, pow+1)
    else:
        return base * pow(base, exp-1)
print(pow(-2,3))
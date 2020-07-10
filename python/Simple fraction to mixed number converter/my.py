
def mixed_fraction(s):

    a, b = s.split('/')
    res, pl = "", 0
    a, b = int(a), int(b)
    if b == 0:
        raise ZeroDivisionError
    if a == 0:
        return "0"
    if  a < 0:
        pl = pl + 1
        a *= -1
    if  b < 0:
        pl = pl + 1
        b *= -1
    if pl == 1:
        res += "-"
    if a % b == 0:
        return res + str(a//b) 
    c = 0
    if a > b:
        c = a//b
        a = a - c * b
    a1 = a
    b1 = b
    while a1 != 0 and b1 != 0:
        if a1 > b1:
            a1 %= b1
        else:
            b1 %= a1
    m = a * b
    a = a//(a1+b1)
    b = b//(a1+b1)
    if c != 0:
        res += str(c) + " "
    res += str(a) + "/" + str(b)
    return res




print(mixed_fraction('15272326/-7636163'))


"""print(mixed_fraction('42/9'),"==",'4 2/3')
print(mixed_fraction('6/3'),"==", '2')
print(mixed_fraction('4/6'),"==", '2/3')
print(mixed_fraction('0/18891'), "==", '0')
print(mixed_fraction('-10/7'), "==", '-1 3/7')
print(mixed_fraction('-22/-7'), "==", '3 1/7')
print(mixed_fraction('-22/0'))
Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(0, 0))
Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(3, 0))"""



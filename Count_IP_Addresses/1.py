
def ips_between(start :str, end :str):
    st, en = start.split('.'), end.split('.')
    sum_1, sum_2 = 0, 0
    step = 3
    st = [int (item) for item in st] 
    en = [int (item) for item in en]
    for i in st: 
        sum_1 += i*256**step
        step = step-1
    step = 3
    for i in en:
        sum_2 += i*256**step
        step = step-1
    return sum_2 - sum_1




print(ips_between("10.0.0.0", "10.0.0.50"))
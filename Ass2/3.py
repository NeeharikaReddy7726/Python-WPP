# Func tofindthe no.of digits divide N
def count_dividing_digits(N):
    count = 0
    str_N = str(N) 
    for digit in str_N:
        if digit != '0':
            if N % int(digit) == 0:
                count += 1
    return count

#no.of
T = int(input())

# each test case
for _ in range(T):
    N = int(input()) 
    result = count_dividing_digits(N)
    print(result)
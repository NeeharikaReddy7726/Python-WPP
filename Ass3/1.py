# Add sum of digits until it becomes a single digit number
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

number=int(input("Enter the input number"))
print(digital_root(number))
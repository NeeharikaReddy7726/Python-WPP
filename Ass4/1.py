def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0
    
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))
    
    return operations

# Read input
T = int(input().strip())  # Number of test cases

for _ in range(T):
    s = input().strip()  # Read each string
    print(min_operations_to_palindrome(s))
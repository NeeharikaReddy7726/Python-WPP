#2. Halloween Party -cutting chocolate into maximum number of pieces
def chocolate(k):
    if k % 2 == 0:
        u = k // 2
        return u ** 2
    else:
        return ((k ** 2) - 1) // 4

# Taking the number of test cases from the user
num_test_cases = int(input("Enter the number of test cases: "))

# Taking values of k from the user
print("Enter the values of k for each test case:")
for i in range(num_test_cases):
    k = int(input(f"Test Case {i+1} - Enter value of k: "))
    print(f"Test Case k = {k}: {chocolate(k)}")

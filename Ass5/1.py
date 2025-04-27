#1. Maximizing XOR
def find_max_xor(L, R):
    max_xor = 0
    
    # Traverse all pairs in the range L to R
    for A in range(L, R + 1):
        for B in range(A, R + 1):
            current_xor = A ^ B
            if current_xor > max_xor:
                max_xor = current_xor
    
    return max_xor

# Get input from the user
L = int(input("Enter the value of L: "))
R = int(input("Enter the value of R: "))

# Find and print the maximum XOR value
max_xor_value = find_max_xor(L, R)
print(f"The maximum XOR value in the range ({L}, {R}) is: {max_xor_value}")
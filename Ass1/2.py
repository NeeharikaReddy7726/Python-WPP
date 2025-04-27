import random

random_list = [random.randint(0, 1) for _ in range(100)]
print("Random List:", random_list)

max_zeros = 0
current_zeros = 0

for num in random_list:
    if num == 0:
        current_zeros += 1
        max_zeros = max(max_zeros, current_zeros)
    else:
        current_zeros = 0  # Reset  1

print("Longest run of zeros:", max_zeros)
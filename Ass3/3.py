def utopian_tree_growth(n):
    height = 1  #int
    for cycle in range(n):
        if cycle % 2 == 0:  # monsooncycle(doubles the height)
            height *= 2
        else:  # summercycle(incr height by 1)
            height += 1
    return height

T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter number of cycles: "))
    print(utopian_tree_growth(N))
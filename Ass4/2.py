import math

def count_square_integers(A, B):
    x = math.ceil(math.sqrt(A))  #smallest int whose sq>= A
    y = math.floor(math.sqrt(B))  #largest int whose sq<= B
    return max(0, y - x + 1)  #non-negative result

T = int(input().strip())  #no.of test cases

for _ in range(T):
    A, B = map(int, input().split())
    print(count_square_integers(A, B))
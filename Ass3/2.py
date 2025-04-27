#To determine whether the entered elemenet is in fibonacci sequence or not
import sys
import math

def is_perfect_square(x):
    """Check if x is a perfect square."""
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(n):
    """Check if n is a Fibonacci number using the mathematical property."""
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

#no.of testcases
T = int(sys.stdin.readline().strip())

#each test case
results = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if is_fibonacci(N):
        results.append("IsFibo")
    else:
        results.append("IsNotFibo")

sys.stdout.write("\n".join(results) + "\n")
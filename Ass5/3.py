#3. Bigger is greater
def next_bigger_permutation(word):
    # Convert the word into a list of characters for easy manipulation
    w = list(word)
    
    # Step 1: Find the pivot (first decreasing element)
    n = len(w)
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    
    if i == -1:
        return "no answer"
    
    # Step 2: Find the smallest character that is greater than w[i]
    j = n - 1
    while w[j] <= w[i]:
        j -= 1
    
    # Step 3: Swap the characters
    w[i], w[j] = w[j], w[i]
    
    # Step 4: Reverse the substring after i
    w = w[:i+1] + w[i+1:][::-1]
    
    return ''.join(w)

def solve():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        w = input().strip()  # Read each word
        print(next_bigger_permutation(w))


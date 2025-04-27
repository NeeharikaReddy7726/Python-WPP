# a)A list consisting of the numbers from 0 to 49.
list_a = [i for i in range(50)]
print(list_a)

# b) A list consisting the squares of the integers 1 to 50.     
list_b = [i**2 for i in range(1, 51)]
print(list_b)

#c)The list ['a', 'bb', 'ccc', 'dddd', ...]
list_c = [chr(97 + i) * (i + 1) for i in range(26)]
print(list_c)
    
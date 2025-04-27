def alternate_capitalize(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i].lower()  # lowercase
        else:
            result += word[i].upper()  #odd-indexed letters
    return result

word = input("Enter a word: ")
formatted_word = alternate_capitalize(word)

print("Formatted word:", formatted_word)
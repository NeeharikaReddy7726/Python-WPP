#3. Pangrams 
sentence=input("Enter the string to be checked:")
def is_pangram(sentence):
   letters = set(sentence.lower()) #coz we want only unique characters from entered string
   alphabet = set('abcdefghijklmnopqrstuvwxyz')
   return alphabet.issubset(letters)

if is_pangram(sentence):
    print("The entered sentence is a pangram.")
else:
    print("The entered sentence is not a pangram.")
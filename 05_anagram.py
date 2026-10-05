word1 = input("Enter first world:")
word2 = input("Enter second world:")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")
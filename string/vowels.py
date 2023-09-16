'''
########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)
'''
inputSentence = input("Enter a sentence: ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split():
    first_vowel_index = 0
    if len(word) > 1:
        for index, char in enumerate(word):
            if char.lower() in vowels:
                first_vowel_index = index
                break
    word = word[first_vowel_index:] + word[:first_vowel_index] + pigLatinKey
    print(word, end=' ')


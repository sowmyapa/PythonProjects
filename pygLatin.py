"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result.
"""
pyg = 'ay'

original = raw_input('Enter a word:\n')

if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=word[0]
    new_word=word[1:len(word)]+first+pyg
    print new_word
else:
    print 'empty'
"""
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack")
should return

"this **** is wack ****"
"""
import string

def censor(text,word):
    list = string.split(text);
    for i in range(len(list)):
        if list[i]==word:
            list[i]="*"*len(word);
    return " ".join(list)
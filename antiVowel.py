"""
Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

Don't count Y as a vowel.
Make sure to remove lowercase and uppercase vowels.
"""
def anti_vowel(text):
    result="";
    for i in range(len(text)):
        if text[i] not in "aeiouAEIOU":
            result=result+text[i];
    return result;
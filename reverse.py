"""
Define a function called reverse that takes a string textand returns that string in reverse.

For example: reverse("abcd") should return "dcba".
"""
def reverse(text):
    output="";
    for i in range(len(text)):
        output=output+text[len(text)-i-1];
    return output;
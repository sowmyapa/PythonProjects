"""
Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.

For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
"""
def product(input):
    output=1;
    for i in range(len(input)):
        output*=input[i];
    return output;
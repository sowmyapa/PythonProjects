"""
Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.

For example, purify([1,2,3]) should return [2].
"""
def purify(numbers):
    result=[];
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            result.append(numbers[i]);
    return result;
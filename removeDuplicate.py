"""
Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1,1,2,2])
should return [1,2].
"""
def remove_duplicates(input):
    output=[];
    for i in range(len(input)):
        if input[i] not in output:
            output.append(input[i]);
    return output;
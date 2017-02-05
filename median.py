"""
The median is the middle number in a sorted sequence of numbers.

Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into [1,3,6,7,12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7,3,1,4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.


"""
def median(input):
    input=sorted(input);
    size=len(input);
    output=0;
    if size%2==0:
        output=(input[size/2]+input[size/2-1])/2.0;
    else:
        output=input[size/2];
    return output;
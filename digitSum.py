"""
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

(Assume that the number you are given will always be positive.)
"""
def digit_sum(x):
    digit_sum=0;
    while(x>0):
        input = x %10;
        x=x/10;
        digit_sum+=input;
    return digit_sum;
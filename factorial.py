"""
To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
"""
def factorial(x):
    factorial=1;
    while x>0:
        factorial*=x;
        x-=1;
    return factorial;
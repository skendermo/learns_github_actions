"""This module does blah blah."""

import time

final_list = []

def factorial(n):
    """bla"""

    time.sleep(.1)

    f = 1

    for i in range (1,n+1):
        f = f * i

    return factorial

def sum_factorial():
    """bla"""

    for i in range(50):

        final_list.append(factorial(i))

    result=sum(final_list)

    print(f"Final SUM is {result}")

    return result

if __name__ == "__main__":

    sum_factorial()

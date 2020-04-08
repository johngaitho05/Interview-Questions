"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""


import math
import random


def compute_pi(n):
    return 4 * simulator(n) / n


def simulator(n):
    p_in_a_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x * x + y * y) < 1:
            p_in_a_circle += 1
    return p_in_a_circle


print('{:0.3f}'.format(compute_pi(100000)))









import math
from math import inf
def true_divide(first, second):
    res = 0
    if second == 0:
        res = math.inf
    else:
        res = first / second
    return res

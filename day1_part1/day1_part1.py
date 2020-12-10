import functools
import operator
import sys


def get_nums_that_sum_to(seq, sum_result=2020):
    """
    This function takes a sequence of numbers
    finds two that sum to sum_result and returns them

    >>> get_nums_that_sum_to([2020,10,0])
    (2020, 0)

    BRUTE FORCE:
    runtime: O(n^2)
    for i, val in enumerate(seq):
        for j, val2 in enumerate(seq):
            if i == j:
                continue
            if val + val2 == sum_result:
                return val, val2

    """

    # runtime: O(n)
    seen = set()
    for val in seq:
        seen.add(val)
        if (sum_result - val) in seen:
            return (sum_result - val), val


def main(args):
    fname = args[-1]
    res = get_nums_that_sum_to([int(line.strip()) for line in open(fname)])
    print(res)
    print(functools.reduce(operator.mul, res))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(sys.argv)

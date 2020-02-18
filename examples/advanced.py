"""Can be called like "python advanced.py" or "mincli advanced.py" """
from mincli import cli, main


@cli
def badd(a_string: str, a_number: int = 10):
    """ Sums a_string and a_number, but we all expect it to fail.

    :param a_string: the first one
    :param a_number: This parameter seems to be
     really good but i don't know tho
    """
    print(a_string + a_number)


@cli
def add(a_number: int, b_number: int = 10):
    print(a_number + b_number)


@cli
def sum_or_multiply(a_number: int, b_number: int = 10, sums: bool = False):
    """ Sums or multiplies a and b

    :param a_number: the first one
    :param b_number: This parameter seems to be
    :param sums: Whether to sum or multiply
    """
    if sums:
        print(a_number + b_number)
    else:
        print(a_number * b_number)


if __name__ == "__main__":
    main()

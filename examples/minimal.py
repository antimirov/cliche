from mincli import cli


@cli
def add(a: int, b: int):
    print(a + b)

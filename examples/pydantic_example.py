from cliche import cli, main
from pydantic import BaseModel


class B(BaseModel):
    b: str


class Item(BaseModel):
    a: str = "good_one"
    b: str


@cli
def print_item(item: Item, b: int = 2):
    print(repr(item), b)


# does not yet work without main()
main()

from collections.abc import Iterable
from typing import Any

VERSION: str

def derangements_range(n: int) -> list[list[int]]: ...
def derangements(iterable: Iterable[Any], k: int) -> list[list[int]]: ...

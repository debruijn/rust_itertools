from collections.abc import Iterable, Sized
from typing import Any

VERSION: str

def derangements_range(n: int) -> list[list[int]]: ...
def derangements(iterable: Sized, k: int | None) -> list[list[Any]]: ...
def permutations(iterable: list[Any], k: int | None) -> list[list[Any]]: ...
def distinct_permutations(iterable: Sized, k: int | None) -> list[list[Any]]: ...
def combinations(iterable: Iterable[Any], k: int) -> list[list[Any]]: ...
def combinations_with_replacement(iterable: Iterable[Any], k: int) -> list[list[Any]]: ...
def pairwise(iterable: Iterable[Any]) -> list[tuple[Any, Any]]: ...
def repeat(n: Any, k: int) -> list[Any]: ...
def powerset(iterable: Iterable[Any]) -> list[list[Any]]: ...

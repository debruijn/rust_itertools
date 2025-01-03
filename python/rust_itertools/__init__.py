from . import _rust_itertools

__all__ = 'VERSION', 'derangements_range', 'derangements', 'permutations', 'distinct_permutations'

# VERSION is set in Cargo.toml
VERSION = _rust_itertools.VERSION
derangements_range = _rust_itertools.derangements_range


def derangements(x, k=None):
    return _rust_itertools.derangements(x, len(x) if k is None else k)


def permutations(x, k=None):
    return _rust_itertools.permutations(x, len(x) if k is None else k)


def distinct_permutations(x, k=None):
    return _rust_itertools.distinct_permutations(x, len(x) if k is None else k)

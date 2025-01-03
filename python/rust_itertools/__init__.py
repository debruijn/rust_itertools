from . import _rust_itertools

__all__ = (
    'VERSION',
    'derangements_range',
    'derangements',
    'permutations',
    'distinct_permutations',
    'combinations',
    'combinations_with_replacement',
    'pairwise',
    'repeat',
    'powerset',
)

# VERSION is set in Cargo.toml
VERSION = _rust_itertools.VERSION
derangements_range = _rust_itertools.derangements_range


def derangements(x, k=None):
    return _rust_itertools.derangements(x, len(x) if k is None else k)


def permutations(x, k=None):
    return _rust_itertools.permutations(x, len(x) if k is None else k)


def distinct_permutations(x, k=None):
    return _rust_itertools.distinct_permutations(x, len(x) if k is None else k)


def combinations(x, k=None):
    return _rust_itertools.combinations(x, len(x) if k is None else k)


def combinations_with_replacement(x, k=None):
    return _rust_itertools.combinations_with_replacement(x, len(x) if k is None else k)


pairwise = _rust_itertools.pairwise
repeat = _rust_itertools.repeat
powerset = _rust_itertools.powerset

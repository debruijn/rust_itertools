from . import _rust_itertools

__all__ = 'VERSION', 'derangements_range', 'derangements', 'permutations', 'distinct_permutations'

# VERSION is set in Cargo.toml
VERSION = _rust_itertools.VERSION
derangements_range = _rust_itertools.derangements_range
derangements = _rust_itertools.derangements
permutations = _rust_itertools.permutations
distinct_permutations = _rust_itertools.distinct_permutations

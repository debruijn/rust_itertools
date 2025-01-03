from rust_itertools import derangements_range
import pytest


def derangements_range_py(n):
    """Yield successive distinct derangements of the range up to *n*.

        >>> sorted(derangements_range_py(3))
        [(1, 2, 0), (2, 0, 1)]

    """
    if n == 2:
        yield 1, 0
    elif n <= 1:
        yield from []
    else:
        lag1 = derangements_range_py(n - 1)
        for lag in lag1:
            for split in range(len(lag)):
                yield lag[0:split] + (n - 1,) + lag[split + 1 :] + (
                    lag[split],
                )

        lag2 = derangements_range_py(n - 2)
        for lag in lag2:
            yield lag + (n - 1, n - 2)
            for k in range(n - 3, -1, -1):
                i = lag.index(k)
                lag = lag[:i] + (k + 1,) + lag[i + 1 :]
                yield lag[:k] + (n - 1,) + lag[k:] + (k,)


@pytest.mark.parametrize("k", [0, 1, 2, 3, 4, 8, 9])
def test_derangement_range(k):
    assert len(derangements_range(k)) == len(list(derangements_range_py(k)))

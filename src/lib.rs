use derangements::{derangements, derangements_range};
use itertools::repeat_n;
use itertools::Itertools;
use pyo3::prelude::*;
use pyo3::pyfunction;
use pyo3::types::PyList;

type T = usize;

#[pyfunction]
#[pyo3(name = "derangements_range")]
fn derangements_range_f(n: T) -> Vec<Vec<T>> {
    derangements_range(n)
}

#[pyfunction]
fn permutations(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().permutations(k).collect_vec()
}

#[pyfunction] // TODO not yet Bound<PyList> due to unique() -> needs NewType that implements Clone, Hash and Eq
fn distinct_permutations(iterable: Vec<T>, k: T) -> Vec<Vec<T>> {
    iterable.into_iter().permutations(k).unique().collect_vec()
}

#[pyfunction]
#[pyo3(name = "derangements")]
fn derangements_f(iterable: Vec<T>, k: T) -> Vec<Vec<T>> {
    derangements(iterable, k)
}

#[pyfunction]
fn combinations(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().combinations(k).collect_vec()
}

#[pyfunction]
fn combinations_with_replacement(iterable: Bound<PyList>, k: T) -> Vec<Vec<Bound<PyAny>>> {
    iterable
        .into_iter()
        .combinations_with_replacement(k)
        .collect_vec()
}

#[pyfunction]
fn pairwise(iterable: Bound<PyList>) -> Vec<(Bound<PyAny>, Bound<PyAny>)> {
    iterable.into_iter().tuple_windows().collect()
}

#[pyfunction]
fn repeat(n: Bound<PyAny>, k: T) -> Vec<Bound<PyAny>> {
    repeat_n(n, k).collect_vec()
}

#[pyfunction]
fn powerset(iterable: Bound<PyList>) -> Vec<Vec<Bound<PyAny>>> {
    iterable.into_iter().powerset().collect_vec()
}

const VERSION: &str = env!("CARGO_PKG_VERSION");

#[pymodule]
pub fn _rust_itertools(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("VERSION", VERSION)?;
    m.add_function(wrap_pyfunction!(permutations, m)?)?;
    m.add_function(wrap_pyfunction!(distinct_permutations, m)?)?;
    m.add_function(wrap_pyfunction!(derangements_f, m)?)?;
    m.add_function(wrap_pyfunction!(combinations, m)?)?;
    m.add_function(wrap_pyfunction!(combinations_with_replacement, m)?)?;
    m.add_function(wrap_pyfunction!(pairwise, m)?)?;
    m.add_function(wrap_pyfunction!(repeat, m)?)?;
    m.add_function(wrap_pyfunction!(powerset, m)?)?;
    m.add_function(wrap_pyfunction!(derangements_range_f, m)?)?;
    Ok(())
}

# rust_itertools
Experimental repo to run Rusts itertools in Python.

## Setup
Initially, this will be mostly used as a proof of concept. This is to investigate the comparisons between:
- rust's itertools functionality vs python's itertools functionality
- rust's itertools functionality vs more_itertools functionality
- new rust functions vs more_itertools functionality
- new rust functions vs new python functions around itertools

# Note
Often, the major goal of porting Rust functionality over to Python is for speed. So far, my initial experimentation
has shown that that gain is very low (or even non-existant) due to 2 main reasons:
- `itertools` is mostly written in C so already quite fast and roughly on par with Rust
- even for `more_itertools` and new python functions: not having to copy over the results back to Python is a major gain
    vs the rust implementations for the type of functions we deal with here. Example: there are over 36 million 
    permutations of the numbers 0 to 9 (incl 9). Generating in Rust and then accessing from Python takes 2.24 seconds
    on my pc, where the CPython itertools takes 0.557 seconds to do the same.

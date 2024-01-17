from pysequence.analysis import compare_sequences

def test_compare_fib_primes():
    n = 50
    fib_primes = compare_sequences.get_intersection_of_sequences(n, 'prime', 'fibonacci')
    assert fib_primes == [2, 3, 5, 15]
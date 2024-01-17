import numpy as np

def even_numbers(n):
    """Return a list of all even numbers up to n
    """
    result = []
    a = 2
    b = 1
    while a < n:
        result.append(a)
        a = a+2
    return result

def fibonacci_numbers(n):
    """Return a list of all Fibonnaci numbers up to n
    """
    result = []
    a, b = 1, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def prime_numbers(n):
    """Return a list of all prime numbers up to n
    """
    integers = np.linspace(1, n, n, dtype=int)
    seive = np.array([True for i in range(n)])
    for i in range(2, n):
        seive[i+i-1::i] = False
    result = integers[seive]
    result = list(result[1:])
    return result

def get_sequence(name):
    """Return the appropriate sequence function given a string name
    """
    if name=='even':
        return even_numbers
    elif name=='fibonacci':
        return fibonacci_numbers
    elif name=='prime':
        return prime_numbers
    else:
        raise ValueError('name should be one of [even, fibonacci, prime]')

if __name__ == "__main__":
    n = 25
    for sequence_name in ['even', 'fibonacci', 'prime']:
        sequence_func = get_sequence(sequence_name)
        print(f'{sequence_name} numbers below {n}: {sequence_func(n)}')
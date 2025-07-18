def factors(n):
    """
    Yield all positive integer factors of `n` in increasing order.

    This generator finds all divisors of `n` by iterating up to the square root of n.
    For each divisor `k`, it yields both `k` and `n // k` if they are distinct.
    If `n` is a perfect square, the square root is yielded only once.
    
    Parameters:
        n (int): The number to factorize. Must be a positive integer.
    
    Yields:
        int: Each factor of `n`, in ascending order.
    """
    small = []
    large = []
    k = 1
    while k * k < n:
        if n % k == 0:
            small.append(k)
            large.append(n // k)
        k += 1
    if k * k == n:
        small.append(k)
    yield from small
    yield from reversed(large)

if __name__=="__main__":
    g = factors(16)
    print(list(g))

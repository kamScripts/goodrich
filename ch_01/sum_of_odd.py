from is_even import is_even
def odds_sum(n):
    """
    Returns the sum of the squares of all the odd positive
    integers smaller than n
    """
    return sum((i**2 for i in range(n)if not is_even(i)))
if __name__=="__main__":
    print(odds_sum(5))
def sum_of_squares(n):
    """
    Returns sum of the squares of all the positive
    integers smaller than n
    """
    return sum((i**2 for i in range(n)))

if __name__=="__main__":
    print(sum_of_squares(5))
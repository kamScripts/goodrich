def arr_product(a, b):
    """
    Returns element-wise products of two lists a and b.
    If lengths differ, raises a ValueError.
    """
    if len(a) != len(b):
        raise ValueError("Both lists must be of the same length")
    return [x * y for x, y in zip(a, b)]
arr=[2,3,4]
arr_b=[5,6,7]
print(arr_product(arr,arr_b))
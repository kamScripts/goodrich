def distinct_check(arr):
    """Check if all elements of the list are distinct."""
    return len(arr)==len(set(arr))
if __name__=="__main__":
    print(distinct_check([1,2,3,3]))
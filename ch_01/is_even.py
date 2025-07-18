def is_even(num):
    """
    check if number is even without arithmetic operators.
    With bitwise & operator as last digit of even number
    binary representation is always 0.
    """
    return (num & 1) == 0

if __name__=="__main__":
    print(is_even(4))
    #0b prefix indicates binary number
    print(int(0b10001010))
    

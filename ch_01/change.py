def make_change(charged, received):
    """
    Give each kind of bill and coin to give back as change for the
    difference between the amount given and amount charged.
    Program returns as few bills and coins as possible.
    
    Params: charged - FLOAT; received - FLOAT
    
    Returns: list of FLOATs representing denominations for the change
    
    TODO: replace floats with int (val*100) to avoid rounding issues
    """
    monetary_vals = [50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

    change={}
    if charged > received:
        raise ValueError('Not enough money received')
    to_return= received-charged
    for val in monetary_vals:
        
        while to_return >= val:
            change[val]=change.get(val, 0) + 1
            # result has to be rounded to two decimal laces as 
            to_return = round(to_return - val, 2)
    return change

if __name__=="__main__":
    change=make_change(45.99, 100.00)
    print(change)
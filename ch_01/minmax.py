def minmax(data):
    res=sorted(data)
    return res[0], res[-1]
if __name__=="__main__":
    print(minmax({3,8,1,35,4,6,21,5}))
    
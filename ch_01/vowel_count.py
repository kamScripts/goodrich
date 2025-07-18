def vowel_count(s):
    hist={}
    count = 0
    for l in s:
        if l in ['a','e','o','i','u','y']:
            hist[l]= hist.get(l,0) +1
            count+=1
    return hist, count
if __name__=="__main__":
    h,c=vowel_count('stara krowa w kropki bordo mieli mordo ieee')
    print(h,c)
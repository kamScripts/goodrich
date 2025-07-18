import random as r

def shuffle(arr):
    current_index=len(arr)
    
    while current_index > 0:
        current_index-=1
        random_index = r.randint(0, current_index)
        print(f'current={current_index}, random={random_index}')
        arr[current_index], arr[random_index] = arr[random_index], arr[current_index]
q=[1,2,3,4,5,6,7,8,9,10]
shuffle(q)
print(q)
import random as r
def choice_rand(data):
    return data[r.randrange(0,len(data))]
q=[2*r.randint(1,100) for _ in range(3)]
if __name__=="__main__":
    print(q, choice_rand(q), sep="\trandom choice: ")
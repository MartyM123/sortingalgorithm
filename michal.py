from numpy import random
a=list(random.randint(10000, size=(10000)))

res=[a.pop(0)]
for item in a:
    for i in range(len(res)):
        if res[i]>=item:
            res.insert(i,item)
            break
    else:
        res.append(item)

print(res)

#odhadovana slozitost (1/2)*(n**3)

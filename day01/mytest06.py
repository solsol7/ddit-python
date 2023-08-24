# 로또
from random import random

arr=list(range(1,45+1))

# arr = []
# for i in range(1,45+1) :
#     arr.append(i)

for i in range(1,10000+1) :
    rnd = int(random()*45)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp

for i in range(0,5+1) :
    print(arr[i], end=" ")


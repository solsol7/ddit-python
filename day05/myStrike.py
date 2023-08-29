# 0~9까지 숫자 중 3개를 골라 문자열 만들기 3 2 5
# 세 숫자를 입력하세요.    1 2 3
# 1 2 3    1S1B
# 세 숫자를 입력하세요.    3 2 5
# 3 2 5    3S0B
# 정답입니다.
from random import random



numArr = []

while len(numArr)!=3 :
    flag = True
    num = int(random()*10)
    
    for i in numArr :
        if(i==num) : flag=False
    if(flag==True) :
        numArr.append(num)

print(numArr)

sCnt = 0;

while(sCnt!=3) :
    sCnt = 0;
    bCnt = 0;
    userNum = input("세 숫자를 입력하세요.(공백으로 구분)")
    userArr = userNum.split(" ")
    
    for i in range(0,2+1) :
        userArr[i] = int(userArr[i])

    for i in numArr :
        for j in userArr :
            if i==j and numArr.index(i)==userArr.index(j) :
                sCnt += 1
            elif i==j and numArr.index(i)!=userArr.index(j) :
                bCnt += 1

    print("{}\t{}S{}B".format(userArr,sCnt,bCnt))

print("정답입니다.")

"""
def ranCom():
    arr = [1,2,3,4,5,6,7,8,9]
    for i in range(100) :
        rnd = int(random()*9)
        a=arr[0]
        arr[0]=arr[rnd]
        arr[rnd]=a
       
    return "{}{}{}".format(arr[0],arr[1],arr[2])

def getS(mine,com):
    cnt = 0
    
    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    if m1==c1 : cnt+=1
    if m2==c2 : cnt+=1
    if m3==c3 : cnt+=1

    return cnt


def getB(mine,com):
    cnt = 0

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    if m1==c2 or m1==c3 : cnt+=1
    if m2==c1 or m2==c3 : cnt+=1
    if m3==c2 or m3==c1 : cnt+=1

    return cnt

com = ranCom()
print("com",com)
while True:
    mine = input("세 숫자를 입력하세요")
    s = getS(mine,com)
    b = getB(mine,com)
    if s==3 :
        print("{}\t{}S{}B\t정답입니다.".format(mine,s,b))
        break
    else :
        print("{}\t{}S{}B".format(mine,s,b))
    
"""
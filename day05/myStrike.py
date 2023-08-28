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
    num = str(int(random()*10))
    
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

    for i in numArr :
        for j in userArr :
            if i==j and numArr.index(i)==userArr.index(j) :
                sCnt += 1
            elif i==j and numArr.index(i)!=userArr.index(j) :
                bCnt += 1

    print("{}\t{}S{}B".format(userArr,sCnt,bCnt))

print("정답입니다.")

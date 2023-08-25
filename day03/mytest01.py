# 1~99 숫자 랜덤 up and down게임
# 숫자를 맞춰보세요 20 => 20 up
# 숫자를 맞춰보세요 50 => 50 down
# 숫자를 맞춰보세요 35 => 35 정답입니다.
from random import random

comNum = int(random()*99+1)

userNum = ""
while userNum!=comNum :
    userNum = int(input("숫자를 맞춰보세요"))
    
    if userNum > comNum :
        print(str(userNum)+"\tdown")
    elif userNum < comNum :
        print(str(userNum)+"\tup")

print(str(userNum)+"\t정답입니다.")
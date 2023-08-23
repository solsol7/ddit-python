# 홀/짝을 선택하시오 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 이김

from random import random

com = ""
rnd = (int)(random()*2)

if rnd%2==0 :
    com = "짝"
else : 
    com = "홀"

user = input("홀/짝을 선택하시오")

print("나 : "+user)
print("컴 : "+com)

if user == com :
    print("결과 : 이김")
else :
    print("결과 : 짐")

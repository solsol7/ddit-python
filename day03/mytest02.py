#가위바위보
#가위/바위/보를 선택하세요. 가위
#나 : 가위
#컴 : 가위
#결과 : 비김
from random import random

rnd = int(random()*3)

if rnd==0 :
    com = "가위"
elif rnd==1 :
    com = "바위"
else :
    com = "보"

user = input("가위/바위/보를 선택하세요.")

result = ""
if user=="가위" and com=="보" or user=="바위" and com=="가위" or  user=="보" and com=="바위" :
    result = "이김"
elif user=="가위" and com=="가위" or user=="바위" and com=="바위" or user=="보" and com=="보" :
    result = "비김"
else :
    result = "짐"

print("나 : "+user)
print("컴 : "+com)
print("결과 : "+result)
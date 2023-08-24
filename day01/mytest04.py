# 첫 수를 입력하세요. 1
# 끝 수를 입력하세요. 4
# 1에서 4까지의 합은 10입니다.

num1 = int(input("첫 수를 입력하세요."))
num2 = int(input("끝 수를 입력하세요."))
sum = 0

for i in range(num1, num2+1) :
    sum += i

print("{}에서 {}까지의 합은 {}입니다.".format(num1, num2, sum))
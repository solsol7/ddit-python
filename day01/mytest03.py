# 첫째 수를 입력하시오. 7
# 둘째 수를 입력하시오. 8
# 7과 8의 합은 15입니다.

num1 = input("첫째 수를 입력하시오.")
num2 = input("둘째 수를 입력하시오.")

sum = int(num1)+int(num2)

print(num1+"과 "+num2+"의 합은 "+str(sum)+"입니다.")

print("{}과 {}의 합은 {}입니다.".format(num1,num2,sum))
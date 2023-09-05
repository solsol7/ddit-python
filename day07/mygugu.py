
str = ""
for ii in range(2,9+1) :
    i = 10-ii
    if i%2==0 : 
        for j in range(1,9+1) :
            str += "{}*{}={}".format(i, j, i*j)
            str+="\n"
        str += "\n"


print(str)


def showdan(dan):
    print("{}*{}={}".format(dan,1,1*dan))
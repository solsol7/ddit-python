def showAllGugudan():
    for i in range(1,9+1) :
        print(str(i)+"단")
        for j in range(1,9+1) :
            print("{}*{}={}".format(i,j,i*j))
        print()

showAllGugudan()
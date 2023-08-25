class Biden :
    def __init__(self):
        self.doller = 10
    def reelected(self):
        self.doller += 10

class Xi :
    def __init__(self):
        self.cnt_nuclear = 200
    def war(self,cnt):
        self.cnt_nuclear -= cnt

class Musk :
    def __init__(self):
        self.cnt_spaceX = 100
    def twitter(self,cnt):
        self.cnt_spaceX += cnt


class Kyeongseok(Biden, Xi, Musk):
    def __init__(self):
       Biden.__init__(self)
       Xi.__init__(self)
       Musk.__init__(self)
       self.weight = 3.3
    def now(self):
        self.weight = 80


if __name__ == '__main__':
    ky = Kyeongseok()
    
    print("doller",ky.doller)
    print("cnt_nuclear",ky.cnt_nuclear)
    print("cnt_spaceX",ky.cnt_spaceX)
    print("weight",ky.weight)
    
    ky.reelected()
    ky.war(9)
    ky.twitter(10)
    ky.now()
    
    print()
    print("doller",ky.doller)
    print("cnt_nuclear",ky.cnt_nuclear)
    print("cnt_spaceX",ky.cnt_spaceX)
    print("weight",ky.weight)
    
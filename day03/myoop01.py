# Python으로 자바 - day02 OOP 똑같이 구현
# 한 소스에 클래스 놓고 상속받는 소스 놓고.. 쭉 해도 됨

class Animal : 
    def __init__(self):
        self.flagLife=True
    
    def die(self):
        self.flagLife = False


class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.job = "백수"
    
    def chippo(self, job):
        self.job = job

if __name__ == '__main__':
    hum = Human()
    
    print(hum.flagLife)
    print(hum.job)
    
    hum.die()
    hum.chippo("프로그래머")
    
    print(hum.flagLife)
    print(hum.job)

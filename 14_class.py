class monster :
    hp = 100;
    alive = True;

    def demage(self , attack): #self는 상위의 부모 클래스의 객체 명시
        self.hp = self.hp - attack

        if self.hp < 0 :
            self.alive = False;

    def status_check(self):
        if self.alive :
            print("살았습니다!")
        else:
            print("죽었습니다!!")

m1 = monster()
m1.demage(500)
m1.status_check()

m2 = monster()
m2.demage(50)
m2.status_check()
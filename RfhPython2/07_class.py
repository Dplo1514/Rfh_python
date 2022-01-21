class Monster():
    hp = 100
    alive = True

    def damege(self , attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def Monster_Check(self):
        if self.alive:
            print("살아있다.")
        else:
            print("죽었습니다.")

m = Monster()
m.damege(60)
m.Monster_Check()

m.damege(100)
m.Monster_Check()

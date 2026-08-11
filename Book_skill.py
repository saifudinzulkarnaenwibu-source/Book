from Kertas import player, goblin, cerbe
class Skill:
    def __init__(self,nama,dmg,mana,type):
        self.nama = nama
        self.dmg = dmg
        self.mana = mana
        self.type = type
class Gerakan(Skill):
    def __init__(self, nama, dmg, mana, type):
        super().__init__(nama, dmg, mana, type)
    def gerak(self,penarget,target):
        if penarget.mana >= self.mana:
            penarget.mana -= self.mana
            if self.type == "p":
                hasil = int(self.dmg*penarget.atk)* (100-target.defp) // 100
            else:
                hasil = int(self.dmg*penarget.atk) * (100-target.defm) // 100
            target.hp -= hasil
            print(f"{penarget.nama} Berhasil melancarkan {self.nama} Memberi {hasil}")
smash = Gerakan("Smash",1,0,"p")
fireball = Gerakan("Fireball",1.5,50,"m")
lightning = Gerakan("Lightning",2,100,"m")
explosion = Gerakan("explosion",3,200,"m")
print(cerbe.hp)
lightning.gerak(player,cerbe)
print(cerbe.hp)
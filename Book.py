class Karakter:
    def __init__(self,nama,hp_a,atk,defen):
        self.nama = nama
        self.atk = atk
        self.hp_a = hp_a
        self.hp = hp_a      
        self.defen = defen
    def serang(self):
        print(f"menyerang")
    def menyerang(self,target):
        hasil = max(0,self.atk*(100-target.defen)//100)
        self.serang()
        target.hp -= hasil
        print(f"{self.nama} berhasil memberi {hasil} DMG ")
class inventory:
    def __init__(self):
        self.item = []
class pemain(Karakter):
    def __init__(self, nama, hp_a, atk,defen):
        super().__init__(nama, hp_a, atk,defen)
        self.tas = inventory()
    def serang(self):
        print(f"{self.nama} menyerang pake otak")
class musuh(Karakter):
    def serang(self):
        print(f"{self.nama} menyerang pake kekuatan")
class boss(Karakter):
    def serang(self):
        print(f"{self.nama} menyerang pake bomb")
player = pemain("Udin",200,100,30)
goblin = musuh("Goblin",300,50,0)
cerbe = boss("Cerberus",400,100,50)
player.menyerang(cerbe)
goblin.menyerang(player)
cerbe.menyerang(player)
player.tas.item.append("Book")
print(cerbe.defen)
print(player.tas.item[0])
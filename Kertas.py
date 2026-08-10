from abc import ABC, abstractmethod
from Book_skill import *
class Karakter(ABC):
    def __init__(self,nama,hp_a,atk,defen):
        self.nama = nama
        self.atk = atk
        self.hp_a = hp_a
        self._hp = hp_a      
        self.defen = defen
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,nilai):
        self._hp = max(0,min(nilai,self.hp_a))
    @abstractmethod
    def serang(self):
        print(f"menyerang")
    def menyerang(self,target):
        hasil = max(0,self.atk*(100-target.defen)//100)
        self.serang()
        target.hp -= hasil
        print(f"{self.nama} berhasil memberi {hasil} DMG ")
class Heal:
    def menyembuhkan(self):
        heal = int(self.hp * 0.3)
        self.hp += heal
        print(f"{self.nama} berhasil menyembuhkan {heal} HP")
class inventory:
    def __init__(self):
        self.item = []
    def tambah(self,barang):
        self.item.append(barang)
    def buang(self,barang):
        self.item.remove(barang)
class Skill:
    def __init__(self):
        self.skillp = []
    def tambah(self,barang):
        self.skillp.append(barang)
    def buang(self,barang):
        self.skillp.remove(barang)
class pemain(Karakter,Heal):
    def __init__(self, nama, hp_a, atk,defen):
        super().__init__(nama, hp_a, atk,defen)
        self.tas = inventory()
        self.skill = Skill()
    def serang(self):
        print(f"{self.nama} menyerang pake {self.skill}")
class musuh(Karakter):
    def __init__(self, nama, hp_a, atk,defen):
        super().__init__(nama, hp_a, atk,defen)
        self.skill = Skill()
    def serang(self):
        print(f"{self.nama} menyerang pake {self.skill}")
class boss(Karakter):
    def __init__(self, nama, hp_a, atk,defen):
        super().__init__(nama, hp_a, atk,defen)
        self.skill = Skill()
    def serang(self):
        print(f"{self.nama} menyerang pake {self.skill}")
player = pemain("Udin",300,100,30)
goblin = musuh("Goblin",300,50,0)
cerbe = boss("Cerberus",400,500,50)
player.skill.tambah(shot)
print(player.skill.skillp[0].nama)
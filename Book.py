from abc import ABC, abstractmethod
class Karakter(ABC):
    def __init__(self,nama,hp_a,atk,defen):
        self.nama = nama
        self.atk = atk
        self.hp_a = hp_a
        self._hp = hp_a      
        self.defen = defen
        self.skill = []
    def tambah
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
class heal:
    def menyembuhkan(self):
        heel = int(self.hp * 0.3)
        self.hp += heel
        print(f"{self.nama} berhasil menyembuhkan {heel} HP")
class inventory:
    def __init__(self):
        self.item = []
    def tambah_i(self,barang):
        self.item.append(barang)
    def buang_i(self,barang):
        self.item.remove(barang)
class pemain(Karakter,heal):
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
player = pemain("Udin",300,100,30)
goblin = musuh("Goblin",300,50,0)
cerbe = boss("Cerberus",400,500,50)
player.menyerang(cerbe)
goblin.menyerang(player)
cerbe.menyerang(player)
print(player.hp)
player.hp += 500
print(player.hp)
print(cerbe.defen)
player.menyembuhkan()
print(pemain.mro())
player.tas.tambah_i("Baju")
player.tas.tambah_i("Helm")
print(player.tas.item)
player.tas.buang_i("Helm")
print(player.tas.item)
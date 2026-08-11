class Karakter():
    def __init__(self,nama,hp_a,atk,defp,defm):
        self.nama = nama
        self.atk = atk
        self.hp_a = hp_a
        self._hp = hp_a      
        self.defp = defp
        self.defm = defm
    @property
    def persen_hp(self):
        return f"{self._hp // self.hp_a *100}%"

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,nilai):
        self._hp = max(0,min(nilai,self.hp_a))
    def menyerang(self,target):
        hasil = max(0,self.atk*(100-target.defp)//100)
        target.hp -= hasil
        print(f"{self.nama} berhasil memberi {hasil} DMG ")
    def __str__(self):
        return self.nama
class inventory:
    def __init__(self):
        self.item = []
    def tambah(self,barang):
        self.item.append(barang)
    def buang(self,barang):
        self.item.remove(barang)
class pemain(Karakter):
    def __init__(self,nama,hp_a,atk,defp,defm,mana):
        super().__init__(nama, hp_a, atk,defp,defm)
        self.tas = inventory()
        self.mana = mana
class musuh(Karakter):
    pass
class boss(Karakter):
    pass
player = pemain("Udin",300,100,30,0,200)
goblin = musuh("Goblin",300,50,0,0)
cerbe = boss("Cerberus",400,500,50,0)
print(player.persen_hp)
print(player)
print(player.hp)
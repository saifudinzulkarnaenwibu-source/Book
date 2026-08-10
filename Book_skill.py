class sskill:
    def __init__(self,nama,dmg,pakai,mana):
        self.nama = nama
        self.dmg = dmg
        self.pemakaian = pakai
        self.mana = mana
class skill_pemain(sskill):
    def __init__(self,nama,dmg,pakai,mana,heal):
        super().__init__(nama,dmg,pakai,mana) 
        self.heal = heal
shot = sskill("Shot",1.6,100,50)
heal = skill_pemain("Heal",0,5,50,0.3)
hit = sskill("Hit",1,100,0)

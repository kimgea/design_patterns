


class RougeCap(object):
    def get_armor(self):
        return 5

class WarriorHelmet(object):
    def get_armor(self):
        return 15
    
class Dagger(object):
    def get_attack(self):
        return 20
    
class Sword(object):
    def get_attack(self):
        return 10


class NPC(object):
    def __init__(self,items=[]):
        self.items = items
    
    def get_armor(self):
        sum = 0
        for item in self.items:
            try:
                attack = item.get_armor()
                sum+=attack
            except:pass
        return sum
    
    def get_attack(self):
        sum = 0
        for item in self.items:
            try:
                armor = item.get_attack()
                sum+=armor
            except:pass
        return sum
    
    
class NPCBuilder(object):
    @staticmethod
    def warrior():
        return NPC([WarriorHelmet(),Sword()])
    
    @staticmethod
    def rouge():
        npc = NPC()
        npc.items.append(RougeCap())
        npc.items.append(Dagger())
        return npc
    
    
    
    
warrior = NPCBuilder.warrior()  
rouge = NPCBuilder.rouge()
print ("Rouge Attack: {} - Armor: {}".format(rouge.get_attack(), rouge.get_armor()))
print ("Warrior Attack: {} - Armor: {}".format(warrior.get_attack(), warrior.get_armor()))  
    

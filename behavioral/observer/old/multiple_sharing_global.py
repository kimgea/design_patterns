"""
Fast and dirty, could ofcourse be designed better.

Just a example for how multiple subjects with the same list of observers could be done
"""

import math

class Subject:
    """

    """
    _observers = set([])

    def __init__(self):
        self.running = False
        self.remove = set([])

    def register(self, observer):
        if self.running:
            self.remove.add(observer)               # WTF
        else:
            self._observers.add(observer)

    def unregister(self, observer):
        if self.running:
            self.remove.add(observer)
        else:
            self._observers.remove(observer)

    def notefy(self):
        self.running = True
        for observer in self._observers:
            observer.update(self)
        self.running = False
        for observer in self.remove:
            self.unregister(observer)


class Observer:
    """
    NOTE: Observer could be exhanged with registering callback in subject
    """
    def observe(self, subject):
        subject.register(self)

    def update(self, subject):
        pass


class Sound(Subject):
    def notefy_sound(self, coordinate, range):
        self.coordinate = coordinate
        self.range = range
        self.notefy()

class Aura(Subject):
    def notefy_aura(self, coordinate, range, damage):
        self.coordinate = coordinate
        self.range = range
        self.damage = damage
        self.notefy()



class Player(Subject):
    def __init__(self, name, coordinate):
        super(Player, self).__init__()
        self.coordinate = coordinate
        self.name = name
        self.sound = Sound()
        self.aura = Aura()

    def speak(self):
        print("{0} is speaking".format(self))
        self.sound.notefy_sound(self.coordinate, 10)

    def shout(self):
        print("{0} is shouting".format(self))
        self.sound.notefy_sound(self.coordinate, 50)

    def emit_aura(self):
        # suposed to be called every second or so
        print("{0} is emiting damage aura".format(self))
        self.aura.notefy_aura(self.coordinate, 10, 100)

    def kill(self, object):
        print("{0} is atacking {1}".format(self,object))
        object.destroy(self)

    def __str__(self):
        return self.name



class Enemy(Observer):
    def __init__(self, name, coordinate):
        self.name = name
        self.coordinate = coordinate
        self.hp = 150

    def destroy(self, destroyer):
        print("{0} was killed by {1}".format(self, destroyer))
        destroyer.unregister(self)

    def update_sound(self, subject):
        dist = math.hypot(self.coordinate[0] - subject.coordinate[0],
                          self.coordinate[1] - subject.coordinate[1])
        if dist <= subject.range:
            print("{0} heard a noise".format(self))

    def update_aura(self, subject):
        dist = math.hypot(self.coordinate[0] - subject.coordinate[0],
                          self.coordinate[1] - subject.coordinate[1])
        if dist <= subject.range:
            self.hp -= subject.damage
            print("{0} damaged {1} by aura".format(self, subject.damage))

        if self.hp < 0:
            print("{0} was killed by aura damage".format(self))
            subject.unregister(self)

    def update(self, subject):
        if type(subject) is Sound:
            self.update_sound(subject)
        elif type(subject) is Aura:
            self.update_aura(subject)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



def main():
    player = Player("Reskin",[0,0])

    enemy1 = Enemy("Troll",[10,10])
    enemy1.observe(player)
    enemy2 = Enemy("Giant",[3,3])
    player.register(enemy2)

    player.speak()
    print("_________________")
    player.shout()
    print("_________________")
    print("Current observers",player._observers)
    print("_________________")

    player.emit_aura()
    player.emit_aura()

    print("_________________")
    print("Current observers",player._observers)
    print("_________________")

    player.kill(enemy1)

    print("_________________")
    print("Current observers",player._observers)
    print("_________________")

if __name__ == "__main__":
    main()
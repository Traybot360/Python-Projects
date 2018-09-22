class Creature:
  def __init__(self, name, hp, attack):
    self.hp = hp
    self.attack = attack
    self.name = name[:1].upper() + name[1:].lower()
    print(self.name + " created.")
  def show(self):
    print(self.name + " hp = "+ str(self.hp) + ".")
    print(self.name + " attack = "+ str(self.attack) + ".")
  def fight(self, target):
    print(self.name + " attacks the " + target.name + " and deals " + str(self.attack) + " damage." )
    target.hp -= self.attack

class Dragon(Creature):
  def __init__(self, name, hp, attack, acid):
    self.acid = acid
    super().__init__(name,hp,attack)
  def show(self):
    super().show()
    print(self.name + " acid = "+ str(self.acid) + ".")
  def fight(self, target):
    super().fight(target)
  def fire(self, target):
    print(self.name + " burns the " + target.name + " and deals " + str(self.acid) + " damage." )
    target.hp -= self.acid

class Knight(Creature):
  def __init__(self, name, hp, attack, potion):
    self.potion = potion
    super().__init__(name,hp,attack)
  def show(self):
    super().show()
    print(self.name + " potion = "+ str(self.potion) + ".")
  def fight(self, target):
    super().fight(target)
  def heal(self, target):
    print(self.name + " uses potion to heal the " + target.name + " and heals " + str(self.potion) + " hp." )
    target.hp += self.potion

if __name__ == "__main__":
  d = Dragon("smaug",300,10,20)
  print("-------------")
  d.show()
  print("-------------")
  a = Knight("arthur",50,5,20)
  g = Knight("galahad",20,5,20)
  print("-------------")
  a.show()
  g.show()
  print("-------------")
  d.fight(a)
  d.fight(g)
  print("-------------")
  a.show()
  g.show()
  print("-------------")
  d.fire(a)
  print("-------------")
  a.show()
  print("-------------")
  g.heal(a)
  print("-------------")
  a.show()

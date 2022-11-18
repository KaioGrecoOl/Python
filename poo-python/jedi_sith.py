from character import Character
from random import choice
from light_saber import LightSaber


class Sith(Character):
  def __init__(self, name, specy, weight, height, hp):
      super().__init__(name, specy, weight, height, hp)
      self.lightsaber = LightSaber("Red", 40)

  def attack(self, character):
    if not character.defense():
        character.set_hp(self.lightsaber.force)

  def speak(self):
      return "Come to the dark side of the force"

  
class Jedi(Character):
  def __init__(self, name, specy, weight, height, hp):
      super().__init__(name, specy, weight, height, hp)
      self.lightsaber = LightSaber("Green", 20)

  def defense(self):
      defe = choice([True, False])
      if defe:
        print(f"{self.name} defense")
        return defe

  def counterattack(self, character):
      character.set_hp(self.lightsaber.force)

  def speak(self):
      return "May the force be with you!"

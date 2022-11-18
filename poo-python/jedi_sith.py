from character import Character

class Jedi(Character):
  def __init__(self, name, specy, weight, height, hp):
      super().__init__(name, specy, weight, height, hp)
      self.lightsaber = "Green lightsaber"


class Sith(Character):
  def __init__(self, name, specy, weight, height, hp):
      super().__init__(name, specy, weight, height, hp)
      self.lightsaber = "Red lightsaber"
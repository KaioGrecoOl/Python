from character_interface import CharachterInterface


class Character:
  def __init__(self, name, specy, weight, height, hp):
      self.name = name
      self.specy = specy
      self.__weight = weight
      self.__height = height
      self.__hp = hp
  
  def get_weight(self):
    return self.__weight

  def set_weight(self, new_weight):
    self.__weight = new_weight

  def get_height(self):
    return self.__height

  def set_height(self, new_height):
    self.__height = new_height


  def get_hp(self):
    return self.__hp

  def set_hp(self, damage):
    self.hp -= damage

  def speak(self):
    return "I speak!"

  
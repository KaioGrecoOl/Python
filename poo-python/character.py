class Character:
  def __init__(self, name, specy, weight, height, hp):
      self.name = name
      self.specy = specy
      self.__weight = weight
      self.__height = height
      self.__hp = hp
  
  def get_weight(self):
    return self.__weight

  def get_height(self):
    return self.height
  
  def get_weight(self):
    return self.__weight

  def get_hp(self):
    return self.__hp

  
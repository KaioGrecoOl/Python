from abc import ABC, abstractclassmethod

class CharachterInterface(ABC):

  @abstractclassmethod
  def speak(self):
    raise NotImplementedError
from character import Character
from jedi_sith import Jedi, Sith


character_1 = Character("Padmé", "Humana", 50, 165, 40)
character_2 = Jedi("Luke", "Humana", 60, 170, 200)
character_3 = Sith("Darth Vader", "Humana", 60, 200, 200)


print("Battle Begun ⚔️")
print("-----------------")

while character_3.get_hp() > 0:
    
  print(f" -> {character_2.name}; hp:{character_2.get_hp()}")
  print(f" -> {character_3.name}; hp:{character_3.get_hp()}")
  print("-----------------")
  character_3.attack(character_2)

  if character_2.get_hp() > 0:
    character_2.counterattack(character_3)
  else:
    print("Siths wins")
    break

else:
  print("Jedi wins")



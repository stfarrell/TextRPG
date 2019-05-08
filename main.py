import math
import random
import time


def wait():
  time.sleep(1)


#Define Player class#
class Player:
  def __init__(self, name, hp, attack, defense, speed, gold, exp, accuracy, crit, maxhp, weapon_equipped, armor_equipped, player_class):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.gold = gold
    self.exp = exp
    self.accuracy = accuracy
    self.crit = crit
    self.lvl = 1
    self.monlvl = 0
    self.maxhp = maxhp
    self.weapon_equipped = False
    self.armor_equipped = False
    self.player_class = player_class

#Retrieve name from user#
player_name = input("\nYO, WHAT'S YOUR NAME?!\n")


#Declare "empty" character
da_player = None
warrior = Player(player_name + " " + "The Warrior", 10, 8, 3, 5, 50, 0, 90, 2, 10, False, False, "warrior")
assassin = Player(player_name + " " + "The Assassin", 8, 7, 1, 8, 0, 0, 90, 25, 8, False, False, "assassin")
thief = Player(player_name + " " + "The Thief", 7, 6, 2, 8, 0, 0, 90, 4, 7, False, False, "thief")
inventory = []
inventory_item_names = []


def apply_bonuses(item):
  da_player.maxhp += item.hp_bonus
  da_player.attack += item.attack_bonus
  da_player.defense += item.defense_bonus
  da_player.speed += item.speed_bonus
  da_player.crit += item.crit_bonus
  print("\n{} has been equipped!\n".format(item.name))
  Town_Menu()
  
def take_away_bonues(item):
  da_player.maxhp -= item.hp_bonus
  da_player.attack -= item.attack_bonus
  da_player.defense -= item.defense_bonus
  da_player.speed -= item.speed_bonus
  da_player.crit -= item.crit_bonus
  print("\n{} has been unequipped!\n".format(item.name))
  Town_Menu()


def equip_weapon():
  if da_player.weapon_equipped == True:
    print("\nYou can only have one weapon equipped at a time!\n")
    open_inventory()
  else:
    weapon_to_equip = input("\nWhich weapon would you like to have equipped?\n")
    if (weapon_to_equip.lower() == "stick") and ("stick" in inventory_item_names):
      stick.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(stick)
    elif (weapon_to_equip.lower() == "wooden sword") and ("wooden sword" in inventory_item_names):
      wooden_sword.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(wooden_sword)
    elif (weapon_to_equip.lower() == "iron sword") and ("iron sword" in inventory_item_names):
      iron_sword.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(iron_sword)
    elif (weapon_to_equip.lower() == "steel sword") and ("steel sword" in inventory_item_names):
      steel_sword.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(steel_sword)
    elif (weapon_to_equip.lower() == "assassin's dagger") and ("assassin's dagger" in inventory_item_names):
      assassin_dagger.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(assassin_dagger)
    elif (weapon_to_equip.lower() == "lightsaber") and ("lightsaber" in inventory_item_names):
      lightsaber.equipped = True
      da_player.weapon_equipped = True
      apply_bonuses(lightsaber)
    else:
      print("\nYou don't have that!\n")
      equip_weapon()
  
def unequip_weapon():
  if da_player.weapon_equipped == False:
    print("\nYou don't have a weapon equipped!\n")
    open_inventory()
  else:
    for weapon in inventory:
      if (weapon.equipped == True) and (weapon.item_type == "weapon"):
        weapon_to_unequip = weapon.name
    option = input("\nAre you sure you want to unequip {}?\n(1) Yes\n(2) No\n".format(weapon.name))
    if option == "1":
      da_player.weapon_equipped = False
      weapon.weapon_equipped = False
      take_away_bonues(weapon)
    if option == "2":
      open_inventory()
  
def equip_armor():
  if da_player.armor_equipped == True:
    print("\nYou can only have one piece of armor equipped at a time!\n")
    open_inventory()
  else:
    armor_to_equip = input("\nWhich armor would you like to have equipped?\n")
    if (armor_to_equip.lower() == "red cloak") and ("red cloak" in inventory_item_names):
      red_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(red_cloak)
    elif (armor_to_equip.lower() == "blue cloak") and ("blue cloak" in inventory_item_names):
      blue_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(blue_cloak)
    elif (armor_to_equip.lower() == "green cloak") and ("green cloak" in inventory_item_names):
      green_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(green_cloak)
    elif (armor_to_equip.lower() == "yellow cloak") and ("yellow cloak" in inventory_item_names):
      yellow_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(yellow_cloak)
    elif (armor_to_equip.lower() == "black cloak") and ("black cloak" in inventory_item_names):
      black_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(black_cloak)
    elif (armor_to_equip.lower() == "invisibility cloak") and ("invisibility cloak" in inventory_item_names):
      invisiblity_cloak.equipped = True
      da_player.armor_equipped = True
      apply_bonuses(invisiblity_cloak)
    else:
      print("\nYou don't have that!\n")
      equip_armor()


def unequip_armor():
  if da_player.armor_equipped == False:
    print("\nYou don't have a weapon equipped!\n")
    open_inventory()
  else:
    for armor in inventory:
      if (armor.equipped == True) and (armor.item_type == "armor"):
        armor_to_unequip = armor.name
    option = input("\nAre you sure you want to unequip {}?\n(1) Yes\n(2) No\n".format(armor.name))
    if option == "1":
      da_player.armor_equipped = False
      armor.equipped = False
      take_away_bonues(armor)
    if option == "2":
      open_inventory()



def open_inventory():
  print("\n~~INVENTORY~~\n")
  for item in inventory:
    print(item.name + " ~ Equipped: {}".format(item.equipped))
  option = input("\n(1) Equip Item\n(2) Unequip Item\n(3) Back to Town\n")
  if option == "1":
    which_item = input("\nWhich type of item would you like to equip?\n(1) Weapon\n(2) Armor\n")
    if which_item == "1":
      equip_weapon()
    elif which_item == "2":
      equip_armor()
    else:
      print("\nWHAT!?\n")
      open_inventory()
  if option == "2":
    which_item = input("\nWhich type of item would you like to unequip?\n(1) Weapon\n(2) Armor\n")
    if which_item == "1":
      unequip_weapon()
    elif which_item == "2":
      unequip_armor()
    else:
      print("\nWHAT!?\n")
      open_inventory()
  elif option == "3":
    Town_Menu()
  

#Create Monster class#
class Monster:
  def __init__(self, level):
    monster_name = ["Slime", "Zombie", "Goblin", "Troll", "Ghost"]
    self.name = monster_name[random.randint(0,len(monster_name)-1)]
    self.hp = math.floor(level) + random.randint(5,9)
    self.attack = math.floor(level) + random.randint(3,5)
    self.defense = math.floor(level) + random.randint(3,5)
    self.speed = math.floor(level) + random.randint(3,5)
    self.gold = math.floor(level) + random.randint(2,5)
    self.exp = math.floor(level) + random.randint(10,20)
    self.accuracy = math.floor(level) + random.randint(75,99)
    self.crit = math.floor(level) + random.randint(0,3)

sassy_remarks = ["I had a scholarship to Berkley!", "I am simply misunderstood!", "I have kids!", "I just finished paying off my loans!", "Why do you keep attacking us?!", "Just wait...", "Help, I need somebody!", "Help, not just anybody!", "Help, ya know I need someone!", "HEEELLLLPPPP!!!!", "I just want to go to work!", "Hankuna matata...", "You haven't seen the last of me!", "YOU..you...bleh", "Why have you forsaken us?!", "I just needed directions to the library!"]


#Create the Store Items class and initialize all the different weapons, armor, and potions!
class Store_Item():
    def __init__(self, name, cost, hp_bonus, attack_bonus, defense_bonus, speed_bonus, crit_bonus, gold_bonus, exp_bonus, equipped, item_type):
      self.name = name
      self.cost = cost
      self.hp_bonus = hp_bonus
      self.attack_bonus = attack_bonus
      self.defense_bonus = defense_bonus
      self.speed_bonus = speed_bonus
      self.crit_bonus = crit_bonus
      self.gold_bonus = gold_bonus
      self.exp_bonus = exp_bonus
      self.equipped = False
      self.item_type = item_type
    
stick = Store_Item("Stick", 5, 0, 1, 0, 0, 0, 0, 0, False, "weapon")
wooden_sword = Store_Item("Wooden Sword", 10, 0, 3, 0, 0, 0, 0, 0, False, "weapon")
iron_sword = Store_Item("Iron Sword", 15, 0, 5, 0, 0, 0, 0, 0, False, "weapon")
steel_sword = Store_Item("Steel Sword", 25, 0, 9, 0, 0, 0, 0, 0, False, "weapon")
assassin_dagger = Store_Item("Assassin's Dagger", 40, 0, 8, 0, 0, 25, 0, 0, False, "weapon")
light_saber = Store_Item("Lightsaber", 100, 0, 20, 0, 0, 0, 0, 0, False, "weapon")
weapons_list = [stick, wooden_sword, iron_sword, steel_sword, assassin_dagger, light_saber]


red_cloak = Store_Item("Red Cloak", 20, 5, 5, 0, 0, 0, 0, 0, False, "armor")
blue_cloak = Store_Item("Blue Cloak", 20, 0, 5, 5, 0, 0, 0, 0, False, "armor")
green_cloak = Store_Item("Green Cloak", 20, 0, 0, 0, 0, 0, 5, 5, False, "armor")
yellow_cloak = Store_Item("Yellow Cloak", 20, 0, 0, 0, 5, 0, 5, 0, False, "armor")
black_cloak = Store_Item("Black Cloak", 20, 0, 5, 0, 0, 0, 5, 0, False, "armor")
invisiblity_cloak = Store_Item("Invisibility Cloak", 50, 0, 0, 0, 10, 15, 0, 0, False, "armor")
armor_list = [red_cloak, blue_cloak, green_cloak, yellow_cloak, black_cloak, invisiblity_cloak]


health_potion = Store_Item("Health Potion", 10, 0, 0, 0, 0, 0, 0, 0, False, "potion")
attack_potion = Store_Item("Attack Potion", 10, 0, 2, 0, 0, 0, 0, 0, False, "potion")
defense_potion = Store_Item("Defense Potion", 10, 0, 0, 2, 0, 0, 0, 0, False, "potion")
speed_potion = Store_Item("Speed Potion", 10, 0, 0, 0, 2, 0, 0, 0, False, "potion")
crit_potion = Store_Item("Crit Potion", 10, 0, 0, 0, 0, 5, 0, 0, False, "potion")
gold_potion = Store_Item("Gold Potion", 10, 0, 0, 0, 0, 0, 1.2, 0, False, "potion")
exp_potion = Store_Item("EXP Potion", 10, 0, 0, 0, 0, 0, 0, 1.2, False, "potion")
potions_list = [health_potion, attack_potion, defense_potion, speed_potion, crit_potion, gold_potion, exp_potion]







  
    
#User picks their character (warrior, assassin or thief)
def choose_character():
  wait()
  character_choice = input("\nWelcome {}!\nWhat type of character will you play as?\n\nThe Warrior is an all around good fighter. Solid offense, solid defense, and decent speed.\n\nThe Assassin is very quick and has a high critical hit chance, but low defense.\n\nThe Thief is not the strongest of characters but has a chance to steal gold on each hit!\n\nWho will you play as?\n(1) Warrior\n(2) Assassin\n(3) Thief\n".format(player_name))
  if character_choice == "1":
    chosen_character = warrior
  elif character_choice == "2":
    chosen_character = assassin
  elif character_choice == "3":
    chosen_character = thief
  else:
    print("\nI don't understand!")
    chosen_character = choose_character()
  print("\nWelcome {}!\n".format(chosen_character.name))  
  return chosen_character
    

  
#Call the choose character function!
da_player = choose_character()






#Create the Town Menu
def Town_Menu():
  wait()
  option = input("\nWelcome to Town! Here you can venture out to fight monsters, visit our resident healer for 3 gold, head to the store to buy more gear, or check your stats with the trainer.\nWhich would you like to do now?\n(1) Fight Monsters!\n(2) Heal my Wounds! (3 gold)\n(3) Buy Stuff at The Store!\n(4) Check my Stats!\n(5) Open inventory!\n")
  
  if option == "1":
    fight()
  if option == "2":
    if da_player.gold < 3:
      print("\nYou don't have enough money for healing!\n")
      Town_Menu()
    else:
      da_player.gold -= 3
      da_player.hp = da_player.maxhp
      print("\nYou have been fully healed!\n")
      print("\nThank you for your business! We hope you get injured again soon!\n")
      Town_Menu()
  if option == "3":
    store()
  if option == "4":
    wait()
    print("\nHEALTH POINTS = {}\nATTACK = {}\nDEFENSE = {}\nSPEED = {}\nACCURACY = {}\nCRIT CHANCE = {}\nLVL = {}\nEXP = {}\ngold = {}".format(da_player.hp, da_player.attack, da_player.defense, da_player.speed, da_player.accuracy, da_player.crit, da_player.lvl, da_player.exp, da_player.gold))
    Town_Menu()
  if option == "5":
    open_inventory()
  else:
    print("\nI don't understand!")
    Town_Menu()


def store():
  
  def buy_again():
    option = input("\nWould you like to purchase anything else?\n(1) Yes\n(2) No\n")
    if option == "1":
      store()
    elif option == "2":
      Town_Menu()
    else:
      print("\nWHAT?!\n")
      buy_again()
  
  def money_check(item):
      if da_player.gold < item.cost:
        print("\nYou don't have enough money for that!")
        store()
      else:
        da_player.gold -= item.cost
        print("\nThank you for purchasing the {}!\nYou have {} gold remaining.".format(item.name, da_player.gold))
        inventory.append(item)
        inventory_item_names.append(item.name.lower())
        print("The {} is now in your inventory.  Remember to equip it!".format(item.name))
        if item.item_type == "potion":
          item.equipped = True
        if item in weapons_list:
          weapons_list.remove(item)
        elif item in armor_list:
          armor_list.remove(item)
        buy_again()
          
  
  
  def purchase_weapons():
    print("\nHere's what we have in stock!\n")
    for weapon in weapons_list:
      print("{}, COST: {}".format(weapon.name, weapon.cost))
    choice = input("\nDo any of these strike your fancy?  If so, type the name of the item you'd like to purchase!\nIf not, just type 'no'\n")
    if choice.lower() == "stick":
      money_check(stick)
    elif choice.lower() == "wooden sword":
      money_check(wooden_sword)
    elif choice.lower() == "iron sword":
      money_check(iron_sword)
    elif choice.lower() == "steel sword":
      money_check(steel_sword)
    elif choice.lower() == "assassin's dagger":
      money_check(assassin_dagger)
    elif choice.lower() == "lightsaber":
      money_check(light_saber)
    elif choice.lower() == "no":
      Town_Menu()
    else:
      print("\nWHAT?!\n")
      purchase_weapons()
    buy_more = input("\nBuy more weapons?\n")
    if buy_more.lower() == "yes":
      purchase_weapons()
    elif buy_more.lower() == "no":
      store()
    
  def purchase_armor():
    print("\nHere's the armor we have in stock!\n")
    for armor in armor_list:
      print("{}, COST: {}".format(armor.name, armor.cost))
    choice = input("\nDo any of these strike your fancy?  If so, type the name of the item you'd like to purchase!\nIf not, just type 'no'\n")
    if choice.lower() == "red cloak":
      money_check(red_cloak)
    elif choice.lower() == "blue cloak":
      money_check(blue_cloak)
    elif choice.lower() == "green cloak":
      money_check(green_cloak)
    elif choice.lower() == "yellow cloak":
      money_check(yellow_cloak)
    elif choice.lower() == "black cloak":
      money_check(black_cloak)
    elif choice.lower() == "invisibility cloak":
      money_check(invisiblity_cloak)
    elif choice.lower() == "no":
      Town_Menu()
    else:
      print("\nWHAT?!\n")
      purchase_armor()
    buy_more = input("\nBuy more armor?\n")
    if buy_more.lower() == "yes":
      purchase_armor()
    elif buy_more.lower() == "no":
      store()
      

  def purchase_potions():
    print("\nHere's what we have in stock!\n")
    for potion in potions_list:
      print("{}, COST: {}".format(potion.name, potion.cost))
    choice = input("\nDo any of these strike your fancy?  If so, type the name of the item you'd like to purchase!\nIf not, just type 'no'\n")
    if choice.lower() == "health potion":
      money_check(health_potion)
    elif choice.lower() == "attack potion":
      money_check(attack_potion)
    elif choice.lower() == "defense potion":
      money_check(defense_potion)
    elif choice.lower() == "speed potion":
      money_check(speed_potion)
    elif choice.lower() == "crit potion":
      money_check(crit_potion)
    elif choice.lower() == "gold potion":
      money_check(gold_potion)
    elif choice.lower() == "exp potion":
      money_check(exp_potion)
    elif choice.lower() == "no":
      Town_Menu()
    else:
      print("\nWHAT?!\n")
      purchase_potions()
    buy_more = input("\nBuy more potions?\n")
    if buy_more.lower() == "yes":
      purchase_potions()
    elif buy_more.lower() == "no":
      store()
  
  wait()
  option = input("\nWelcome to the store!\nWe have plenty of options to choose from and we always have new potions.\n~You have {} gold~\nWhat type of equipment would you like to buy?\n(1) Weapons\n(2) Armor\n(3) Potions\n".format(da_player.gold))
  if option == "1":
    purchase_weapons()
  if option == "2":
    purchase_armor()
  if option == "3":
    purchase_potions()
  


#########################FIGHTING STUFF AHHHHHH##################################
def fight():
  #Summon new monster enemy#
  summoned_monster = Monster(da_player.monlvl)
  
  print("\nA {} has appeared! It has {} HP and {} attack!\n".format(summoned_monster.name, summoned_monster.hp, summoned_monster.attack))
  
  def lvlup():
    wait()
    da_player.lvl += 1
    print("\nLVL UP LVL UP LVL UP LVL UP\nYou are now Level ".format(da_player.lvl))
    hp = random.randint(1,100)
    at = random.randint(1,100)
    d = random.randint(1,100)
    s = random.randint(1,100)
    ac = random.randint(1,100)
    c = random.randint(1,100)
    
    if hp > 30:
      da_player.maxhp += 1
      print("\nYour HP has increased by 1!\n")
    if at > 30:
      da_player.attack += 1
      print("\nYour Attack has increased by 1!\n")
    if d > 30:
      da_player.defense += 1
      print("\nYour Defense has increased by 1!\n")
    if s > 30:
      da_player.speed += 1
      print("\nYour Speed has increased by 1!\n")
    if ac > 30:
      da_player.accuracy += 1
      print("\nYour Accuracy has increased by 1!\n")
    if c > 30:
      da_player.crit += 1
      print("\nYour Critical Hit Perecentage has increased by 1!\n")
    if hp <= 30 and at <= 30 and d <= 30 and s <= 30 and ac <= 30 and c <= 30:
      print("\nWow, that was some horrible luck...no stat bonuses for you!")
      
    da_player.hp = da_player.maxhp
    print("\nYou have been fully healed!\n")
    Town_Menu()
    
    
  
  
  def attack():
    wait()
    hit_chance = random.randint(1,100)
    if hit_chance < 100 - da_player.accuracy:
      wait()
      print("Your attack missed!\n")
      if da_player.speed >= summoned_monster.speed:
        monattack()
      else:
        fight_menu()
    else:
      crit_chance = random.randint(1,100)
      wait()
      #Only gold-steal ability for thief#
      gold_steal = random.randint(1, 100)
      if (gold_steal <= 25) and (da_player.player_class == "thief"):
        gold_stolen = random.randint(1,5)
        print("\n{} stole {} gold from the {}!\n".format(da_player.name, gold_stolen, summoned_monster.name))
        da_player.gold += gold_stolen
      ############################################################################################################  
      monster_damage_taken = da_player.attack - summoned_monster.defense
      if monster_damage_taken <= 0:
        monster_damage_taken = 1
      if da_player.crit > crit_chance:
        monster_damage_taken *= 2
        print("\n{} strikes a critical blow!".format(da_player.name))
      summoned_monster.hp -= monster_damage_taken
      print("\n{} deals {} damage to the {}!\nThe {} has {} HP remaining!\n".format(da_player.name, monster_damage_taken, summoned_monster.name, summoned_monster.name, summoned_monster.hp))
      if summoned_monster.hp <= 0:
        da_player.gold += summoned_monster.gold
        da_player.exp += summoned_monster.exp
        da_player.monlvl += 0.2
        print("\nThe {} has been defeated!\nAs the monster dies you hear its last words:\n\n{}\n\nYou have gained {} gold! You have {} gold in total.\nYou have gained {} exp! You have {} in total.\n".format(summoned_monster.name, sassy_remarks[random.randint(0,len(sassy_remarks)-1)], summoned_monster.gold, da_player.gold, summoned_monster.exp, da_player.exp))
        if da_player.exp >= 100:
          da_player.exp = da_player.exp%100
          lvlup()
        Town_Menu()
      
      if summoned_monster.speed > da_player.speed:
        fight_menu()
      else:
        monattack()
    
    
    
    
  def monattack():
    wait()
    hit_chance = random.randint(1,100)
    if hit_chance < 100 - summoned_monster.accuracy:
      wait()
      print("The {}'s attack missed!\n".format(summoned_monster.name))
      if da_player.speed >= summoned_monster.speed:
        fight_menu()
      else:
        attack()
    else:
      crit_chance = random.randint(1,100)
      wait()
      player_damage_taken = summoned_monster.attack - da_player.defense
      if player_damage_taken <= 0:
         player_damage_taken = 1
      if summoned_monster.crit > crit_chance:
        player_damage_taken *= 2
        print("\nThe {} strikes a critical blow!\n".format(summoned_monster.name))
      da_player.hp -= player_damage_taken
      print("\nThe {} deals {} damage to {}\n{} has {} HP remaining!\n".format(summoned_monster.name, player_damage_taken, da_player.name, da_player.name, da_player.hp))
      if da_player.hp <= 0:
        print("\n You dead.\n")
        system.exit()
      elif da_player.speed >= summoned_monster.speed:
        fight_menu()
      else:
        attack()
  
  
  
  
  def speed_check():
    if da_player.speed >= summoned_monster.speed:
      print("\nYou are faster than the {} and attack first!\n".format(summoned_monster.name))
      attack()
    else:
      print("\nThe {} is faster than you and attacks first!\n".format(summoned_monster.name))
      monattack()
  
  
  def run():
    flee = random.randint(1,100)
    if da_player.speed*100 / (da_player.speed + 2) > flee:
      print("\nYou got away safely!\n")
      Town_Menu()
    else:
      print("\nYou couldn't get away!\n")
      monattack()
  
  def use_potions():
    print("\n~ POTIONS ~\n")
    for item in inventory:
      if item.item_type == "potion":
        print("{}".format(item.name))
    potion = input("\nWhich potion will you use? Write 'none' to go back to fighting!\n") 
    if potion.lower() == "none":
      fight_menu()
    elif potion.lower() in inventory_item_names:
      if potion.lower() == "health potion":
        print("\n{} has been healed by {}hp!\n".format(da_player.name, da_player.maxhp - da_player.hp))
        da_player.hp = da_player.maxhp
        inventory.remove(health_potion)
        inventory_item_names.remove("health potion")
      elif potion.lower() == "defense potion":
        print("\n{}'s defense has increased by {} for the battle!\n".format(da_player.name, defense_potion.defense_bonus))
        da_player.defense += defense_potion.defense_bonus
        inventory.remove(defense_potion)
        inventory_item_names.remove("defense potion")
      elif potion.lower() == "attack potion":
        print("\n{}'s attack has increased by {} for the battle!\n".format(da_player.name, attack_potion.attack_bonus))
        da_player.attack += attack_potion.attack_bonus
        inventory.remove(attack_potion)
        inventory_item_names.remove("attack potion")
      elif potion.lower() == "speed potion":
        print("\n{}'s speed has increased by {} for the battle!\n".format(da_player.name, speed_potion.speed_bonus))
        da_player.speed += speed_potion.speed_bonus
        inventory.remove(speed_potion)
        inventory_item_names.remove("speed potion")
      elif potion.lower() == "crit potion":
        print("\n{}'s critical hit percentage has increased by {}% for the battle!\n".format(da_player.name, crit_potion.crit_bonus))
        da_player.crit += crit_potion.crit_bonus
        inventory.remove(crit_potion)
        inventory_item_names.remove("crit potion")
      elif potion.lower() == "gold potion":
        print("\n{} will gain triple gold for this battle!\n".format(da_player.name))
        summoned_monster.gold *= 3
        inventory.remove(gold_potion)
        inventory_item_names.remove("gold potion")
      elif potion.lower() == "exp potion":
        print("\n{} will gain double EXP for this battle!\n".format(da_player.name))
        summoned_monster.exp *= 2
        inventory.remove(exp_potion)
        inventory_item_names.remove("exp potion")
      else:
        print("\nI don't understand!\n")
        use_potions()
    use_again = input("\nUse another potion?\n(1) Yes\n(2) No\n")
    if (use_again == "1") or (use_again.lower() == "yes"):
      use_potions()
    elif (use_again == "2") or (use_again.lower() == "no"):
      fight_menu()
    else:
      print("\nHUH?!\n")
      fight_menu()
  
  
  def fight_menu():
    wait()
    option = input("\nWhat do you do?\n(1) Attack\n(2) Run\n(3) Use Potions\n")
    if option == "1":
      speed_check()
    elif option == "2":
      run()
    elif option == "3":
      use_potions()
    else:
      print("\nI don't understand!!!")
      fight_menu()











  
  
  
  
  fight_menu()
  
  #Run the Town Menu function!
Town_Menu()
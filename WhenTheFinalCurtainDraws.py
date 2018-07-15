# Sarah Sides
# 7/10/18
# When The Final Curtain Draws

import time
import sys
import random
global character
global inventory
global day

day = 1
character = {}
character["Hunger"]=100
character["Thirst"]=100
character["Health"]=100


if character["Hunger"] > 100:
    character["Hunger"] = 100
        
if character["Thirst"] > 100:
    character["Thirst"] = 100

if character["Health"] > 100:
    character["Health"] = 100

possible_items = {}
possible_items["Item 1"]="OldClothes(Health+20)"
possible_items["Item 2"]="Bandages(Health+40)"
possible_items["Item 3"]="FirstAidKit(Health+60)"
possible_items["Item 4"]="PB&J(Hunger+20)"
possible_items["Item 5"]="Eggs&Bacon(Hunger+40)"
possible_items["Item 6"]="TurkeyDinner(Hunger+60)"
possible_items["Item 7"]="SodaCan(Thirst+20)"
possible_items["Item 8"]="WaterBottle(Thirst+40)"
possible_items["Item 9"]="EnergyDrink(Thirst+60)"

inventory = {}
inventory["Slot 1"]="OldClothes(Health+20)"
inventory["Slot 2"]="PB&J(Hunger+20)"
inventory["Slot 3"]="SodaCan(Thirst+20)"
inventory["Slot 4"]="Empty"
inventory["Slot 5"]="Empty"
inventory["Slot 6"]="Empty"
inventory["Slot 7"]="Empty"
inventory["Slot 8"]="Empty"

menuchoice = 0

# function setup

def rest(day):
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("You spent the day resting.")
    time.sleep(1)
    print("Your stats have risen by 10 points.")
    character["Health"] = character["Health"] + 10
    character["Hunger"] = character["Hunger"] + 10
    character["Thirst"] = character["Thirst"] + 10
    time.sleep(1.5)
    day = end_day(day)
    menu(day)
        
def use_item(day):
    print("Which item would you like to use?")
    print(list(inventory.keys()))
    supply_choice = int(input(" "))
    print("You used an item.")
    slot = list(inventory.keys())[supply_choice - 1]
    used_item = inventory[slot]
    print(inventory[slot])
    time.sleep(2)
            
    if used_item =="OldClothes(Health+20)":
        character["Health"] = character["Health"] + 20
                    
    if used_item =="Bandages(Health+40)":
        character["Health"] = character["Health"] + 40

    if used_item =="FirstAidKit(Health+60)":
        character["Health"] = character["Health"] + 60

    if used_item =="PB&J(Hunger+20)":
        character["Hunger"] = character["Hunger"] + 20
                    
    if used_item =="EggsAndBacon(Hunger+40)":
        character["Hunger"] = character["Hunger"] + 40

    if used_item =="TurkeyDinner(Health+60)":
        character["Hunger"] = character["Hunger"] + 60

    if used_item =="SodaCan(Thirst+20)":
        character["Thirst"] = character["Thirst"] + 20
                    
    if used_item =="WaterBottle(Thirst+40)":
        character["Thirst"] = character["Thirst"] + 40

    if used_item =="EnergyDrink(Thirst+60)":
        character["Thirst"] = character["Thirst"] + 60

    if used_item =="Empty":
        print("You have nothing in this slot.")
        time.sleep(2)

    inventory[slot] = "Empty"
    menu(day)
    
def jokes(day):
    joke = random.randint(1,7)
    time.sleep(1)
    print()
    
    if joke == 1:
        print("Why did the picture go to jail?")
        time.sleep(2)
        print("He was framed!")
    elif joke == 2:
        print("What do you get when you cross a snowman and a vampire?")
        time.sleep(2)
        print("Frostbite!")
    elif joke == 3:
        print("Why did the cookie go to the doctor?")
        time.sleep(2)
        print("He was feeling crummy!")
    elif joke == 4:
        print("What do you call a fake noodle?")
        time.sleep(2)
        print("An impasta!")
    elif joke == 5:
        print("Why did the barber win the race?")
        time.sleep(2)
        print("He took a shortcut!")
    elif joke == 6:
        print("Why didn't the skeleton go to the dance?")
        time.sleep(2)
        print("He had no body to go with!")
    else:
        print("What do you call an alligator in a vest?")
        time.sleep(2)
        print("An investigator!")
        
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("I'm gonna die out here.")
    time.sleep(3)
    menu(day)

def gather_supplies(day):
    available = False
    
    print("You spend the day gathering supplies.")
    time.sleep(2)
    print("You got...")
    time.sleep(1)
    
    gather_chance = random.randint(1,450)
    if 0 < gather_chance < 101:
        item_got = "OldClothes(Health+20)"
    if 100 < gather_chance < 201:
        item_got = "PB&J(Hunger+20)"
    if 200 < gather_chance < 301:
        item_got = "SodaCan(Thirst+20)"
    if 300 < gather_chance < 351:
        item_got = "Bandages(Health+40)"
    if 350 < gather_chance < 401:
        item_got = "Eggs&Bacon(Hunger+40)"
    if 400 < gather_chance < 451:
        item_got = "Water Bottle(Thirst+40)"

    print (item_got)
    
    for slot in inventory:
        if inventory[slot] == "Empty" and available == False:
            inventory[slot] = item_got
            available = True

    if available == False:
        print("You have no space in your inventory for another item.")

    day = end_day(day)
    menu(day)

def fight_supplies(day):
    available = False
    
    print("You spent the day fighting for supplies.")
    time.sleep(2)
    print("You got...")
    time.sleep(1)

    gather_chance = random.randint(1,500)
    if 0 < gather_chance < 101:
        item_got = "Bandages(Health+40)"
    if 100 < gather_chance < 201:
        item_got = "Eggs&Bacon(Hunger+40)"
    if 200 < gather_chance < 301:
        item_got = "WaterBottle(Thirst+40)"
    if 300 < gather_chance < 351:
        item_got = "FirstAidKit(Health+60)"
    if 350 < gather_chance < 401:
        item_got = "TurkeyDinner(Hunger+60)"
    if 400 < gather_chance < 451:
        item_got = "EnergyDrink(Thirst+60)"

    print (item_got)
    time.sleep(1)
    
    for slot in inventory:
        if inventory[slot] == "Empty" and available == False:
            inventory[slot] = item_got
            available = True

    if available == False:
        print("You have no space in your inventory for another item.")

    print("However,you lost some health...")
    time.sleep(2)
          
    health_chance = random.randint(1,5)
    if health_chance == 1:
        print("You lost 10 health outside.")
        character["Health"] = character["Health"] - 10

    if health_chance == 2:
        print("You lost 20 health outside.")
        character["Health"] = character["Health"] - 20

    if health_chance == 3:
        print("You lost 30 health outside.")
        character["Health"] = character["Health"] - 30

    if health_chance == 4:
        print("You lost 40 health outside.")
        character["Health"] = character["Health"] - 40

    if health_chance == 5:
        print("You lost 50 health outside.")
        character["Health"] = character["Health"] - 50

    day = end_day(day)
    menu(day)

def end_day(day):
    time.sleep(2)
    print()
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("The day is now over. ")
    print("-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(2)
    
    character["Hunger"] = character["Hunger"] - 20
    character["Thirst"] = character["Thirst"] - 20
    character["Health"] = character["Health"] - 20
    
    if character["Hunger"] > 100:
        character["Hunger"] = 100
        
    if character["Thirst"] > 100:
        character["Thirst"] = 100

    if character["Health"] > 100:
        character["Health"] = 100

    if character["Hunger"] == 0 or character["Hunger"] < 0:
        loss()
    if character["Thirst"] == 0 or character["Thirst"] < 0:
        loss()
    if character["Health"] == 0 or character["Health"] < 0:
        loss()

    day += 1  
    return day
        

def loss():
    time.sleep(1)
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("      GAME OVER      ")
    print("-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(10)
    sys.exit()

def menu(day):
    print()
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("Day",day,)
    print("(1) View Possible Actions")
    print("(2) View Inventory")
    print("(3) View Stats")
    print("(4) Rest")
    print("(5) Help")
    try:
        menu_choice = int(input(" "))

    except ValueError:
        print("That is an invalid choice. Try again.")
        time.sleep(1.5)
        menu(day)
        
    time.sleep(1)

    if menu_choice == 1:
        print()
        print("-=-=-=-=-=-=-=-=-=-=-")
        print("Possible Actions")
        print("(1) Tell Yourself A Joke")
        print("(2) Gather Supplies")
        print("(3) Fight for Supplies")
        print("(4) Use Supplies(Check Inventory First)")
        print("(5) Go back to menu")
        try:
            action = int(input(" "))

        except ValueError:
            print("That is an invalid choice. Try again.")
            time.sleep(1.5)
            menu(day)
        
        #possible action results

        if action == 1:
            jokes(day)

        elif action == 2:
            gather_supplies(day)
            
        elif action == 3:
            fight_supplies(day)
            
        elif action == 4:
            use_item(day)
            
        elif action == 5:
            menu(day)

        else:
            print("That is an invalid choice. Try again.")
            time.sleep(1.5)
            menu(day)
                
    elif menu_choice == 2:
        print()
        print("-=-=-=-=-=-=-=-=-=-=-")
        print(inventory)
        time.sleep(3)
        menu(day)

    elif menu_choice == 3:
        print()
        print("-=-=-=-=-=-=-=-=-=-=-")
        print("Hunger -",character["Hunger"],)
        print("Thirst -",character["Thirst"],)
        print("Health -",character["Health"],)
        time.sleep(3)
        menu(day)

    elif menu_choice == 4:
        rest(day)
        
    elif menu_choice == 5:
        print()
        print("-=-=-=-=-=-=-=-=-=-")
        print("The point of When The Final Curtain Draws is to stay alive. To do this you must gather supplies and keep your hunger, thirst, and health from reaching 0.")
        time.sleep(4)
        print("Gathering supplies guarantees no loss of your health, but the chances of getting useful items are lower.")
        time.sleep(4)
        print("Fighting for supplies almost guarantees that you will leave with less health or even die. But, the chances of getting useful items are higher.")
        time.sleep(4)
        print("Items you collect will either help your hunger, thirst, or health. The stat that it affects will be listed next to the item name.")
        time.sleep(4)
        print("Resting increases all of your stats by 10. This is useful when you want to give yourself an extra day to live.")
        time.sleep(4)
        print("Supply runs or rest finishes the day. After every day, your three stats will decrease by 20. Doing nothing for 5 turns will kill you.")
        time.sleep(4)
        print("Try your best to survive.")
        time.sleep(5)
        menu(day)

    else:
        print("That is an invalid choice. Try again.")
        time.sleep(1.5)
        menu(day)
        

# the intro
time.sleep(1.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("     When the Final Curtain Draws      ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(3)
print()
print("Upon looking outside, the sun is a bright red.")
time.sleep(3)
print()
print("The television is set to NBC. The newscasters are screaming.")
time.sleep(3)
print()
print("Your neighbors have long since left town.")
time.sleep(3)
print()
print("Your mother has called you at least ten times today.")
time.sleep(3)
print()
print("It is the end of the world.")
time.sleep(3)

# gameplay begins
print()
print("What do you do?")
time.sleep(1)
menu(day)

      

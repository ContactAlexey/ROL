import random
import os
import tkinter as tk
import keyboard

# Monsters' health
monster_1 = 500
monster_2 = 500

# Attack damage values
claw_damage = 10
tail_damage = 50
special_damage = 100

# Hit probabilities (in percentage)
prob_claw = 90    # 90% chance to hit
prob_tail = 70    # 70% chance to hit
prob_special = 15 # 15% chance to hit

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Player's attacks
def attack_claw():
    global monster_2
    luck = random.randint(1, 100)
    if luck <= prob_claw:
        monster_2 -= claw_damage
        print(f"{player_name} hit! You dealt {claw_damage} damage.")
    else:
        print(f"{player_name} missed!")

def attack_tail():
    global monster_2
    luck = random.randint(1, 100)
    if luck <= prob_tail:
        monster_2 -= tail_damage
        print(f"{player_name} hit! You dealt {tail_damage} damage.")
    else:
        print(f"{player_name} missed!")

def attack_special():
    global monster_2
    luck = random.randint(1, 100)
    if luck <= prob_special:
        monster_2 -= special_damage
        print(f"{player_name} hit! You dealt {special_damage} damage.")
    else:
        print(f"{player_name} missed!")

player_name = input("Enter your name: ")

while monster_1 > 0 and monster_2 > 0:
    print(f"{player_name} health: {monster_1}")
    print(f"Monster 2 health: {monster_2}")
    print(f"{player_name}, choose your attack:")
    print("1 = Claw")
    print("2 = Tail")
    print("3 = Special")

    clear_screen()

    # Add hotkeys to call the corresponding attack
    keyboard.add_hotkey('1', attack_claw)
    keyboard.add_hotkey('2', attack_tail)
    keyboard.add_hotkey('3', attack_special)

    keyboard.wait('1','2','3')  # Wait for the player to press a key

    print("Now it's the monster's turn.")

    if monster_2 > 0:
        ia = random.randint(1, 3)
        luck = random.randint(1, 100)
        if ia == 1:
            print("Monster 2 uses Claw Attack!")
            if luck <= prob_claw:
                monster_1 -= claw_damage
                print(f"Monster 2 hit! It dealt {claw_damage} damage.")
            else:
                print("Monster 2 missed!")
        elif ia == 2:
            print("Monster 2 uses Tail Attack!")
            if luck <= prob_tail:
                monster_1 -= tail_damage
                print(f"Monster 2 hit! It dealt {tail_damage} damage.")
            else:
                print("Monster 2 missed!")
        else:
            print("Monster 2 uses Special Attack!")
            if luck <= prob_special:
                monster_1 -= special_damage
                print(f"Monster 2 hit! It dealt {special_damage} damage.")
            else:
                print("Monster 2 missed!")

# Show result window
clear_screen()
window = tk.Tk()
window.geometry("400x300")
if monster_1 <= 0:
    window.title("DEFEAT")
    label = tk.Label(window, text="YOU LOST", font=("Arial", 24), anchor='center')
else:
    window.title("VICTORY")
    label = tk.Label(window, text="YOU WON", font=("Arial", 24), anchor='center')
label.pack(fill=tk.BOTH, expand=True)
window.mainloop()


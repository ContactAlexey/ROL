import random
import os
import tkinter as tk

# Characters
monster_1 = 500
monster_2 = 500

# Abilities
claw = 10
tail = 50
special = 100

# Probability (success rates)
prob1 = 90  # 90% success for claw
prob2 = 70  # 70% success for tail
prob3 = 15  # 15% success for special

# Damage values
claw_damage = 10
tail_damage = 50
special_damage = 100

# Random chance
luck = random.randrange(1, 101)

# Clear the screen
def clear_screen():
    os.system('cls')  # Use 'clear' if you're on macOS/Linux

user = input("Enter your name: ")

while monster_2 > 0 and monster_1 > 0:
    print(f"{user}, you have: {monster_1} HP")
    print(f"The enemy monster has: {monster_2} HP")

    question = input(f"{user}, how do you want to attack? (1=Claw, 2=Tail, 3=Special): ")
    clear_screen()

    match question:
        case "1":
            if luck <= prob1:
                monster_2 -= claw_damage
                print(f"{user}, you hit! You dealt {claw_damage} damage.")
            else:
                print("You missed!")
        case "2":
            if luck <= prob2:
                monster_2 -= tail_damage
                print(f"{user}, you hit! You dealt {tail_damage} damage.")
            else:
                print("You missed!")
        case "3":
            if luck <= prob3:
                monster_2 -= special_damage
                print(f"{user}, you hit! You dealt {special_damage} damage.")
            else:
                print("You missed!")

    print("Now it's the monster's turn...")
    
    if monster_2 > 0:
        ai_choice = random.randrange(1, 4)
        match ai_choice:
            case 1:
                print("Monster 2 used Claw attack!")
                if luck <= prob1:
                    monster_1 -= claw_damage
                    print(f"Monster 2 hit you! It dealt {claw_damage} damage.")
                else:
                    print("Monster 2 missed!")
            case 2:
                print("Monster 2 used Tail attack!")
                if luck <= prob2:
                    monster_1 -= tail_damage
                    print(f"Monster 2 hit you! It dealt {tail_damage} damage.")
                else:
                    print("Monster 2 missed!")
            case 3:
                print("Monster 2 used Special attack!")
                if luck <= prob3:
                    monster_1 -= special_damage
                    print(f"Monster 2 hit you! It dealt {special_damage} damage.")
                else:
                    print("Monster 2 missed!")

# Check who won
if monster_1 < monster_2:
    clear_screen()
    # Create defeat window
    window = tk.Tk()
    window.title("DEFEAT")
    window.geometry("400x300")
    label = tk.Label(text="YOU LOST", font=("Arial", 24), anchor='center')
    label.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

if monster_2 < monster_1:
    clear_screen()
    # Create victory window
    window = tk.Tk()
    window.title("VICTORY")
    window.geometry("400x300")
    label = tk.Label(text="YOU WON", font=("Arial", 24), anchor='center')
    label.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

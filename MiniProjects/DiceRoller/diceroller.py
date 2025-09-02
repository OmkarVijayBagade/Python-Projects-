import random 
import time 
import os   

#ascii art 
dice_faces = {
    1: (
        "+-------+\n"
        "|       |\n"
        "|   ●   |\n"
        "|       |\n"
        "+-------+"
    ),
    2: (
        "+-------+\n"
        "| ●     |\n"
        "|       |\n"
        "|     ● |\n"
        "+-------+"
    ),
    3: (
        "+-------+\n"
        "| ●     |\n"
        "|   ●   |\n"
        "|     ● |\n"
        "+-------+"
    ),
    4: (
        "+-------+\n"
        "| ●   ● |\n"
        "|       |\n"
        "| ●   ● |\n"
        "+-------+"
    ),
    5: (
        "+-------+\n"
        "| ●   ● |\n"
        "|   ●   |\n"
        "| ●   ● |\n"
        "+-------+"
    ),
    6: (
        "+-------+\n"
        "| ●   ● |\n"
        "| ●   ● |\n"
        "| ●   ● |\n"
        "+-------+"
    )
}

def roll_dice():
    """
    Simulates rolling a single 6-sided dice.
    Returns a random integer between 1 and 6.
    """
    return random.randint(1,6)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def shake_dice_animation():
    for _ in range(5):
        number = random.randint(1,6)
        clear_screen()
        print("Rolling dice....\n")
        print(dice_faces[number])
        time.sleep(0.2)

def main():
    print("🎲 Welcome to the Dice Roller! 🎲\n")
    
    while True: 
        input("Press enter to roll the dice...")
        shake_dice_animation()
        number = roll_dice()
        clear_screen()
        print(f"You rolled a {number}!\n")
        print(dice_faces[number]) 

        choice = input("Do you want to roll again? (yes/no): ").strip().lower()
        # .strip() removes any extra spaces before or after the input
        # .lower() converts input to lowercase so "YES" or "Yes" also works

        if choice != "yes" and choice != "y" and choice != "Y" and choice != "Yes" :
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()  
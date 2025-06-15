#second part
print("At this part of the game , you need: go around of the trap, find the key, and escape from main door.")
#part 2
has_key1 = False
has_key2 = False
step = 0

while True:
    print("You are in a corridor with multiple escape options.")
    print("You have 5 steps to escape , or you will be caught by the monster.")


    choice2 = input("Now you are in the corridor. Do you need try to find way from house - you can make it choice how you want to escape:" \
    "\nPress '1' if you want to destroy the window, but its hurt" \
    "\nPress '2' if you want to escape via door, but you need to find 2 keys" \
    "\nPress '3' if you want to escape via trapdoor " \
    "\nPress '4' if you want to escape via door from under the house" \
    "\nPress '5' if you want to look at note on the wall" \
    "\nYour choice: ").strip().lower()
    if step >= 5:
        print("You have been caught by the monster! Game over.")
        break
    #window

    if choice2 == '1':
        print("You try to destroy the window, but it hurts you. You lose 1 step.")
        step += 1
        print(f"Steps left: {5 - step}")
    #door
    elif choice2 == '2':
        if has_key1 and has_key2:
            print("You have both keys! You unlock the door and escape!")
            break
        else:
            print("You need to find both keys to escape via door.")
            if not has_key1:
                print("You find the first key in a drawer.")
                has_key1 = True
            if not has_key2:
                print("You find the second key under a rug.")
                has_key2 = True
            step += 1
            print(f"Steps left: {5 - step}")
    #trapdoor
    elif choice2 == '3':
        print("You find a trapdoor and escape through it!")
        break
    #door under the house
    elif choice2 == '4':
        print("You find a door under the house and escape through it!")
        break
    #note on the wall
    elif choice2 == '5':
        print("You find a note on the wall that says 'The keys are hidden under the rug and in the drawer.'")
        step += 1
        print(f"Steps left: {5 - step}")
    
    else:
        print("Invalid choice. Try again.")
        step += 1
        print(f"Steps left: {5 - step}")
print("You have successfully escaped the corridor! Congratulations!")
# This code is a simple text-based escape room game where the player has to find keys and escape through various methods.

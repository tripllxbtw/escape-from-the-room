#run away from the room.py
print("You are in a room with a locked door.")
has_key = False
def main():
    global has_key
    print("Welcome to the escape room!")
    print("You need to find a way to escape the room.")
    print("You can look around, unlock the door, leave, or try to crack the door open.")
    print("Type 'look' to search the room, 'unlock' to unlock the door, 'leave' to exit, or 'crack' to try cracking the door.")
    print("Good luck!")
while True:
    action = input("What do you want to do? (look, unlock, leave, crack): ").strip().lower()
    if action == "look":
        print("You see a door and a key on the table.")
        if not has_key:
            has_key = True
            print("You pick up the key.")
        else:
            print("You already have the key.")
    elif action == "crack":
        print("You try to crack the door open.")
        if has_key:
            print("You successfully crack the door open with the key!")
        else:
            print("You need a key to crack the door.")
    elif action == "unlock":
        if has_key:
            print("You unlock the door and escape!")
            break
        else:
            print("You need a key to unlock the door.")
    elif action == "leave":
        if has_key:
            print("You leave the room with the key.")
            break
        else:
            print("You can't leave without unlocking the door first.")
    else:
        print("Invalid action. Try again.")
    print("You are still in the room.")
print("You have escaped the room successfully!")
if __name__ == "__main__":
    main()
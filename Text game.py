room = "livingroom"
inventory = []
house = "occupied"
help = """actions: pick up, open.
pick up:
stores the key in your inventory
Example: 'pick up kitchen key'
open:
open the door to the room of your choosing depending on the room you are in.
just type in open press spacebar then type the room.
Example: open bedroom 1"""
while house == "occupied":
    while room == "livingroom":
        print("""You are in the livingroom. It contains a couch, television, and
all the other bullshit that is in a normie's livingroom. There is a door leading
to the kitchen as well.""")
        if "kitchen key" not in inventory:
            print("There is also a kitchen key located on the livingroom table.")
        action = input("type an action. For a list of actions, type 'help': ")
        if action == "pick up kitchen key":
            inventory.append("kitchen key")
            print("you picked up the 'kitchen key'")
        elif action == "open kitchen door":
            if "kitchen key" in inventory:
                room = "kitchen"
            else:
                print("The door is locked. You need the Kitchen key.")
        elif action == "help":
            print(help)
        else:
            print("That is not a valid option.")
    while room == "kitchen":
        print("""What a surprise! there's more bullshit that's in everyone else's
kitchens. A lot of silverware in drawers, a microwave, and Kitchen counters.
There are two doors. One door leads to bedroom 1 and the other to bedroom 2.""")
        if "bedroom 1 key" not in inventory:
            print("you notice the bedroom 1 key on the counter.")
        if "bedroom 2 key" not in inventory:
            print("you notice the bedroom 2 key on the counter.")
        action = input("type an action. For a list of actions, type 'help': ")
        if action == "pick up bedroom 1 key":
            inventory.append("bedroom 1 key")
            print("You picked up the bedroom 1 key.")
        elif action == "pick up bedroom 2 key":
            inventory.append("bedroom 2 key")
            print("you picked up the bedroom 2 key.")
        elif action == "open bedroom 1 door":
            if "bedroom 1 key" in inventory:
                room = "bedroom 1"
            else:
                print("The door is locked. You need the bedroom 1 key.")
        elif action == "open bedroom 2 door":
            if "bedroom 2 key" in inventory:
                room = "bedroom 2"
            else:
                print("The door is locked. You need the bedroom 2 key.")
        elif action == "open livingroom door":
            room = "livingroom"
        elif action == "help":
            print(help)
        else:
            print("That is not a valid option.")
    while room == "bedroom 1":
        print("""Alright! This is getting old now! Where's my alcohol?! I'm hungry.
There's a bunch of shit in the room. Is that Disgaea 5 I see?! The only
door left in this room is the one that leads to the kitchen. Take a wild
guess at what you should do. Before you type in 'pick up key' there's
not a key to be picked up. So, don't.""")
        action = input("There's only one command you can type. So type it: ")
        if action == "open kitchen door":
            room = "kitchen"
        else:
            print("Seriously? You had one job. Try again.")
    while room == "bedroom 2":
        print("I'm tired. It's just a basic room. The kitchen door is behind you.")
        action = input("There's only one command you can type. So type it: ")
        if action == "open kitchen door":
            room = "kitchen"
        else:
            print("Seriously? You had one job. Try again.")


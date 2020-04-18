from termcolor import colored, cprint


player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.\nThere are the following exits:",
        "exit": {
            'east': 'cave',
            'west': 'stonehenge',
            'north': '1968',
            'south': 'imagination',
        },
        "items": {
            "key": "key",
        },
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.\nThere are the following exits:",
        "exit": {
            'west': 'outside' 
            },
    },
    "stonehenge": {
        "title": "Stonehenge",
        "description": "What\'s the meaning of Stonehenge?\nThere are the following exits:",
        "exit": {
            'east': 'outside' 
            },
    },
    "1968": {
        "title": "1968",
        "description": "Battle of Khe Sanh\nThere are the following exits:",
        "exit": {
            'south': 'outside' 
            },
    },
    "imagination": {
        "title": "Imagination",
        "description": "Where is my mind?\nThere are the following exits:",
        "exit": {
            'north': 'outside' 
            },
    },
}

room = {
    ""
}


def main():
    describe_room()
    describe_items()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
            describe_items()
        if command in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']:
            move(command)
            describe_room()
            describe_items()
        elif command in ['quit', 'q']:
            cprint('Bye!', "magenta")
            playing = False
        else:
            print(f'Unrecognized command: {command}')


def get_command():
    print()
    return input(colored('> ', "green"))


def describe_room():
    room = rooms[player['room']]
    print()
    cprint(room['title'], 'yellow')
    print()
    p = colored(get_vailable_exits(), "green")
    cprint(room['description'] + p, "magenta")
    


def get_vailable_exits():
    room = rooms[player['room']]
    exits = room['exit']

    exit_options = []
    for exit in exits:
        exit_options.append(exit)

    return " ".join(exit_options)

def move(command):
    room = rooms[player['room']]
    exits = room["exit"]
    next_location = exits[command]
    player['room'] = next_location


def describe_items():
    room = rooms[player['room']]
    items = get_items_row()
    colored_items = colored(items, "white")
    cprint("There are items on the floor: " + colored_items, 'magenta')
    print()


def get_items_row():
    room = rooms[player['room']]
    items = room['items']
    items_names = []

    for item in items:
        items_names.append(item)

    return "".join(items_names)


if __name__ == '__main__':
    main()



    

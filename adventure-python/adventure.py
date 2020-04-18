from termcolor import colored, cprint


player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.\n There are the following exits:",
        "exit": {
            'east': 'cave',
            'west': 'stonehenge',
            'north': '1968',
            'south': 'imagination',
        },
        "items": ['dirt', 'stick'],
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "exit": {
            'west': 'outside' 
            },
        "items": ['dirt', 'stick', 'mud', 'mold'],
    },
    "stonehenge": {
        "title": "Stonehenge",
        "description": "What\'s the meaning of Stonehenge?",
        "exit": {
            'east': 'outside' 
            },
        "items": ['bone', 'pepsi can'],
    },
    "1968": {
        "title": "1968",
        "description": "Battle of Khe Sanh",
        "exit": {
            'south': 'outside' 
            },
        "items": ['grenade', 'hustler magazine'],
    },
    "imagination": {
        "title": "Imagination",
        "description": "Where is my mind?",
        "exit": {
            'north': 'outside' 
            },
        "items": ['sawdust', 'fish'],
    },
}

room = {
    ""
}


def main():
    describe_room()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        if command in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']:
            move()
        elif command in ['quit', 'q']:
            cprint('Bye!', "white")
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
    cprint(room['description'] + get_vailable_exits(), "white")
    


def get_vailable_exits():
    room = rooms[player['room']]
    exits = room['exit']

    exit_options = []
    for exit in exits:
        exit_options.append(exit)

    return " ".join(exit_options)

if __name__ == '__main__':
    main()


def move(command):
    room = rooms[player['room']]
    exits = room["exit"]
    print(exits[command])
    

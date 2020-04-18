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
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        if command in ['north', 'south', 'east', 'west', 'n', 's', 'e', 'w']:
            move(command)
            describe_room()
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
    p = colored(get_vailable_exits(), "green")
    cprint(room['description'] + p, "white")
    


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


if __name__ == '__main__':
    main()



    

from termcolor import colored, cprint


player = {
    'room': 'outside',
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.\n Exits are available:",
        "exit": {
            'east': 'cave',
            'west': 'stonehenge',
            'north': '1968',
            'south': 'imagination',
        },
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "exit": {
            'west': 'outside'
        },
    },
    "stonehenge": {
        "title": "Stonehenge",
        "description": "What\'s the meaning of Stonehenge?",
        "exit": {
            'west': 'outside'
        }, 
    },
    "1968": {
        "title": "1968",
        "description": "Battle of Khe Sanh",
        "exit": {
            'south': 'outside'
        },
    },
    "imagination": {
        "title": "Imagination",
        "description": "Where is my mind?",
        "exit": {
            'north'
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
<<<<<<< Updated upstream
           move()
=======
            move()
>>>>>>> Stashed changes
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
    cprint(room['title'], 'red')
    print()
    cprint(room['description'], "white")


def get_vailable_exits():
    room = rooms[player['room']]


if __name__ == '__main__':
    main()

def move():

    """
    Args:
    """
    pass

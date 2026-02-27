# Write your game here

import curses
import time

# Good Luck!
game_data = {
    'width': 20,
    'height': 25,
    'player': {"x": 0, "y": 0, "score": 0},
    'obstacles': [
        {"x": 1, "y": 2},
        {"x": 3, "y": 1}
    ],

    # ASCII icons
    'chicken': "\U0001F414",
    'rock': "\U0001FAA8 ",
    'tree1': "\U0001F332",
    'tree2': "\U0001F333",

    'empty': "  "
}

def draw_board(screen):
    # Print the board and all game elements using curses
    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['chicken']
            # Obstacles
           # elif any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
              #  row += game_data['obstacle']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))
    stdscr.addstr(game_data['height'] + 1, 0,
                  f"Moves Survived: {game_data['player']['score']}",
                  curses.color_pair(1))
    stdscr.addstr(game_data['height'] + 2, 0,
                  "Move with W/S/D (no backwards), Q to quit",
                  curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 0:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
    else:
        return  # Invalid key or move off board

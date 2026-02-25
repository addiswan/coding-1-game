# Write your game here

#game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
#}

#def draw_board(screen):
    # Print the board and all game elements using curses

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

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

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

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

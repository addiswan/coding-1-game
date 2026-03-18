# Write your game here

import curses
import random
import time

# Good Luck!
game_data = {
    'width': 15,
    'height': 2,
    'player': {"x": 0, "y": 0, "score": 0},
    'obstacles': [
        {"x": 2, "y": 1, },
    ],

    #icons
    'chicken': "\U0001F414",
    'rock': "\U0001FAA8 ",
    'tree1': "\U0001F332",
    'tree2': "\U0001F333",
    'empty': "  ",
}
def random_obs_move():
    for obstacle in game_data['rock']:
        obstacle["x"] = random.randint(1,2)
        obstacle["y"] = random.randint(1,14)

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['chicken']
            # Obstacles
            elif any(c['x'] == x and c['y'] == y for c in game_data['obstacles']):
                row += game_data['rock']

            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1)) #read docs for curses
        # stdscr.addstr(game_data['height'] + 1, 0,
        #             f"Moves Survived: {game_data['player']['score']}",
        #             curses.color_pair(1))
        # stdscr.addstr(game_data['height'] + 2, 0,
        #             "Move with W/S/D (no backwards), Q to quit",
        #             curses.color_pair(1))
    stdscr.refresh()
        # stdscr.getkey()  # pause so player can see board

# curses.wrapper(draw_board)

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
    # else:
    #     return  # Invalid key or move off board
    
        # Check for obstacles
    # if any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
    #     return

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    game_data['player']['score'] += 1


def obstacless():
    obstacle_count = [c for c in game_data['obstacles']]
    if len(obstacle_count) >= 7:
        return
    if random.random() > 0.2:
        return

    while True:
        x = random.randint(0, game_data['width'] - 1)
        y = random.randint(0, game_data['height'] - 1)

        if (x, y) == (game_data['player']['x'], game_data['player']['y']):
            continue
        if any(o['x'] == x and o['y'] == y for o in game_data['obstacles']):
            continue
        break



def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            move_player(key)
            random_obs_move()
            draw_board(stdscr)
            time.sleep(0.2)


curses.wrapper(main)

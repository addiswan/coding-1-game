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

def draw_board(screen):
   z # Print the board and all game elements using curses
>>>>>>> 260fead (put in icons)

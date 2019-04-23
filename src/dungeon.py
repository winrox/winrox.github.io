import random
import os

CELLS = [
    [(0,0), (1,0), (2,0), (3,0), (4,0)],
    [(0,1), (1,1), (2,1), (3,1), (4,1)],
    [(0,2), (1,2), (2,2), (3,2), (4,2)],
    [(0,3), (1,3), (2,3), (3,3), (4,3)],
    [(0,4), (1,4), (2,4), (3,4), (4,4)]
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_grid(monster, door, player):
    for row in CELLS:
        row_to_draw = ""
        for cell in row:
            if cell == player and not cell == monster and not cell == door:
                row_to_draw += "[🤔]"
            elif cell == player and cell == monster:
                row_to_draw += "[👹]"
            elif cell == player and cell == door:
                row_to_draw += "[🚪]"
            else:
                row_to_draw += "[  ]"
        print(row_to_draw)

def get_locations():
#    randint = random.randint
#    monster = (randint(0,4), randint(0,4))
#    door = None
#    player = None
#
#    def find_not_used_coords():
#        coords = (randint(0,4), randint(0,4))
#        if not coords == monster and not coords == door and not coords == player:
#            return coords
#        else:
#            find_not_used_coords()
#
#    door = find_not_used_coords()
#    player = find_not_used_coords()

#    return monster, door, player

    # below does all of the above code for me with list comprehension and unique samples
    return random.sample([item for list in CELLS for item in list], 3)

def move_player(player_position, move):
    new_pos = None
    # if move == LEFT, x-1
    if move == "LEFT":
        new_pos = (player_position[0] - 1, player_position[1])
    # if move == RIGHT, x+1
    elif move == "RIGHT":
        new_pos = (player_position[0] + 1, player_position[1])
    # if move == UP, y-1
    if move == "UP":
        new_pos = (player_position[0], player_position[1] - 1)
    # if move == DOWN, y+1
    if move == "DOWN":
        new_pos = (player_position[0], player_position[1] + 1)

    return new_pos

def get_moves(player_position):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player_position

    if y == 0: # they can't move UP
        moves.pop(2)
    elif y == 4: # they can't move DOWN
        moves.pop(3)

    if x == 0: # they cabn't move LEFT
        moves.pop(0)
    elif x == 4: # they can't move RIGHT
        moves.pop(1)

    return moves

first_move = True
player = None

while True:
    if first_move:
        print("Welcome to the dungeon!\nYou're trapped and need to escape.\nYou don't know which room the door to escape is in or which room contains a monster.\nTry to escape, good luck!!!")
        first_move = False
        monster, door, player_pos = get_locations()
        player = player_pos
        draw_grid(monster, door, player)

    print("You're currently in room {}".format(player))
    available_moves = get_moves(player)
    moves_length = len(available_moves)
    move_options = None
    if moves_length > 2:
        move_options = ", ".join(available_moves[:-1]) + ' or ' + available_moves[-1]
    elif moves_length == 2:
        move_options = " or ".join(available_moves)
    elif moves_length < 2:
        move_options = available_moves[0]

    print("You can move {}".format(move_options))
    print("Enter QUIT to quit")

    move = input("> ").upper()
    new_position = None
    # move player
    if move == "QUIT":
        break
    elif move in available_moves:
        new_position = move_player(player, move)
        player = new_position
    else:
        print("Please enter a valid move.")

    clear_screen()
    draw_grid(monster, door, player)
    if new_position and new_position == monster:
        print("AHHHHH THE MONSTER GOT YOU!!!!!\nGAME OVER!")
        break
    elif new_position and new_position == door:
        print("YAY!\nYou made it to the door and escaped, congratulations!")
        break
    else:
        continue

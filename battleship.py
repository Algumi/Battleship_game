from random import randint
board = []
current_board = []
dead_ship = 0


def game_mode_input():
    print ">> Would you like to play alone or with a friend ? "
    game_mode = int(raw_input('>> print "1" to play alone, else print "2": '))
    while game_mode != 1 and game_mode != 2:
        print '>> error, please print "1" or "2"'
        game_mode = int(raw_input('>> print "1" to play alone, else print "2": '))
    if game_mode == 1:
        print ">> you've chosen to play alone"
    else:
        print ">> you've chosen to play with friend"
    return game_mode


def board_size_input():
    board_size = int(raw_input(">> you can play on the board 4x4, 6x6 or 10x10, print 4, 6, or 10 to chose it: "))
    while board_size != 4 and board_size != 6 and board_size != 10:
        print ">> error, try to print the size of the board again"
        board_size = int(raw_input(">> you can play on the board 4x4, 6x6 or 10x10, print 4, 6, or 10 to chose it"))
    if board_size == 4:
        print "you've chosen the board 4x4"
    if board_size == 6:
        print "you've chosen the board 6x6"
    if board_size == 10:
        print "you've chosen the board 10x10"
    return board_size


def generate_board(board_size):
    for x in range(board_size):  # creating the board of the game
        board.append(["O"] * board_size)


def generate_current_board(board_size):
    for x in range(board_size):
        current_board.append(["O"] * board_size)


def print_board(field):
    letter = unichr(97)
    if len(board) == 4:
        print "  1 2 3 4"
    if len(board) == 6:
        print "  1 2 3 4 5 6"
    if len(board) == 10:
        print "  1 2 3 4 5 6 7 8 9 10"
    for row in field:
        print letter, " ".join(row)
        letter = unichr(ord(letter.lower())+1)


def start():
    print "Welcome to Battleship"
    # game_mode = game_mode_input()
    game_mode = 1
    board_size = board_size_input()
    generate_board(board_size)
    return game_mode


def check_ship(x, y):
    if x > len(board) - 1:
        return False
    if y > len(board) - 1:
        return False

    if board[x][y] == "X":
        return False

    if y < len(board) - 1:
        if board[x][y + 1] == "X":
            return False
    if y > 0:
        if board[x][y - 1] == "X":
            return False
    if x < len(board) - 1:
        if board[x + 1][y] == "X":
            return False
    if x > 0:
        if board[x - 1][y] == "X":
            return False
    if y < len(board) - 1 and x < len(board) - 1:
        if board[x + 1][y + 1] == "X":
            return False
    if x > 0 and y > 0:
        if board[x - 1][y - 1] == "X":
            return False
    if y < len(board) - 1 and x > 0:
        if board[x - 1][y + 1] == "X":
            return False
    if x < len(board) - 1 and y > 0:
        if board[x + 1][y - 1] == "X":
            return False
    return True


def generate_ship():
    coord = []
    coord_x = randint(0, len(board) - 1)
    coord_y = randint(0, len(board[0]) - 1)
    correct_coord = check_ship(coord_x, coord_y)
    while not correct_coord:
        coord_x = randint(0, len(board) - 1)
        coord_y = randint(0, len(board[0]) - 1)
        correct_coord = check_ship(coord_x, coord_y)
    coord.append(coord_x)
    coord.append(coord_y)
    return coord


def generate_small_ship():
    coord = generate_ship()
    board[coord[0]][coord[1]] = 'X'


def generate_double_ship():
    created = False
    while not created:
        coord = generate_ship()
        direction = randint(0, 1)
        if direction == 0:
            if check_ship(coord[0] + 1, coord[1]):
                board[coord[0]][coord[1]] = 'X'
                board[coord[0] + 1][coord[1]] = 'X'
                created = True
            elif check_ship(coord[0] - 1, coord[1]):
                board[coord[0]][coord[1]] = 'X'
                board[coord[0] - 1][coord[1]] = 'X'
                created = True
            else:
                direction = 1
        if direction == 1:
            if check_ship(coord[0], coord[1] + 1):
                board[coord[0]][coord[1]] = 'X'
                board[coord[0]][coord[1] + 1] = 'X'
                created = True
            elif check_ship(coord[0], coord[1] - 1):
                board[coord[0]][coord[1]] = 'X'
                board[coord[0]][coord[1] - 1] = 'X'
                created = True


def generate_triple_ship():
    created = False
    while not created:
        coord = generate_ship()
        direction = randint(0, 1)
        if direction == 0:
            if check_ship(coord[0] + 1, coord[1]):
                if check_ship(coord[0] + 2, coord[1]):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0] + 1][coord[1]] = 'X'
                    board[coord[0] + 2][coord[1]] = 'X'
                    created = True
                elif check_ship(coord[0] - 1, coord[1]):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0] + 1][coord[1]] = 'X'
                    board[coord[0] - 1][coord[1]] = 'X'
                    created = True
            if check_ship(coord[0] - 1, coord[1]) and not created:
                if check_ship(coord[0] - 2, coord[1]):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0] - 1][coord[1]] = 'X'
                    board[coord[0] - 2][coord[1]] = 'X'
                    created = True
            if not created:
                direction = 1
        if direction == 1:
            if check_ship(coord[0], coord[1] + 1):
                if check_ship(coord[0], coord[1] + 2):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0]][coord[1] + 1] = 'X'
                    board[coord[0]][coord[1] + 2] = 'X'
                    created = True
                elif check_ship(coord[0], coord[1] - 1):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0]][coord[1] + 1] = 'X'
                    board[coord[0]][coord[1] - 1] = 'X'
                    created = True
            if check_ship(coord[0], coord[1] - 1) and not created:
                if check_ship(coord[0], coord[1] - 2):
                    board[coord[0]][coord[1]] = 'X'
                    board[coord[0]][coord[1] - 1] = 'X'
                    board[coord[0]][coord[1] - 2] = 'X'
                    created = True


def generate_quad_ship():
    created = False
    while not created:
        coord = generate_ship()
        direction = randint(0, 1)
        if direction == 0:
            if coord[0] > 2:
                board[coord[0]][coord[1]] = 'X'
                board[coord[0] - 1][coord[1]] = 'X'
                board[coord[0] - 2][coord[1]] = 'X'
                board[coord[0] - 3][coord[1]] = 'X'
                created = True
            elif coord[0] < len(board) - 3:
                board[coord[0]][coord[1]] = 'X'
                board[coord[0] + 1][coord[1]] = 'X'
                board[coord[0] + 2][coord[1]] = 'X'
                board[coord[0] + 3][coord[1]] = 'X'
                created = True
            else:
                direction = 1
        if direction == 1:
            if coord[1] > 2:
                board[coord[0]][coord[1]] = 'X'
                board[coord[0]][coord[1] - 1] = 'X'
                board[coord[0]][coord[1] - 2] = 'X'
                board[coord[0]][coord[1] - 3] = 'X'
                created = True
            elif coord[1] < len(board) - 3:
                board[coord[0]][coord[1] + 1] = 'X'
                board[coord[0]][coord[1] + 2] = 'X'
                board[coord[0]][coord[1] + 3] = 'X'
                board[coord[0]][coord[1] + 4] = 'X'
                created = True


def generate_all_ship():
    if len(board) == 4:
        generate_double_ship()
        generate_small_ship()
        generate_small_ship()
    if len(board) == 6:
        generate_triple_ship()
        generate_double_ship()
        generate_double_ship()
        generate_small_ship()
        generate_small_ship()
    if len(board) == 10:
        generate_quad_ship()
        generate_triple_ship()
        generate_triple_ship()
        generate_double_ship()
        generate_double_ship()
        generate_double_ship()
        generate_small_ship()
        generate_small_ship()
        generate_small_ship()
        generate_small_ship()


def destroy_ship(x, y):
    if check_ship(x-1, y):
        if board[x-1][y] == 'W':
            current_board[x-1][y] = 'X'
            if check_ship(x-2, y):
                if board[x-2][y] == 'W':
                    current_board[x-2][y] = 'X'
                    if check_ship(x-3, y):
                        if board[x-3][y] == 'W':
                            current_board[x-3][y] = 'X'
    if check_ship(x+1, y):
        if board[x+1][y] == 'W':
            current_board[x+1][y] = 'X'
            if check_ship(x+2, y):
                if board[x+2][y] == 'W':
                    current_board[x+2][y] = 'X'
                    if check_ship(x+3, y):
                        if board[x+3][y] == 'W':
                            current_board[x+3][y] = 'X'
    if check_ship(x, y+1):
        if board[x][y+1] == 'W':
                current_board[x][y+1] = 'X'
                if check_ship(x, y+2):
                    if board[x][y+2] == 'W':
                        current_board[x][y+2] = 'X'
                        if check_ship(x, y+3):
                            if board[x][y+3] == 'W':
                                current_board[x][y+3] = 'X'
    if check_ship(x, y-1):
        if board[x][y-1] == 'W':
                current_board[x][y-1] = 'X'
                if check_ship(x, y-2):
                    if board[x][y-2] == 'W':
                        current_board[x][y-2] = 'X'
                        if check_ship(x, y-3):
                            if board[x][y-3] == 'W':
                                current_board[x][y-3] = 'X'


def transform_letter(y):
    result = ord(y) - 97
    return result


def coord_input():
    y = int(raw_input("coordinate x: ")) - 1  # just as planned, no panic
    temp_x = raw_input("coordinate y: ")
    x = transform_letter(temp_x)
    success = 0
    if x < 0:
        print "error, there is no such coordinate"
        return 0
    if x > len(board) - 1:
        print "error, there is no such coordinate"
        return 0
    if y < 0:
        print "error, there is no such coordinate"
        return 0
    if y > len(board) - 1:
        print "error, there is no such coordinate"
        return 0
    if board[x][y] == 'X':
        board[x][y] = 'W'
        if check_ship(x, y):
            current_board[x][y] = "X"
            print "nice shot"
            print "you've destroyed this ship"
            destroy_ship(x, y)
            print_board(current_board)
            success = 2
        else:
            current_board[x][y] = "W"
            print "nice shot"
            print "you've damaged this ship, destroy it faster"
            print_board(current_board)
            success = 2
    if board[x][y] == "O" and not success:
        board[x][y] = "P"
        current_board[x][y] = "P"
        print "you've missed"
        print_board(current_board)
        success = 1
    if not current_board[x][y] == "O" and not success:
        print "you've already checked this coordinate, try again"
    return success


def check_win(current_damage):
    if len(board) == 4:
        if current_damage == 4:
            return True
    if len(board) == 6:
        if current_damage == 9:
            return True
    if len(board) == 10:
        if current_damage == 20:
            return True
    return False


def max_attempts_input():
    result = 0
    if len(board) == 4:
        while result < 4:
            result = int(raw_input("how many attempts will you need? "))
            if result < 4:
                print "you are not so good, try to enter the number of your attempts again: "
    if len(board) == 6:
        while result < 9:
            result = int(raw_input("how many attempts will you need? "))
            if result < 9:
                print "you are not so good, try to enter the number of your attempts again: "
    if len(board) == 10:
        while result < 20:
            result = int(raw_input("how many attempts will you need? "))
            if result < 20:
                print "you are not so good, try to enter the number of your attempts again: "
    return result


def one_player_mode():
    generate_all_ship()
    generate_current_board(len(board))
    print_board(current_board)
    damage = 0
    max_attempts = max_attempts_input()
    current_attempt = 1
    print "let's begin our game!"
    while current_attempt <= max_attempts and not check_win(damage):
        print "turn ", current_attempt
        result = coord_input()
        if result == 2:
            current_attempt += 1
            damage += 1
        if result == 1:
            current_attempt += 1
    if check_win and max_attempts >= current_attempt:
        print "-------The Winner is you!-------"
        print "Statistics:"
        print "--- you needed %s attempts to destroy all the ships" % (current_attempt - 1)
        print "--- you've missed %s times" % (current_attempt - 1 - damage)
        print "--- your accuracy is about %s percent" % (100 * damage / (current_attempt - 1))
    else:
        print "-------Game Over-------"
        print "You are looser"
        print "Statistics:"
        print "--- you've missed %s times" % (current_attempt - 1 - damage)
        print "--- your accuracy is about %s percent" % (100 * damage / (current_attempt - 1))
        print "the board was: "
        print_board(board)


def try_again():
    print "would you like to play again ? (enter Yes/No)"
    answer = ""
    while not answer == "Yes" or not answer == "No":
        answer = raw_input()
        if answer == "Yes":
            return True
        if answer == "No":
            return False


def game():
    cont = True
    while cont:
        game_mode = start()
        if game_mode == 1:
            one_player_mode()
        cont = try_again()


game()

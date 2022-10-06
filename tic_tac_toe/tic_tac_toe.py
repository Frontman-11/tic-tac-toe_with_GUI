# TIC-TAC-TOE GAME CLASS
import random


def render_template(table):
    print('\t.____.____.____.')
    print(
        f'\t| {table[0][0]}  | {table[0][1]}  |  {table[0][2]} |')
    print('\t|____|____|____|')
    print(
        f'\t| {table[1][0]}  | {table[1][1]}  |  {table[1][2]} |')
    print('\t|____|____|____|')
    print(
        f'\t| {table[2][0]}  | {table[2][1]}  |  {table[2][2]} |')
    print('\t|____|____|____|')


def winning_check(board):
    # ROW CHECK OPEN
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        return True
    # ROW CHECK CLOSE

    # COLUMN CHECK OPEN
    elif board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        return True
    # COLUMN CHECK CLOSE

    # DIAGONAL CHECK OPEN
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    return False


class T3Game:
    random_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    def __init__(self, player_name, moves, board, score, win_check, player_id, my_play_history=None, mode=None):
        self.player_name = player_name
        self.moves = moves
        self.board = board
        self.score = score
        self.my_play_history = my_play_history
        self.win_check = win_check
        self.player_id = player_id
        self.mode = mode

    def movement(self):
        if self.player_name != 'Frontbot':
            while True:
                try:
                    player_number = int(input('Enter No. to play: '))
                    if player_number not in self.moves:
                        print(f"Oops! Enter value among {', '.join(map(lambda num: str(num), self.moves))}")
                        continue
                except ValueError:
                    print(f'Oops: Enter a real number')
                    continue
                else:
                    self.moves.remove(player_number)
                    return self.update_board(player_number, self.board)

        elif self.mode.lower() == 'hard':
            self.hard_mode()

        else:
            self.easy_mode()

    def hard_mode(self):
        random.shuffle(self.random_set)
        for item in self.random_set:
            _intersect = list(item & set(my_list))
            if len(_intersect) == 1:
                x, y = item - set(my_list)
                if x in self.my_play_history and y in self.my_play_history:
                    self.moves.remove(_intersect[0])
                    self.my_play_history.append(_intersect[0])
                    return self.update_board(_intersect[0], self.board)
        for item in self.random_set:
            _intersect = list(item & set(my_list))
            if len(_intersect) == 1:
                x, y = item - set(my_list)
                if x not in self.my_play_history and y not in self.my_play_history:
                    self.moves.remove(_intersect[0])
                    self.my_play_history.append(_intersect[0])
                    return self.update_board(_intersect[0], self.board)

            elif len(_intersect) == 2:
                x = item - set(my_list)
                if x in self.my_play_history:
                    y, z = _intersect
                    if y in my_list and z in my_list:
                        player_number = random.choice(_intersect)
                        self.moves.remove(player_number)
                        self.my_play_history.append(player_number)
                        return self.update_board(player_number, self.board)
            else:
                continue
        self.easy_mode()

    def easy_mode(self):
        player_number = random.choice(self.moves)
        self.moves.remove(player_number)
        self.my_play_history.append(player_number)
        return self.update_board(player_number, self.board)

    def update_board(self, value, board):
        for row in board:
            for item in range(3):
                if row[item] == value:
                    row[item] = self.player_id
                    break

    def check_status(self):
        if self.win_check(self.board):
            print(f'{self.player_name} won!')
            self.score[self.player_name] += 1
            return True
        return False


while True:
    player1_name = input('Enter your name to play against Frontbot: ')
    try:
        if player1_name.lower() == 'frontbot':
            raise ValueError('Oops! Frontbot is my name. Enter your name.')
    except ValueError as err:
        print(err)
        continue
    else:
        break

player2_name = 'Frontbot'
record = {player1_name: 0, player2_name: 0, 'draw': 0}
trial = True
counter = random.choice([1, 0])
while trial:
    template = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    turn = 9
    frontbot_play_history = []
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = T3Game(player1_name, my_list, template, record, winning_check, player_id='X')
    player2 = T3Game(player2_name, my_list, template, record, winning_check, player_id='O',
                     my_play_history=frontbot_play_history, mode='hard', )
    player = [player1, player2]
    counter += 1
    a = counter % 2
    b = 1 - a

    while turn:
        if turn % 2 == 0:
            render_template(template)
            print(player[a].movement())
            turn -= 1
            if player[a].check_status():
                break
            elif turn == 0:
                record['draw'] += 1
        else:
            render_template(template)
            print(player[b].movement())
            turn -= 1
            if player[b].check_status():
                break
            elif turn == 0:
                record['draw'] += 1

    render_template(template)
    print(record)
    while True:
        play_again = input('do you want to play again?\nEnter Y to continue or N to stop: ')
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            trial = True
            break
        elif play_again.lower() == 'n' or play_again.lower() == 'no':
            trial = False
            break
        else:
            print('Invalid input!')
            continue

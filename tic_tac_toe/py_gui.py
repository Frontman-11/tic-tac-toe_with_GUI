import random
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5 import uic


class TTTUI(QWidget):
    button = []
    my_play_history = []
    random_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    def __init__(self, player_name, score, mode='easy'):
        super().__init__()
        uic.loadUi('tttGUI1.ui', self)
        self.show()
        self.button = [self.pushButton_1, self.pushButton_2, self.pushButton_3,
                       self.pushButton_4, self.pushButton_5, self.pushButton_6,
                       self.pushButton_7, self.pushButton_8, self.pushButton_9,
                       ]
        self.player_name.setText(player_name)
        self.score = score
        self.trial_num.setText(str(self.score['trial']))
        self.mode = mode
        self.quit_btn.clicked.connect(lambda: sys.exit(0))
        self.new_game_btn.clicked.connect(lambda: self.close())

    def congratulatory_message(self, any_button):
        message = QMessageBox()
        message.addButton(QMessageBox.Abort)
        message.addButton(QMessageBox.Ok)
        message.setStyleSheet('background-color: rgb(170, 170, 127);')
        if any_button.text() == 'X':
            message.setText(f'Congratulations {self.player_name.text()}, you won!\nWould you like to play again?')
            self.score[self.player_name.text()] += 1
            self.player_score.setText(str(self.score[self.player_name.text()]))
            status = message.exec_()
            if status == 1024:
                return 'continue'
            return 'exit'
        elif any_button.text() == 'O':
            message.setText(f'OOps! Do better next time {self.player_name.text()}\nWould you like to play again?')
            self.score[self.frontbot.text()] += 1
            self.frontbot_score.setText(str(self.score[self.frontbot.text()]))
            status = message.exec_()
            if status == 1024:
                return 'continue'
            return 'exit'

    def check_winning(self):
        if (self.pushButton_1.text() == self.pushButton_2.text() == self.pushButton_3.text()) and \
                (self.pushButton_3.text() == 'X' or self.pushButton_3.text() == 'O'):
            return self.congratulatory_message(self.pushButton_2)
        if (self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text()) and \
                (self.pushButton_6.text() == 'X' or self.pushButton_6.text() == 'O'):
            return self.congratulatory_message(self.pushButton_5)
        if (self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text()) and \
                (self.pushButton_9.text() == 'X' or self.pushButton_9.text() == 'O'):
            return self.congratulatory_message(self.pushButton_8)
        if (self.pushButton_1.text() == self.pushButton_4.text() == self.pushButton_7.text()) and \
                (self.pushButton_7.text() == 'X' or self.pushButton_7.text() == 'O'):
            return self.congratulatory_message(self.pushButton_4)
        if (self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text()) and \
                (self.pushButton_8.text() == 'X' or self.pushButton_8.text() == 'O'):
            return self.congratulatory_message(self.pushButton_5)
        if (self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text()) and \
                (self.pushButton_9.text() == 'X' or self.pushButton_9.text() == 'O'):
            return self.congratulatory_message(self.pushButton_6)
        if (self.pushButton_1.text() == self.pushButton_5.text() == self.pushButton_9.text()) and \
                (self.pushButton_9.text() == 'X' or self.pushButton_9.text() == 'O'):
            return self.congratulatory_message(self.pushButton_5)
        if (self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text()) and \
                (self.pushButton_7.text() == 'X' or self.pushButton_7.text() == 'O'):
            return self.congratulatory_message(self.pushButton_5)

    def play(self, play_first):
        self.score['trial'] += 1
        self.trial_num.setText(str(self.score['trial'] - 1))
        self.player_score.setText(str(self.score[self.player_name.text()]))  # keeping score track
        self.frontbot_score.setText(str(self.score[self.frontbot.text()]))  # keeping score track
        self.my_play_history = []  # for reinitialization
        history = []
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        frontbot_start = play_first

        def easy_mode():
            i = random.choice(my_list)
            update_items(i)

        def update_items(_i):
            n = self_list.index(_i)
            my_list.remove(_i)
            self.my_play_history.append(_i)
            self.button[n].setText('O')
            return 0

        if frontbot_start:
            easy_mode()

        def button_on_click():
            self.button[0].clicked.connect(lambda: print_out(self.button[0], 0))
            self.button[1].clicked.connect(lambda: print_out(self.button[1], 1))
            self.button[2].clicked.connect(lambda: print_out(self.button[2], 2))
            self.button[3].clicked.connect(lambda: print_out(self.button[3], 3))
            self.button[4].clicked.connect(lambda: print_out(self.button[4], 4))
            self.button[5].clicked.connect(lambda: print_out(self.button[5], 5))
            self.button[6].clicked.connect(lambda: print_out(self.button[6], 6))
            self.button[7].clicked.connect(lambda: print_out(self.button[7], 7))
            self.button[8].clicked.connect(lambda: print_out(self.button[8], 8))

        def print_out(btn, index):
            if not btn.text():
                if index not in history:
                    history.append(index)
                    btn.setText('X')
                    my_list.remove(self_list[index])

                    status = self.check_winning()
                    if status == 'continue':
                        self.close()
                        return 0
                    elif status == 'exit':
                        sys.exit(0)

                    if self.mode.lower() == 'hard':
                        try:
                            random.shuffle(self.random_set)
                            for item in self.random_set:
                                _intersect = list(item & set(my_list))
                                if len(_intersect) == 1:
                                    x, y = item - set(my_list)
                                    if x in self.my_play_history and y in self.my_play_history:
                                        update_items(_intersect[0])
                                        status = self.check_winning()
                                        if status == 'continue':
                                            self.close()
                                            return 0
                                        elif status == 'exit':
                                            sys.exit(0)
                            for item in self.random_set:
                                _intersect = list(item & set(my_list))
                                if len(_intersect) == 1:
                                    x, y = item - set(my_list)
                                    if x not in self.my_play_history and y not in self.my_play_history:
                                        update_items(_intersect[0])
                                        return 0
                                elif len(_intersect) == 2:
                                    x = item - set(my_list)
                                    if x in self.my_play_history:
                                        y, z = _intersect
                                        if y in my_list and z in my_list:
                                            player_number = random.choice(_intersect)
                                            update_items(player_number)
                                            return 0
                                else:
                                    continue
                            easy_mode()
                            return 0
                        except IndexError:
                            return 0
                    else:
                        try:
                            easy_mode()
                            return 0
                        except IndexError:
                            return 0

        button_on_click()


turn = True
starter = random.choice([True, False])
score_board = {'Frontbot': 0, 'Priscilla': 0, 'trial': 0}


def main(arg_starting_player):
    app = QApplication(sys.argv)
    window = TTTUI('Priscilla', score_board, mode='hard')
    window.play(arg_starting_player)
    app.exec_()


if __name__ == '__main__':
    while turn:
        starter = not starter
        starting_player = starter
        main(starting_player)

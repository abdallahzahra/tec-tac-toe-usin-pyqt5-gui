#python -m pip install pyqt5 --user
from PyQt5 import QtWidgets,QtGui
from PyQt5.uic import loadUiType
from user_names_dialog import PlayerNamesDialog
UiClass, no_need_for_it = loadUiType("game_form.ui")


class TickTackToo(QtWidgets.QMainWindow, UiClass):
    def __init__(self):
        super(TickTackToo, self).__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(lambda : self.buttons_handler(self.btn1, 1))
        self.btn2.clicked.connect(lambda : self.buttons_handler(self.btn2, 2))
        self.btn3.clicked.connect(lambda : self.buttons_handler(self.btn3, 3))
        self.btn4.clicked.connect(lambda : self.buttons_handler(self.btn4, 4))
        self.btn5.clicked.connect(lambda : self.buttons_handler(self.btn5, 5))
        self.btn6.clicked.connect(lambda : self.buttons_handler(self.btn6, 6))
        self.btn7.clicked.connect(lambda : self.buttons_handler(self.btn7, 7))
        self.btn8.clicked.connect(lambda : self.buttons_handler(self.btn8, 8))
        self.btn9.clicked.connect(lambda : self.buttons_handler(self.btn9, 9))

        self.__buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5,self.btn6,self.btn7,self.btn8, self.btn9]
        self.start_btn.clicked.connect(self.start_game)
        self.is_game_started = False
        self._win_based_on = ""
        self.game_board=["" for i in range(9)]
        self.num_of_clicks = 0
        self.current_player = 1
        self.selected_char_player1 = ""
        self.selected_char_player2 = ""
        self.show()
    
    def buttons_handler(self, btn ,pos):
        if self.is_game_started:
            btn.setEnabled(False)
            self.num_of_clicks += 1
            if self.current_player == 1:
                btn.setText(self.selected_char_player1)
                self.current_player = 2
                self.game_board[pos-1] = self.selected_char_player1
                btn.setStyleSheet("background-color:blue;")
            else:
                btn.setText(self.selected_char_player2)
                self.current_player = 1
                self.game_board[pos-1] = self.selected_char_player2
                btn.setStyleSheet("background-color:red;")
            self.player_lbl.setText(f"player {self.pleyers_names[self.current_player-1]}")

            if self.winning_validation():
                pix_map = QtGui.QPixmap(r"images/Smiley Face With Thumbs Up Cartoon.png")
                pix_map = pix_map.scaled(150, 100)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("congrateulation")
                msg.setIconPixmap(pix_map)
                winner = ""
                if self.selected_char_player1.lower() in self._win_based_on :
                    winner = self.pleyers_names[0]
                else:
                    winner = self.pleyers_names[1]

                msg.setText(f"congrateulation {winner}, you won the game.")
                msg.exec_()
                self.start_btn.setText("try agin")
                self.start_btn.setStyleSheet("background-color:red;")
                self.start_btn.setEnabled(True)
                self.is_game_started = False
            elif self.num_of_clicks == 9:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("try again.")
                msg.setText("congrateulation, try again .")
                msg.exec_()
                self.start_btn.setText("try agin")
                self.start_btn.setStyleSheet("background-color:red;")
                self.start_btn.setEnabled(True)
                self.is_game_started = False


    
    def winning_validation(self):
        # 0:3 , 3:6 , 6:9
        available_options = ["ooo","xxx"]
        # raw 
        for i in range(0,9,3):
            row_content = "".join(self.game_board[i:i+3]).lower()
            if row_content in available_options:
                self._win_based_on = row_content
                return True 
        # cols 
        for i in range(0,3):
            #00x xxx oox
            col_content = "".join(self.game_board[i::3]).lower()
            if col_content in available_options:
                self._win_based_on = col_content
                return True
        # diagonals 
        dial1 = self.game_board[0] + self.game_board[4] + self.game_board[8]
        dial1 = dial1.lower()
        if dial1 in available_options:
            self._win_based_on = dial1 
            return True
        dial2 = self.game_board[2] + self.game_board[4] + self.game_board[6]
        dial2 = dial2.lower()
        if dial2 in available_options:
            self._win_based_on = dial2
            return True
        return False

    def start_game(self):
        names_dialog = PlayerNamesDialog()
        names_dialog.exec_()
        self.pleyers_names = names_dialog.get_players_names()
        self.start_btn.setEnabled(False)
        self.is_game_started = True
        for button in self.__buttons:
            button.setEnabled(True)
            button.setText("")
            button.setStyleSheet("background-color:black;")
        if self.o_radio.isChecked():
            self.selected_char_player1 = "O"
            self.selected_char_player2 = "X"
        else:
            self.selected_char_player1 = "X"
            self.selected_char_player2 = "O"

        self.start_btn.setText("started.")
        self.start_btn.setStyleSheet("background-color:green;")
        self.game_board=["" for i in range(9)]
        self.num_of_clicks = 0
        self.current_player = 1
        self.player_lbl.setText(f"player {self.pleyers_names[self.current_player-1]}")
    

app = QtWidgets.QApplication([])
main_app = TickTackToo()
app.exec_()

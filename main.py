from PyQt5 import  QtWidgets
from  zahra import  Ui_btn
class calculator (QtWidgets.QMainWindow , Ui_btn):
    def __init__(self):
        super(calculator, self).__init__()
        self.setupUi(self)
        self.ptn.clicked.connect(lambda :self.buttons_handler(self.ptn,1))
        self.ptn_2.clicked.connect(lambda :self.buttons_handler(self.ptn_2,1))
        self.ptn_3.clicked.connect(lambda :self.buttons_handler(self.ptn_3,1))
        self.ptn_4.clicked.connect(lambda :self.buttons_handler(self.ptn_4,1))
        self.ptn_5.clicked.connect(lambda :self.buttons_handler(self.ptn_5,1))
        self.ptn_6.clicked.connect(lambda :self.buttons_handler(self.ptn_6,1))
        self.ptn_7.clicked.connect(lambda :self.buttons_handler(self.ptn_7,1))
        self.ptn_8.clicked.connect(lambda :self.buttons_handler(self.ptn_8,1))
        self.ptn_9.clicked.connect(lambda :self.buttons_handler(self.ptn_9,1))
        self.is_game_started=False
        self.start_button.clicked.connect(self.start_game)
        self.current_player=1
        self.selected_char_player1=""
        self.selected_char_player2 = ""
        self.setWindowTitle("tektaktoo")

        self.show()

    def buttons_handler(self,btn,pos):
        if self.is_game_started :
            btn.setEnabled(False)
            if self.current_player==1:
                btn.setText(self.selected_char_player1)
                self.current_player=2
                btn.setStyleSheet("background-color:blue;")
            else:
                btn.setText(self.selected_char_player2)
                self.current_player = 1
                btn.setStyleSheet("background-color:red;")
    def start_game(self):
        self.start_button.setEnabled(False)
        self.is_game_started = True
        if self.o_radio.isChecked():
            self.selected_char_player1="O"
            self.selected_char_player2 = "X"
        else :
            self.selected_char_player1 = "X"
            self.selected_char_player2 = "O"

        self.start_button.setStyleSheet("background-color:green;")



app = QtWidgets.QApplication([])
calculator_app=calculator()
app.exec_()

















# w=QtWidgets.QMainWindow()
# w.setWindowTitle("hello")
#
#ggogle indstall
#python -m pip install PyQt5Designer --user
#pyuic5 main_view

from PyQt5 import QtWidgets,QtGui
from PyQt5.uic import loadUiType
UiClass, no_need_for_it = loadUiType("dialog_form.ui")


class PlayerNamesDialog(QtWidgets.QDialog, UiClass):
    def __init__(self):
        super(PlayerNamesDialog, self).__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.store_names)
        self.__player1_name = ""
        self.__player2_name = ""
    
    def store_names(self):
        self.__player1_name = self.player1_line.text()
        self.__player2_name = self.player2_line.text()
        self.accept()
    
    def get_players_names(self):
        return self.__player1_name.capitalize() , self.__player2_name.capitalize()

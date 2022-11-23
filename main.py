import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password 

user1 = User("ardanozpolat", 123456)

users = [user1]

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def loginfunction(self, users):
        username = self.username.text()
        password = self.password.text()
        
        for i in range(0, 5):
        
            if(users[i].username == username and users[i].password == password):
                print("Hos geldin ", username)

app = QApplication(sys.argv)
mainWindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow) 
widget.setFixedWidth(700)
widget.setFixedHeight(500)
widget.show()
app.exec_()
import pickle
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)


class Communicate(QObject):
    closeApp = pyqtSignal()


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.name = ""
        self.age = ""
        self.score = ""
        self.amount = ""
        self.keyname = "Name"
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        # Set Window
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # Set Label
        name = QLabel("Name: ", self)
        age = QLabel("Age: ", self)
        score = QLabel("Score: ", self)
        amount = QLabel("Amount: ", self)
        key = QLabel("Key: ", self)
        result = QLabel("Result: ", self)

        # Set Line Editor
        nameEdit = QLineEdit(self)
        nameEdit.textChanged[str].connect(self.name_onChanged)
        ageEdit = QLineEdit(self)
        ageEdit.textChanged[str].connect(self.age_onChanged)
        scoreEdit = QLineEdit(self)
        scoreEdit.textChanged[str].connect(self.score_onChanged)
        amountEdit = QLineEdit(self)
        amountEdit.textChanged[str].connect(self.amount_onChanged)

        # Set Text Editor
        self.resultEdit = QTextEdit(self)

        # Set Combo Box
        keyCombo = QComboBox(self)
        keyCombo.addItem("Name")
        keyCombo.addItem("Age")
        keyCombo.addItem("Score")
        keyCombo.activated[str].connect(self.onActivated)

        # Set Button
        addBtn = QPushButton("Add")
        addBtn.clicked.connect(self.addScoreDB)
        delBtn = QPushButton("Del")
        delBtn.clicked.connect(self.delScoreDB)
        fndBtn = QPushButton("Find")
        fndBtn.clicked.connect(self.findScoreDB)
        incBtn = QPushButton("Inc")
        incBtn.clicked.connect(self.incScoreDB)
        shwBtn = QPushButton("Show")
        shwBtn.clicked.connect(self.showScoreDB)

        # Initialize Layout
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name)
        hbox1.addWidget(nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(keyCombo)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addBtn)
        hbox3.addWidget(delBtn)
        hbox3.addWidget(fndBtn)
        hbox3.addWidget(incBtn)
        hbox3.addWidget(shwBtn)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        self.show()

    def onActivated(self, text):
        self.keyname = text

    def mousePressEvent(self, event):
        self.writeScoreDB()
        self.c.closeApp.emit()

    def name_onChanged(self, text):
        self.name = text

    def age_onChanged(self, text):
        self.age = text

    def score_onChanged(self, text):
        self.score = text

    def amount_onChanged(self, text):
        self.amount = text

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        resultStr = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.keyname]):
            for attr in sorted(p):
                resultStr += attr + " = " + str(p[attr]) + "        "
            resultStr += "\n"

        self.resultEdit.setText(resultStr)

    def findScoreDB(self):
        resultStr = ""
        DB = self.scoredb
        for i in range(len(DB)):
            if DB[i]["Name"] == self.name:
                for j in DB[i]:
                    resultStr += j + " = " + str(DB[i][j]) + "        "
                resultStr += "\n"

        self.resultEdit.setText(resultStr)

    def delScoreDB(self):
        DB = self.scoredb
        for i in range(len(DB)).__reversed__():
            if DB[i]['Name'] == self.name:
                DB.remove(DB[i])

        self.showScoreDB()

    def addScoreDB(self):
        name = self.name
        age = self.age
        score = self.score

        record = {'Name': name, 'Age': int(age), 'Score': int(score)}
        self.scoredb += [record]

        self.showScoreDB()

    def incScoreDB(self):
        DB = self.scoredb
        name = self.name
        amount = self.amount
        for i in range(len(DB)):
            if DB[i]['Name'] == name:
                DB[i]['Score'] = int(DB[i]['Score']) + int(amount)

        self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

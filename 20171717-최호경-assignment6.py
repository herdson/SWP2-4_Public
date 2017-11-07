import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Communicate(QObject):
    closer = pyqtSignal()

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.tempkey = 'Name'
        self.name = ""
        self.age = ""
        self.score = ""
        self.amount = ""
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

        
    def initUI(self):

        #Init signals
        self.c = Communicate()
        self.c.closer.connect(self.close)
        
        self.setGeometry(200, 100, 700, 400)
        self.setWindowTitle('20171717-최호경-Assignment6')

        #Init texts
        Badd = QPushButton("Add",self)
        Badd.clicked.connect(self.addScoreDB)
        Bshow = QPushButton("Show",self)
        Bshow.clicked.connect(self.showScoreDB)
        Binc = QPushButton("Inc",self)
        Binc.clicked.connect(self.incScoreDB)
        Bdel = QPushButton("Del",self)
        Bdel.clicked.connect(self.delScoreDB)
        Bfind = QPushButton("Find",self)
        Bfind.clicked.connect(self.findScoreDB)

        Tname = QLabel("Name :",self)
        Tage = QLabel("Age :",self)
        Tscore = QLabel("Score :",self)
        Tamount = QLabel("Amout :",self)
        Tkey = QLabel('Key', self)
        sr = QLabel("Result:",self)

        combokey = QComboBox(self)
        combokey.addItem('Name')
        combokey.addItem('Age')
        combokey.addItem('Score')
        combokey.activated[str].connect(self.Detection)

        #Init layouts
        buttlay = QHBoxLayout()
        inputlay = QHBoxLayout()


        #Capsule layouts
        inlay = QHBoxLayout()
        relay = QHBoxLayout()
        showrlay = QHBoxLayout()
        totallayout = QVBoxLayout()

        #Buttons
        buttlay.addWidget(Badd)
        buttlay.addWidget(Bshow)
        buttlay.addWidget(Bdel)
        buttlay.addWidget(Binc)
        buttlay.addWidget(Bfind)

        #Init text typers
        inscore = QLineEdit(self)
        inscore.textChanged[str].connect(self.scorechanger)
        inage = QLineEdit(self)
        inage.textChanged[str].connect(self.agechanger)
        inname = QLineEdit(self)
        inname.textChanged[str].connect(self.namechanger)
        inamount = QLineEdit(self)
        inamount.textChanged[str].connect(self.amountchanger)
        self.showr = QTextEdit(self)

        #Line box layout
        inputlay.addWidget(Tname)
        inputlay.addWidget(inname)
        inputlay.addWidget(Tage)
        inputlay.addWidget(inage)
        inputlay.addWidget(Tscore)
        inputlay.addWidget(inscore)
        inputlay.addWidget(Tamount)
        inputlay.addWidget(inamount)
        inputlay.addWidget(Tkey)
        inputlay.addWidget(combokey)
        relay.addWidget(self.showr)
        showrlay.addWidget(sr)

        inlay.addLayout(inputlay)
        totallayout.addLayout(inlay)
        totallayout.addLayout(buttlay)
        totallayout.addLayout(showrlay)
        totallayout.addLayout(relay)


        self.setLayout(totallayout)
        self.show()

    def Detection(self , text):
        self.tempkey = text

    def namechanger(self, text):
        self.name = text
    def agechanger(self,text):
        self.age = text
    def scorechanger(self, text):
        self.score = text
    def amountchanger(self, text):
        self.amount = text

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return self.scoredb

        try:
            self.scoredb =  pickle.load(fH)
            for p in self.scoredb:
                p['Age'] = int(p['Age'])
                p['Score'] = int(p['Score'])
        except:
            print('Empty DB - ', self.dbfilename)
        else:
            print("Open DB - ", self.dbfilename)
        fH.close()
        return self.scoredb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def addScoreDB(self):
        name = self.name
        score = self.score
        age = self.age

        record = {'Name' : name, 'Age' : int(age), 'Score' : int(score)}
        self.scoredb += [record]
        self.showScoreDB()

    def showScoreDB(self):
        stin = ''
        for p in sorted(self.scoredb, key = lambda i : i[self.tempkey]):
            for x in sorted(p):
                stin += x +' = ' + str(p[x]) + "               "
            stin += '\n'
        self.showr.setText(stin)

    def findScoreDB(self):
        show = []
        stin = ''
        name = self.name
        for k in self.scoredb:
            if k['Name'] == name:
                show.append(k['Name'] + '  Age :  ' + str(k['Age']) + '  Score :  ' + str(k['Score']))
        for x in show:
            stin += (x + '\n')
        self.showr.setText(stin)

    def delScoreDB(self):
        trap = 0
        while trap < len(self.scoredb):
            if self.scoredb[trap]['Name'] == self.name:
                self.scoredb.remove(self.scoredb[trap])
            else:
                trap += 1
        self.showScoreDB()

    def incScoreDB(self):
        amount = self.amount
        trap = 0
        while trap < len(self.scoredb):
            if self.scoredb[trap]['Name'] == self.name:
                self.scoredb[trap]['Score'] += int(amount)
                trap += 1
            else:
                trap += 1
        self.showScoreDB()



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())






from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class Ui_Widget(object):
    
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")

        #tabela numeryczna
        self.widok = QTableView()

        #przyciski 
        self.logujBtn  = QPushButton("Za&loguj")
        self.koniecBtn = QPushButton("&Koniec")

        #układ przycisków

        uklad = QHBoxLayout()
        uklad.addWidget(self.logujBtn)
        uklad.addWidget(self.koniecBtn)

        #główny układ okna

        ukladV = QVBoxLayout(self)
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)

        #właściwości widgetu

        self.setWindowTitle("Prosta lista zadań")
        self.resize(500, 300)


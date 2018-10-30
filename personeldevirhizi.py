import sys
from PyQt4.QtGui import*
from PyQt4.QtCore import *
class Hesaplama(QDialog):
    def __init__(self,ebeveyn=None):
        super(Hesaplama,self).__init__(ebeveyn)

        grid=QGridLayout()

        grid.addWidget(QLabel("işten ayrılan sayısı:"),0,0)

        self.ayrilan=QLineEdit()
        grid.addWidget(self.ayrilan,0,1)

        grid.addWidget(QLabel("ortalama çalışan sayısı:"),1,0)

        self.calisan=QLineEdit()
        grid.addWidget(self.calisan,1,1)

        grid.addWidget(QLabel("personel devir hızı:"),3,0)

        self.devir=QLabel("")
        grid.addWidget(self.devir,4,1)


        hesaplaDugme=QPushButton("hesapla")
        grid.addWidget(hesaplaDugme,3,1)
        self.connect(hesaplaDugme,SIGNAL('pressed()'),self.hesapla)

        self.setLayout(grid)

        self.setWindowTitle("personel devir hızı hesaplama")
        self.resize(250,150)

    def hesapla(self):
        a=int(self.ayrilan.text())
        c=int(self.calisan.text())
        
        hiz=(a/c)*100
        self.devir.setText('<font color="red"><b>%0.2f</b></font>'%hiz)

        
uygulama=QApplication([])
pencere=Hesaplama()
pencere.show()
uygulama.exec_
        

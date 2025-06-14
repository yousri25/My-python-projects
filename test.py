from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

def play():
    n=int(form.s1.text())
    if(divisible(n)==True):
        form.s2.setText("est divisible par 7")
    else:
        form.s2.setText("n'est pas divisible par 7")


def divisible(n):
    while(len(str(n))!=1):
        n=abs((n//10)-(2*(n%10)))

    if(n==7):
        return(True)
    else:
        return(False)
    
    
    
app = QApplication([])
form = loadUi ("2.ui")
form.show()
form.b1.clicked.connect (play)
app.exec_()
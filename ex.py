from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
res = ""
def calc():
    global res
    try:
        res2 = eval(res) 
        form.result.setText(str(res2))  
    except ZeroDivisionError:
        form.result.setText("Error: Division by zero")  
    except (SyntaxError, TypeError, NameError):
        form.result.setText("Error: Invalid input")  
def add_value():
    global res
    button = window.sender()
    value = button.text()
    res += value
    form.result.setText(str(res))
def reset():
    global res
    res = ""
    form.result.setText("")
app = QApplication([])
window = QMainWindow()
form = loadUi("exp.ui", window)
form.n1.clicked.connect(add_value)  
form.n2.clicked.connect(add_value)  
form.n3.clicked.connect(add_value)
form.n4.clicked.connect(add_value)  
form.n5.clicked.connect(add_value)  
form.n6.clicked.connect(add_value)
form.n7.clicked.connect(add_value)  
form.n8.clicked.connect(add_value)  
form.n9.clicked.connect(add_value)
form.plus.clicked.connect(add_value)  
form.moin.clicked.connect(add_value)  
form.fois.clicked.connect(add_value)
form.sur.clicked.connect(add_value)
form.n0.clicked.connect(add_value)
form.verg.clicked.connect(add_value)
form.nc.clicked.connect(reset)
form.calc.clicked.connect(calc)
window.show()
app.exec_()
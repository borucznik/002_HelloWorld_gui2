import sys    
from PyQt5 import QtWidgets, QtCore  

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400, 200)
widget.setWindowTitle("Hello World with GUI")
widget.show()
exit(app.exec_())
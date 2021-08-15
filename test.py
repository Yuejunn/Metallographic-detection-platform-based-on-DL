import sys
from PyQt5 import QtWidgets
import main_widget



app = QtWidgets.QApplication(sys.argv)
mw = main_widget.MainWidget()
mw.show()

sys.exit(app.exec_())

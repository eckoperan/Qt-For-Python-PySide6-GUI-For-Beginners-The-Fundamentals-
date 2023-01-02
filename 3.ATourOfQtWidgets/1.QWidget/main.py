from PySide6.QtWidgets import QAppl
ication,QWidget
from rocketwidget import RockWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
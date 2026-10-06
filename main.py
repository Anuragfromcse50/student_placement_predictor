import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from student_placement_predictor.placement_ui import Ui_Dialog

app = QApplication(sys.argv)

window = QMainWindow()

ui = Ui_Dialog()
ui.setupUi(window)

window.show()

sys.exit(app.exec())

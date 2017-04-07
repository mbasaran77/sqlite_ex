
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
import sys

class MyGui(QWidget):
    """docstring for MyGui."""
    def __init__(self):
        super(MyGui, self).__init__()
        self.setGeometry(0,0,100,300)
        # self.resize(100,300)
        # self.move(100,100)
        self.init_Ui()

    def init_Ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("hello my gui")
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyGui()
    form.show()
    sys.exit(app.exec_)

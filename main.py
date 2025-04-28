import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox, QFileDialog, QProgressBar
from PySide6.QtCore import Qt


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.click_count = 0
        
        pushbutton = QPushButton("点我呀~")
        pushbutton.clicked.connect(self.on_pushbutton_clicked)

        pushbutton2 = QPushButton("About Qt")
        pushbutton2.clicked.connect(self.on_pushbutton2_clicked)

        label = QLabel("点击计数:")
        self.lineedit = QLineEdit("0")
        self.lineedit.setReadOnly(True)

        layout1 = QHBoxLayout()
        layout1.addWidget(label)
        layout1.addWidget(self.lineedit)

        layout2 = QHBoxLayout()
        layout2.addWidget(pushbutton2)
        layout2.addStretch()
        layout2.addWidget(pushbutton)

        layout = QVBoxLayout(self)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setWindowTitle("PySide6 Demo")
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.resize(300, 200)


    def on_pushbutton_clicked(self):
        self.click_count += 1
        self.lineedit.setText(f"{self.click_count}")

    def on_pushbutton2_clicked(self):
        QMessageBox.aboutQt(self, "关于Qt")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
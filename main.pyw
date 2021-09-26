"""
version: 1.0
made by: Lavhran

"""

import sys
from os import startfile
from glob import glob as search
from random import choice as randchoice
from json import load as jsonL
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)

class Window(QWidget):
    def __init__(self, json, parent=None):
        super().__init__(parent)

        self.folder = json["folder"]       # path
        self.hfolders = json["hfolders"]   # hidden folders
        self.hfiles = json["hfiles"]
        self.acceptable = json["accepts"]  # accepted file types
        self.files = {}
        self.selected = ""
        self.find_files(self.folder)

        self.setWindowTitle("File-picker")
        self.setFixedSize(200, 120)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.setWindowIcon(QIcon("icon.png"))

        self.label = QLabel("Click the button get a file!")
        self.get_button = QPushButton("Random")
        self.run_button = QPushButton("Run")
        self.maker_label = QLabel("Made by Lavhran")

        self.maker_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maker_label.setStyleSheet("QLabel {color: #727272;}")

        if self.files:
            self.get_button.clicked.connect(self.get_file)
            self.run_button.clicked.connect(self.run_file)
        else:
            self.label.setText("Couldn't find any files!")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.get_button)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.maker_label)
        self.setLayout(self.layout)

    def get_file(self):
        tmp = randchoice(list(self.files.keys()))
        self.selected = self.files[tmp]
        self.label.setText(tmp)

    def run_file(self):
        startfile(self.selected)
        exit()

    def find_files(self, next):
        tmp = search(next)
        if not tmp: return False
        for i in tmp:
            if i[(len(next)-1):] in self.hfolders: continue
            try:
                test = self.find_files(f"{i}/*")
                if not test: raise FileNotFoundError
            except:
                if not i[-4:] in self.acceptable: continue
                if i[(len(next) - 1):-4] in self.hfiles: continue
                self.files[i[(len(next) - 1):-4]] = i


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        config = open("config.json", "r")
        root = Window(jsonL(config))
        root.show()
    except: exit()
    sys.exit(app.exec())


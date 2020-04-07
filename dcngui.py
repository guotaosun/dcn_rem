#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ZetCode PyQt5 tutorial
In this example, we create a simple
window in PyQt5.
author: sungt
last edited: January 20200403
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()
        label = QLabel("Set Style:",self)
        combo = QComboBox(self)
        combo.addItems(QStyleFactory.keys())
        # 选择当前窗口风格
        index = combo.findText(QApplication.style().objectName(), Qt.MatchFixedString)
        # 设置当前窗口风格
        combo.setCurrentIndex(index)
        combo.activated[str].connect(self.onCurrentIndexChanged)

        self.layout.addWidget(label)
        self.layout.addWidget(combo)

        self.setLayout(self.layout)
        self.setWindowTitle("Application Style")
        self.resize(300, 100)

    def onCurrentIndexChanged(self, style):
        QApplication.setStyle(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
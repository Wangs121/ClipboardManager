# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:59:41 2021

@author: 27766
"""

import pyperclip
#read clipvord
#s= pyperclip.paste()

#result = 's'
#pyperclip.copy(result)

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ClipboardWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.history=''
        self.setMinimumSize(QSize(440, 240))    
        self.setWindowTitle("剪切板优化工具") 
        self.setWindowIcon(QtGui.QIcon('clipboard.png'))
        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("软件会自动清除剪切板内容中的换行符\n此页面会显示剪切板中内容\n")
        self.b.move(10,10)
        self.b.resize(400,200)
        QApplication.clipboard().dataChanged.connect(self.clipboardChanged)

    # Get the system clipboard contents
    def clipboardChanged(self):
        text = QApplication.clipboard().text()
        if self.history != text:
            self.history=text
            #print(text)
            #print(repr(text))
            text = text.replace("-\n", "").replace("\n", " ")
            QApplication.clipboard().blockSignals(True)
            pyperclip.copy(text)
            # QApplication.clipboard().setText(text)
            print(QApplication.clipboard().text())
            self.b.setPlainText(text + '\n')
            QApplication.clipboard().blockSignals(False)

        

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ClipboardWindow()
    mainWin.show()
    sys.exit( app.exec_() )


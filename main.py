# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from Ui_main import Ui_MainWindow

import Gbk2Big5All


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_choose_btn_clicked(self):
        print("1")
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "./kitdat/",
                                                  "All Files (*);;Text Files (*.txt)")

        if len(files) == 0:
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        for file in files:
            a = Gbk2Big5All.Gbk2Big5All(file)
            print(file + " 操作结果:" + str(a))

        print("文件筛选器类型: ", filetype)
        QMessageBox.about(self, "操作成功", '简繁转化完成')

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
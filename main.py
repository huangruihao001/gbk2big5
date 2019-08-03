# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

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
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "多文件选择",
                                                       self.cwd,  # 起始路径
                                                       "All Files (*)")

        if len(files) == 0:
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        for file in files:
            a = Gbk2Big5All.Gbk2Big5All(file)
            print(a)
        print("文件筛选器类型: ", filetype)

        QMessageBox.about(self, "操作成功", '简繁转化完成')

if __name__ == "__main__":
    import sys
    app = MainWindow(sys.argv)
    mainForm = MainWindow()
    mainForm.show()
    sys.exit(app.exec_())
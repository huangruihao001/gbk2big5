# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
import Resources.res

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
        self.setWindowTitle("简繁转换器")
        self.setWindowIcon(QIcon(':/ico/logo.ico'))  # 设置窗体标题图标
        self.label_2.setText("txt ini dat html xml mdb xls")  # 可进行简繁转换的文件后缀

    @pyqtSlot()
    def on_choose_folder_clicked(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "./kitdat")
        print(directory1)  # 打印文件夹路径
        if len(directory1) == 0:
            print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        a = Gbk2Big5All.Gbk2Big5All_folder(directory1)
        print(directory1 + " 操作结果:" + str(a))

        print("文件筛选器类型: ", directory1)
        QMessageBox.about(self, "操作成功", '简繁转化完成')

    @pyqtSlot()
    def on_choose_filename_clicked(self):
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "多文件选择",
                                                       "./kitdat/",
                                                       "All Files (*);;Text Files (*.txt)")
        if len(files) == 0:
            print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        for file in files:
            a = Gbk2Big5All.Gbk2Big5All_filename(file)
            print(file + " 操作结果:" + str(a))

        print("文件筛选器类型: ", filetype)
        QMessageBox.about(self, "操作成功", '简繁转化完成')

    @pyqtSlot()
    def on_choose_btn_clicked(self):
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
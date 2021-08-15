r"""
存放一些自定义窗体类
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Ui_my_message_dialog import Ui_MyMessageDialog
from Ui_my_help_dialog import Ui_MyHelpDialog


class My_message_dialog(QtWidgets.QDialog, Ui_MyMessageDialog):
    r"""点击按钮出现的提示窗口
    """

    def __init__(self, parent, title, message, size=(400, 300)):
        r"""可设置显示的消息message，以及窗体大小size
        """
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.resize(size[0], size[1])
        self.setWindowTitle(title)
        self.info_text.append(
            '<p align="center"><span style=" font-size:12pt; font-weight:400;">'+message+'</span></p>')

    def setMessage(self, message):
        r"""设置显示的消息message
        """
        self.info_text.clear()
        self.info_text.append(
            '<p align="center"><span style=" font-size:12pt; font-weight:400;">'+message+'</span></p>')

    @pyqtSlot()
    def on_ensure_pb_clicked(self):
        r"""按下确定按钮后关闭窗体
        """
        self.window().close()


class My_help_dialog(QtWidgets.QDialog, Ui_MyHelpDialog):
    def __init__(self, parent, size=(800, 600)):
        r"""弹出预设的帮助信息窗体（在ui文件里预设），
        可以传入size调整窗体大小
        """
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.resize(size[0], size[1])
        self.setWindowTitle('指纹输入格式说明')

    @pyqtSlot()
    def on_ensure_pb_clicked(self):
        r"""按下确定按钮后关闭窗体
        """
        self.window().close()

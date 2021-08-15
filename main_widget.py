r"""实现继承Ui_MainWindow的MainWidget类，在其图形界面的基础上实现交互式操作
"""
import Ui_main_window
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QRect, pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QBrush
from my_dialogs import My_help_dialog
from PyQt5.QtWidgets import QHeaderView
import math
import os
from my_styles import *

SHADOW_WIDTH = 10  # 窗口阴影宽度


class MainWidget(QtWidgets.QMainWindow, Ui_main_window.Ui_MainWindow):
    r"""继承Ui_MainWindow，在其图形界面的基础上实现交互式操作
    """

    def __init__(self, parent=None):
        r"""可指定父窗口parent
        """
        super(MainWidget, self).__init__(parent)
        self.setupUi(self)

        self.cwd = os.path.expanduser("~")
        self.set_list()  # 绑定页面切换信号
        self.leftList.setCurrentItem(self.leftList.item(0))  # 切换到第一页
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 隐藏背景框，非常重要

        self.last_w_size = self.window().size()
        self.max_size = None
        self.min_size = None

    ###################################### 重写父类函数 ######################################

    def paintEvent(self, e):
        r"""绘制窗口背景阴影
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillRect(QRect(SHADOW_WIDTH, SHADOW_WIDTH, self.width(
        )-2*SHADOW_WIDTH, self.height()-2*SHADOW_WIDTH), QBrush(Qt.white))
        color = QColor(50, 50, 50)
        for i in range(SHADOW_WIDTH):
            color.setAlpha(150 - math.sqrt(i) * 40)
            painter.setPen(color)
            painter.drawRoundedRect(SHADOW_WIDTH-i, SHADOW_WIDTH-i, self.width()-(
                SHADOW_WIDTH-i)*2, self.height() - (SHADOW_WIDTH - i) * 2, 4, 4)

    def resizeEvent(self, a0):
        r"""设置主页和关于我们页label自动resize
        """
        now_w_size = self.window().size()
        w_change = now_w_size.width() / self.last_w_size.width()
        h_change = now_w_size.height() / self.last_w_size.height()  # 随高度和宽度的平均值缩放
        change = (w_change + h_change) / 2
        new_size = self.home_label.size()
        new_size.setWidth(int(new_size.width() * change))
        new_size.setHeight(int(new_size.height() * change))
        if change > 1:  # 保证每次缩放的大小都是一样的,change只是用来判断放大还是缩小
            if self.max_size == None:
                self.max_size = new_size
            new_size = self.max_size
        elif change < 1:  # 初始化时候有一次等于1，要避开
            if self.min_size == None:
                self.min_size = new_size
            new_size = self.min_size

        self.home_label.resize(new_size)
        self.about_label.resize(new_size)
        self.last_w_size = now_w_size
        return super().resizeEvent(a0)

    ###################################### 辅助函数 ######################################

    def set_list(self):
        r"""绑定leftlist和各界面
        """
        self.leftList.currentItemChanged.connect(self.change_page)

    def change_page(self, current, previous):
        r"""响应界面切换
        """
        if current == None:
            current = previous
        self.pages.setCurrentIndex(self.leftList.row(current))

    ###################################### 槽函数 ######################################

    @pyqtSlot()
    def on_p_help_pb_clicked(self):
        r"""响应预测界面输入格式说明p_help_pb按钮点击事件
        """
        help_dialog = My_help_dialog(self)
        help_dialog.exec_()

    @pyqtSlot()
    def on_t_help_pb_clicked(self):
        r"""响应转换界面输入格式说明t_help_pb按钮点击事件
        """
        help_dialog = My_help_dialog(self)
        help_dialog.exec_()

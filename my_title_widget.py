r"""实现继承Ui_my_title_widget的MyTitleWidget的类，实现自定义标题栏
"""

import Ui_my_title_widget
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QSize, pyqtSlot
from PyQt5.QtGui import QIcon


class MyTitleWidget(QtWidgets.QWidget, Ui_my_title_widget.Ui_MyTitleWidget):
    def __init__(self, parent=None):
        r"""继承Ui_my_title_widget，可设置父窗体parent
        """
        super(MyTitleWidget, self).__init__(parent)
        self.setupUi(self)
        self.m_start = None  # 起点
        self.m_end = None  # 终点
        self.m_leftButtonPressed = False  # 鼠标左键按下标记

    ###################################### 重写父类函数 ######################################

    def mouseDoubleClickEvent(self, e):
        r"""鼠标双击标题栏则放大窗体
        """
        self.max_pb.clicked.emit()

    def mousePressEvent(self, e):
        r"""鼠标点击标题栏记录坐标
        """
        if e.button() == Qt.LeftButton:
            # print('press')
            self.m_leftButtonPressed = True  # 记录鼠标左键状态
            self.m_start = QPoint(e.x(), e.y())  # 记录鼠标在屏幕中的位置

    def mouseReleaseEvent(self, e):
        r"""鼠标松开标题栏记录清除记录坐标
        """
        if e.button() == Qt.LeftButton:
            # print('release')
            self.m_leftButtonPressed = False
            self.m_start = None
            self.m_end = None

    def mouseMoveEvent(self, e):
        r"""鼠标拖动标题栏移动整个窗体
        """
        if self.m_leftButtonPressed:
            self.m_end = e.pos() - self.m_start
            self.parentWidget().parentWidget().move(
                self.parentWidget().parentWidget().pos()+self.m_end)

    ###################################### 槽函数 ######################################

    @pyqtSlot()
    def on_max_pb_clicked(self):
        r"""点击按钮最大化窗体，再次点击最小化窗体
        """
        tmpicon = QIcon()
        if self.window().isMaximized():
            self.window().showNormal()
            tmpicon.addFile(":/imgs/kou.png", QSize(), QIcon.Normal, QIcon.Off)
            self.max_pb.setIcon(tmpicon)
            self.max_pb.setIconSize(QSize(30, 30))
        else:
            self.window().showMaximized()
            tmpicon.addFile(":/imgs/dkou.png",
                            QSize(), QIcon.Normal, QIcon.Off)
            self.max_pb.setIcon(tmpicon)
            self.max_pb.setIconSize(QSize(15, 15))

    @pyqtSlot()
    def on_close_pb_clicked(self):
        r"""点击按钮关闭窗体
        """
        self.window().close()

    @pyqtSlot()
    def on_min_pb_clicked(self):
        r"""点击按钮隐藏窗体
        """
        self.window().showMinimized()

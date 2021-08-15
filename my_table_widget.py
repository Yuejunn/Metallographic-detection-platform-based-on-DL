r"""可以在表头显示数学公式的QtableWidget
原作者：https://stackoverflow.com/questions/32035251/displaying-latex-in-pyqt-pyside-qtablewidget?noredirect=1&lq=1
完全复制的，就不给他写注释了。
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QStyleOptionHeader, QStyle
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QCursor, QImage, QPixmap


def mathTex_to_QPixmap(mathTex, fs):
    # ---- set up a mpl figure instance ----
    fig = plt.figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()
    # ---- plot the mathTex expression ----
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs)
    # ---- fit figure size to text artist ----
    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)
    text_bbox = t.get_window_extent(renderer)
    tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
    tight_fheight = text_bbox.height * fheight / fig_bbox.height
    fig.set_size_inches(tight_fwidth, tight_fheight)
    # ---- convert mpl figure to QPixmap ----
    buf, size = fig.canvas.print_to_buffer()
    qimage = QImage.rgbSwapped(QImage(buf, size[0], size[1],
                                      QImage.Format_ARGB32))
    qpixmap = QPixmap(qimage)
    return qpixmap


class MyTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(MyTableWidget, self).__init__(parent)

        self.setHorizontalHeader(MyHorizHeader(self))

    def setHorizontalHeaderLabels(self, headerLabels, fontsize):

        qpixmaps = []
        indx = 0
        for labels in headerLabels:
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            indx += 1

        self.horizontalHeader().qpixmaps = qpixmaps

        super(MyTableWidget, self).setHorizontalHeaderLabels(headerLabels)


class MyHorizHeader(QHeaderView):
    def __init__(self, parent):
        super(MyHorizHeader, self).__init__(Qt.Horizontal, parent)

        # self.setClickable(True)
        self.setStretchLastSection(True)

        self.qpixmaps = []

    def paintSection(self, painter, rect, logicalIndex):

        if not rect.isValid():
            return

        # ------------------------------ paint section (without the label) ----

        opt = QStyleOptionHeader()
        self.initStyleOption(opt)

        opt.rect = rect
        opt.section = logicalIndex
        opt.text = ""

        # ---- mouse over highlight ----
        mouse_pos = self.mapFromGlobal(QCursor.pos())
        if rect.contains(mouse_pos):
            opt.state |= QStyle.State_MouseOver

        # ---- paint ----

        painter.save()
        self.style().drawControl(QStyle.CE_Header, opt, painter, self)
        painter.restore()

        # ------------------------------------------- paint mathText label ----

        qpixmap = self.qpixmaps[logicalIndex]

        # ---- centering ----

        xpix = (rect.width() - qpixmap.size().width()) / 2. + rect.x()
        ypix = (rect.height() - qpixmap.size().height()) / 2.

        # ---- paint ----

        rect = QRect(xpix, ypix, qpixmap.size().width(),
                     qpixmap.size().height())
        painter.drawPixmap(rect, qpixmap)

    def sizeHint(self):
        baseSize = QHeaderView.sizeHint(self)

        baseHeight = baseSize.height()
        if len(self.qpixmaps):
            for pixmap in self.qpixmaps:
                baseHeight = max(pixmap.height() + 8, baseHeight)
        baseSize.setHeight(baseHeight)

        self.parentWidget().repaint()

        return baseSize

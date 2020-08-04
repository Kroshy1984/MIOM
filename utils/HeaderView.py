import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QApplication, QTableWidgetItem, QStyle, QStyleOptionHeader, \
    QTableView

from utils.tex_to_qpixmap import mathTex_to_QPixmap
from PyQt5 import QtGui, QtCore


class MyQTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(MyQTableWidget, self).__init__(parent)

        self.setHorizontalHeader(MyHorizHeader(self))

    def setHorizontalHeaderLabels(self, headerLabels, fontsize):

        qpixmaps = []
        indx = 0
        for labels in headerLabels:
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))            
            self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            print(indx, "-", qpixmaps[indx].size().width())
            indx += 1

        self.horizontalHeader().qpixmaps = qpixmaps

        super(MyQTableWidget, self).setHorizontalHeaderLabels(headerLabels)

class MyQTableView(QTableView):
    def __init__(self, parent=None):
        super(MyQTableWidget, self).__init__(parent)

        self.setHorizontalHeader(MyHorizHeader(self))

    def setHorizontalHeaderLabels(self, headerLabels, fontsize):

        qpixmaps = []
        indx = 0
        for labels in headerLabels:
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            self.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            print(indx, "-", qpixmaps[indx].size().width())
            indx += 1

        self.horizontalHeader().qpixmaps = qpixmaps

        super(MyQTableWidget, self).setHorizontalHeaderLabels(headerLabels)


class MyHorizHeader(QHeaderView):
    def __init__(self, parent):
        super(MyHorizHeader, self).__init__(QtCore.Qt.Horizontal, parent)
        print("MyHorizHeader parent", parent)
        # print(super(MyHorizHeader, self))
        self.setSectionsClickable(False)
        self.setStretchLastSection(True)

        self.qpixmaps = []

    def paintSection(self, painter, rect, logicalIndex):
        print("Called paintSection!")
        if not rect.isValid():
            return

        #------------------------------ paint section (without the label) ----

        opt = QStyleOptionHeader()
        self.initStyleOption(opt)

        opt.rect = rect
        opt.section = logicalIndex
        opt.text = ""

        #---- mouse over highlight ----

        mouse_pos = self.mapFromGlobal(QtGui.QCursor.pos())               
        if rect.contains(mouse_pos):
            opt.state |= QStyle.State_MouseOver

        #---- paint ----

        painter.save()        
        self.style().drawControl(QStyle.CE_Header, opt, painter, self)
        painter.restore()

        #------------------------------------------- paint mathText label ----

        qpixmap = self.qpixmaps[logicalIndex]

        #---- centering ----

        xpix = (rect.width() - qpixmap.size().width()) / 2. + rect.x()
        ypix = (rect.height() - qpixmap.size().height()) / 2.

        #---- paint ----

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

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MyQTableWidget()
    w.verticalHeader().hide()

    headerLabels = [
        '$C_{soil}=(1 - n) C_m + \\theta_w C_w$',
        '$k_{soil}=\\frac{\\sum f_j k_j \\theta_j}{\\sum f_j \\theta_j}$',
        '$\\lambda_{soil}=k_{soil} / C_{soil}$']

    w.setColumnCount(len(headerLabels))
    w.setHorizontalHeaderLabels(headerLabels, 12)
    w.setRowCount(3)
    w.setAlternatingRowColors(True)

    k = 1
    for j in range(3):
        for i in range(3):
            w.setItem(i, j, QTableWidgetItem('Value %i' % (k)))
            k += 1

    w.show()
    w.resize(700, 200)

    sys.exit(app.exec_())

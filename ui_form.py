# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1680, 647)
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(11)
        Widget.setFont(font)
        self.tb_table = QTableWidget(Widget)
        if (self.tb_table.columnCount() < 1):
            self.tb_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tb_table.setObjectName(u"tb_table")
        self.tb_table.setGeometry(QRect(10, 10, 161, 631))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.tb_table.setFont(font1)
        self.tb_table.setDragEnabled(False)
        self.tb_table.horizontalHeader().setVisible(False)
        self.tb_table.verticalHeader().setVisible(False)
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 10, 1491, 631))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.t_asm_in = QTableWidget(self.horizontalLayoutWidget)
        if (self.t_asm_in.columnCount() < 1):
            self.t_asm_in.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.t_asm_in.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.t_asm_in.setObjectName(u"t_asm_in")
        self.t_asm_in.setFont(font1)
        self.t_asm_in.horizontalHeader().setVisible(False)
        self.t_asm_in.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.t_asm_in)

        self.t_asm_tcg = QTableWidget(self.horizontalLayoutWidget)
        if (self.t_asm_tcg.columnCount() < 1):
            self.t_asm_tcg.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.t_asm_tcg.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.t_asm_tcg.setObjectName(u"t_asm_tcg")
        self.t_asm_tcg.setFont(font1)
        self.t_asm_tcg.horizontalHeader().setVisible(False)
        self.t_asm_tcg.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.t_asm_tcg)

        self.t_asm_out = QTableWidget(self.horizontalLayoutWidget)
        if (self.t_asm_out.columnCount() < 1):
            self.t_asm_out.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.t_asm_out.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.t_asm_out.setObjectName(u"t_asm_out")
        self.t_asm_out.setFont(font1)
        self.t_asm_out.horizontalHeader().setVisible(False)
        self.t_asm_out.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.t_asm_out)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Qemu tcg log viewer", None))
    # retranslateUi


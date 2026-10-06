# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'placement.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 0, 191, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 49, 16))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 40, 141, 26))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 49, 16))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 70, 113, 26))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 101, 20))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 110, 113, 26))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 81, 16))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 140, 113, 26))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 200, 81, 26))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"STUDENT PLACEMENT PREDICTOR", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Branch", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"SELECT BRANCH", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"CSE", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"EE", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"IT", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"ME", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"ECE", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"CE", None))

#if QT_CONFIG(accessibility)
        self.comboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"CGPA", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"No.of Internships", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"No.of Projects", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Predict", None))
    # retranslateUi


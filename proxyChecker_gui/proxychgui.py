# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProxyChecker.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import requests

class Ui_ProxyChecker(object):
    def setupUi(self, ProxyChecker):
        if not ProxyChecker.objectName():
            ProxyChecker.setObjectName(u"ProxyChecker")
        ProxyChecker.resize(362, 211)
        self.centralwidget = QWidget(ProxyChecker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 86, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 98, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 80, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 142, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 166, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 170, 75, 23))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 10, 113, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 40, 113, 20))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(230, 70, 113, 20))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(230, 130, 113, 20))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(230, 100, 113, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 170, 200, 20))
        ProxyChecker.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProxyChecker)

        QMetaObject.connectSlotsByName(ProxyChecker)
    # setupUi

    def retranslateUi(self, ProxyChecker):
        ProxyChecker.setWindowTitle(QCoreApplication.translate("ProxyChecker", u"ProxyChecker 1.0", None))
        self.label.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy type:", None))
        self.label_2.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy address", None))
        self.label_3.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy port", None))
        self.label_4.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy login (if required)", None))
        self.label_5.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy password (if required)", None))
        self.pushButton.setText(QCoreApplication.translate("ProxyChecker", u"Check proxy", None))
        self.label_6.setText("")
    # retranslateUi


class prch(QtWidgets.QMainWindow, Ui_ProxyChecker):  # Собираем класс с нашими основными действиями
  def __init__(self):
   super().__init__()
   self.setupUi(self)  # Создание формы и Ui (наш дизайн)
   self.show()  # Показать наше окно
   # прописывем реакции на кнопки
   self.pushButton.clicked.connect(self.check)


  def check(self):  # функция ввода данных для парсера
   PROXY = self.lineEdit_2.text() + ":" + self.lineEdit_3.text()
   try:
        req = self.lineEdit_5.text()
        if len(req) > 0:  # проверяем есть ли у прокси проверка имени\пароля
            proxies = {
            'https': self.lineEdit.text() + '://' + self.lineEdit_5.text() + ":" + self.lineEdit_4.text() + "@" + str(PROXY)  # собираем прокси
            }
        else:  # если прокси без имени\пароля
            proxies = {
            'https': self.lineEdit.text() + '://' + str(PROXY)  # собираем прокси
            }
        s = requests.Session()  # создаем сесиию
        s.proxies = proxies  # привязываем собранный прокси
        r = s.get('https://www.google.com/humans.txt')  # пытаемся получить доступ к адресу через собранный прокси
        self.label_6.setText("      Proxy " + str(PROXY) + " OK")
        self.label_6.setStyleSheet("background-color: lightgreen")
   except Exception as e:  # в случае ошибки
        self.label_6.setText("    Proxy " + str(PROXY) + " not OK")
        self.label_6.setStyleSheet("background-color: red")
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    prch_gui = prch()  # Сздание инстанса класса Калькулятор, который мы создадим далее
    sys.exit(app.exec_())  # Запуск

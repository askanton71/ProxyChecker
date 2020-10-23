# -*- coding: utf-8 -*-
import time
from threading import Thread
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import requests
import chardet
import os
import codecs
import webbrowser
import threading
import logging
from datetime import datetime
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)
thread_list = []

class Ui_ProxyChecker(object):
    def setupUi(self, ProxyChecker):
        if not ProxyChecker.objectName():
            ProxyChecker.setObjectName(u"ProxyChecker")
        ProxyChecker.resize(440, 431)
        self.centralwidget = QWidget(ProxyChecker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 180, 421, 231))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 190, 241, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 98, 16))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 90, 113, 20))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(270, 120, 113, 20))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 90, 80, 16))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 30, 113, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 150, 166, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(49, 29, 86, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 60, 113, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 120, 142, 16))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 190, 75, 23))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 150, 113, 20))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 421, 161))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 101, 16))
        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(120, 20, 221, 20))
        self.lineEdit_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(354, 20, 61, 23))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 60, 101, 16))
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.checkBox.setGeometry(QRect(110, 60, 70, 17))
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(170, 60, 70, 17))
        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(230, 60, 70, 17))
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(300, 60, 70, 17))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 90, 101, 16))
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 120, 111, 17))
        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(110, 90, 51, 20))
        self.lineEdit_7.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(110, 120, 51, 20))
        self.lineEdit_8.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 120, 191, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 90, 111, 23))
        ProxyChecker.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProxyChecker)

        QMetaObject.connectSlotsByName(ProxyChecker)

    # setupUi

    def retranslateUi(self, ProxyChecker):
        ProxyChecker.setWindowTitle(QCoreApplication.translate("ProxyChecker", u"ProxyChecker 2.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("ProxyChecker", u"SingleCheck", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy address", None))
        self.label_3.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy port", None))
        self.label_5.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy password (if required)", None))
        self.label.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy type:", None))
        self.label_4.setText(QCoreApplication.translate("ProxyChecker", u"Enter proxy login (if required)", None))
        self.pushButton.setText(QCoreApplication.translate("ProxyChecker", u"Check proxy", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ProxyChecker", u"GroupCheck", None))
        self.label_7.setText(QCoreApplication.translate("ProxyChecker", u"Path to proxy list file", None))
        self.lineEdit_6.setText("Enter path here..")
        self.pushButton_2.setText(QCoreApplication.translate("ProxyChecker", u"Browse", None))
        self.label_8.setText(QCoreApplication.translate("ProxyChecker", u"Proxy type to chek", None))
        self.checkBox.setText(QCoreApplication.translate("ProxyChecker", u"HTTP", None))
        self.checkBox_2.setText(QCoreApplication.translate("ProxyChecker", u"HTTPS", None))
        self.checkBox_3.setText(QCoreApplication.translate("ProxyChecker", u"SOCKS4", None))
        self.checkBox_4.setText(QCoreApplication.translate("ProxyChecker", u"SOCKS5", None))
        self.label_9.setText(QCoreApplication.translate("ProxyChecker", u"TimeOut (seconds)", None))
        self.lineEdit_7.setText(QCoreApplication.translate("ProxyChecker", u"2", None))
        self.label_11.setText(QCoreApplication.translate("ProxyChecker", u"Threads", None))
        self.lineEdit_8.setText(QCoreApplication.translate("ProxyChecker", u"20", None))
        self.label_10.setText(QCoreApplication.translate("ProxyChecker", u"Status: READY", None))
        self.pushButton_3.setText(QCoreApplication.translate("ProxyChecker", u"Start group check", None))
    # retranslateUi


class PR_CH(QtWidgets.QMainWindow, Ui_ProxyChecker):  # Собираем класс с нашими основными действиями
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Создание формы и Ui (наш дизайн)
        self.show()  # Показать наше окно
        # прописывем реакции на кнопки
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton_3.clicked.connect(self.main_part)

    def type_check(self):
        prxtype = []
        if self.checkBox.isChecked():
            prxtype.append("HTTP")
        if self.checkBox_2.isChecked():
            prxtype.append("HTTPS")
        if self.checkBox_3.isChecked():
            prxtype.append("SOCKS4")
        if self.checkBox_4.isChecked():
            prxtype.append("SOCKS5")
        return prxtype

    def browse(self):
        self.label_10.setText("Status: Ready")
        full_path, _ = QFileDialog.getOpenFileName(self, "Select proxy list", QDir.currentPath())
        self.lineEdit_6.setText(full_path)

    def preload(self):
        filename = self.lineEdit_6.text()
        bytes = min(32, os.path.getsize(filename))
        raw = open(filename, 'rb').read(bytes)
        if raw.startswith(codecs.BOM_UTF8):
            encoding = 'utf-8-sig'
        else:
            result = chardet.detect(raw)
            encoding = result['encoding']

        with open(self.lineEdit_6.text(), 'r', encoding=encoding) as f:
            nums = f.read().splitlines()

        nums = [i for i in nums if len(i) >= 8]
        #print(nums)
        self.label_10.setText("Status: Work")
        return nums

    def one_check(self, prxtchck, to_file):
        try:
            requests.get('https://www.google.com/', proxies=prxtchck, timeout=int(self.lineEdit_7.text()))
            print("Proxy " + str(prxtchck) + " OK")  # подтверждаем что прокси работает
            output = open("output_multi.txt", 'a')
            print(str(to_file), file=output)
            output.close()
        except Exception as e:  # в случае ошибки
            #print(e)
            print("Proxy " + str(prxtchck) + " not OK")  # подтверждаем что проски не работает
            pass

    def main_part(self):
        start_time = datetime.now()
        try:
            lister = self.preload()
            ptl = self.type_check()
            for z in range(len(lister)):
                    for y in range(len(ptl)):
                        proxies1 = {
                            'https': ptl[y] + '://' + lister[z]  # собираем прокси
                        }
                        if threading.activeCount() == int(self.lineEdit_8.text()):
                            while True:
                                logging.info("sleeping")
                                print(threading.activeCount())
                                time.sleep(2)
                                if threading.activeCount() == 1:
                                    for x in range(len(thread_list)):
                                        thread_list[x].join()
                                        to_loger = ("Joined", thread_list[x])
                                        logging.info(to_loger)
                                    thread_list.clear()
                                    break

                        thread_list.append("thread" + str(z) + str(y))
                        thread_list[-1] = Thread(target=self.one_check, args=(proxies1, lister[z]))
                        thread_list[-1].start()
                        print(thread_list)

            webbrowser.open("output_multi.txt")
            self.label_10.setText("Status: Done")
        except Exception:
            self.label_10.setText("Status: Error")
        if z + 1 == len(lister):
            while True:
                if threading.activeCount() == 1:
                    output = open("output_multi.txt", 'a')
                    print(datetime.now() - start_time, file=output)
                    output.close()
                    break
                else:
                    time.sleep(1)

    def check(self):  # функция ввода данных для парсера
        PROXY = self.lineEdit_2.text() + ":" + self.lineEdit_3.text()
        try:
            req = self.lineEdit_5.text()
            if len(req) > 0:  # проверяем есть ли у прокси проверка имени\пароля
                proxies = {
                    'https': self.lineEdit.text() + '://' + self.lineEdit_5.text() + ":" + self.lineEdit_4.text() + "@" + str(
                        PROXY)  # собираем прокси
                }
            else:  # если прокси без имени\пароля
                proxies = {
                    'https': self.lineEdit.text() + '://' + str(PROXY)  # собираем прокси
                }
            s = requests.Session()  # создаем сесиию
            s.proxies = proxies  # привязываем собранный прокси
            r = s.get('https://www.google.com/', timeout=5)  # пытаемся получить доступ к адресу через собранный прокси
            self.label_6.setText("      Proxy " + str(PROXY) + " OK")
            self.label_6.setStyleSheet("background-color: lightgreen")
        except Exception as e:  # в случае ошибки
            self.label_6.setText("    Proxy " + str(PROXY) + " not OK")
            self.label_6.setStyleSheet("background-color: red")
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    prch_gui = PR_CH()  # Сoздание инстанса класса, который мы создадим далее
    sys.exit(app.exec_())  # Запуск

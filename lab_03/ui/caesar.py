# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txt_plaintext = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_plaintext.setGeometry(QtCore.QRect(80, 40, 261, 51))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_key = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_key.setGeometry(QtCore.QRect(80, 100, 261, 31))
        self.txt_key.setObjectName("txt_key")
        self.txt_ciphertext = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_ciphertext.setGeometry(QtCore.QRect(80, 150, 261, 61))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.btn_encrypt = QtWidgets.QPushButton(Dialog)
        self.btn_encrypt.setGeometry(QtCore.QRect(80, 230, 121, 41))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(Dialog)
        self.btn_decrypt.setGeometry(QtCore.QRect(220, 230, 121, 41))
        self.btn_decrypt.setObjectName("btn_decrypt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "caesar"))
        self.label_2.setText(_translate("Dialog", "Plain text:"))
        self.label_3.setText(_translate("Dialog", "Key:"))
        self.label_4.setText(_translate("Dialog", "Cipher text:"))
        self.btn_encrypt.setText(_translate("Dialog", "Encrypt"))
        self.btn_decrypt.setText(_translate("Dialog", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

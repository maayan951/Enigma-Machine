
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from enigma_machine import *
from CONSTANT import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 560))
        MainWindow.setMaximumSize(QtCore.QSize(600, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setEnabled(True)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 110, 181, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.Layout_wiringSetting = QtWidgets.QHBoxLayout(self.formLayoutWidget)
        self.Layout_wiringSetting.setContentsMargins(0, 0, 0, 0)
        self.Layout_wiringSetting.setObjectName("Layout_wiringSetting")
        self.comboBox_wiringSetting1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_wiringSetting1.setEnabled(True)
        
        # region QtWidgets
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_wiringSetting1.setFont(font)
        self.comboBox_wiringSetting1.setObjectName("comboBox_wiringSetting1")
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting1.addItem("")
        
        self.Layout_wiringSetting.addWidget(self.comboBox_wiringSetting1)
        self.comboBox_wiringSetting2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_wiringSetting2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_wiringSetting2.setFont(font)
        self.comboBox_wiringSetting2.setObjectName("comboBox_wiringSetting2")
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting2.addItem("")
        
        self.Layout_wiringSetting.addWidget(self.comboBox_wiringSetting2)
        self.comboBox_wiringSetting3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_wiringSetting3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_wiringSetting3.setFont(font)
        self.comboBox_wiringSetting3.setObjectName("comboBox_wiringSetting3")
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting3.addItem("")
        
        self.Layout_wiringSetting.addWidget(self.comboBox_wiringSetting3)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setEnabled(True)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(290, 60, 181, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.Layout_rotors = QtWidgets.QHBoxLayout(self.formLayoutWidget_2)
        self.Layout_rotors.setContentsMargins(0, 0, 0, 0)
        self.Layout_rotors.setObjectName("Layout_rotors")
        self.comboBox_rotor1 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_rotor1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_rotor1.setFont(font)
        self.comboBox_rotor1.setObjectName("comboBox_rotor1")
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor1.addItem("")
        
        self.Layout_rotors.addWidget(self.comboBox_rotor1)
        self.comboBox_rotor2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_rotor2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_rotor2.setFont(font)
        self.comboBox_rotor2.setObjectName("comboBox_rotor2")
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor2.addItem("")
        
        self.Layout_rotors.addWidget(self.comboBox_rotor2)
        self.comboBox_rotor3 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_rotor3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_rotor3.setFont(font)
        self.comboBox_rotor3.setObjectName("comboBox_rotor3")
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor3.addItem("")
        
        self.Layout_rotors.addWidget(self.comboBox_rotor3)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setEnabled(True)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(290, 160, 181, 31))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.Layout_rotors_2 = QtWidgets.QHBoxLayout(self.formLayoutWidget_3)
        self.Layout_rotors_2.setContentsMargins(0, 0, 0, 0)
        self.Layout_rotors_2.setObjectName("Layout_rotors_2")
        self.comboBox_reflector = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox_reflector.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_reflector.setFont(font)
        self.comboBox_reflector.setObjectName("comboBox_reflector")
        
        for i in range(len(REFLECTOR_WIRINGS)):
            self.comboBox_reflector.addItem("")
        
        self.Layout_rotors_2.addWidget(self.comboBox_reflector)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 270, 271, 191))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 270, 271, 191))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.label_rotors = QtWidgets.QLabel(self.centralwidget)
        self.label_rotors.setGeometry(QtCore.QRect(120, 60, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_rotors.setFont(font)
        self.label_rotors.setObjectName("label_rotors")
        self.label_rotorsPositions = QtWidgets.QLabel(self.centralwidget)
        self.label_rotorsPositions.setGeometry(QtCore.QRect(120, 110, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_rotorsPositions.setFont(font)
        self.label_rotorsPositions.setObjectName("label_rotorsPositions")
        self.label_reflector = QtWidgets.QLabel(self.centralwidget)
        self.label_reflector.setGeometry(QtCore.QRect(120, 160, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_reflector.setFont(font)
        self.label_reflector.setObjectName("label_reflector")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(190, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_plugboard = QtWidgets.QLabel(self.centralwidget)
        self.label_plugboard.setGeometry(QtCore.QRect(120, 210, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_plugboard.setFont(font)
        self.label_plugboard.setObjectName("label_plugboard")
        self.lineEdit_plugboard = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_plugboard.setGeometry(QtCore.QRect(290, 210, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_plugboard.setFont(font)
        self.lineEdit_plugboard.setInputMask("")
        self.lineEdit_plugboard.setText("")
        self.lineEdit_plugboard.setObjectName("lineEdit_plugboard")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # endregion QtWidgets
        
        
        # region event handlers
        self.textEdit.textChanged.connect(self.eventHandler)                        # event handler for text change in textEdit
        self.comboBox_reflector.currentIndexChanged.connect(self.eventHandler)      # event handler for comboBox change in reflector
        self.comboBox_rotor1.currentIndexChanged.connect(self.eventHandler)         # event handler for comboBox change in rotor1
        self.comboBox_rotor2.currentIndexChanged.connect(self.eventHandler)         # event handler for comboBox change in rotor1
        self.comboBox_rotor3.currentIndexChanged.connect(self.eventHandler)         # event handler for comboBox change in rotor1
        self.comboBox_wiringSetting1.currentIndexChanged.connect(self.eventHandler) # event handler for comboBox change in wiringSetting1
        self.comboBox_wiringSetting2.currentIndexChanged.connect(self.eventHandler) # event handler for comboBox change in wiringSetting1
        self.comboBox_wiringSetting3.currentIndexChanged.connect(self.eventHandler) # event handler for comboBox change in wiringSetting1
        self.lineEdit_plugboard.textChanged.connect(self.eventHandler)              # event handler for text change in plugboard
        # endregion event handlers
                
        self.retranslateUi(MainWindow)
        self.comboBox_rotor2.setCurrentIndex(1)
        self.comboBox_rotor3.setCurrentIndex(2)
        self.comboBox_reflector.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enigma Machine V.1(MBB)"))
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting1.setItemText(i,_translate("MainWindow", ALPHABET[i]))
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting2.setItemText(i,_translate("MainWindow", ALPHABET[i]))
        
        for i in range(len(ALPHABET)):
            self.comboBox_wiringSetting3.setItemText(i,_translate("MainWindow", ALPHABET[i]))
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor1.setItemText(i,_translate("MainWindow", list(ROTOR_WIRINGS.keys())[i]))
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor2.setItemText(i,_translate("MainWindow", list(ROTOR_WIRINGS.keys())[i]))
        
        for i in range(len(ROTOR_WIRINGS)):
            self.comboBox_rotor3.setItemText(i,_translate("MainWindow", list(ROTOR_WIRINGS.keys())[i]))
        
        for i in range(len(REFLECTOR_WIRINGS)):
            self.comboBox_reflector.setItemText(i,_translate("MainWindow", list(REFLECTOR_WIRINGS.keys())[i]))
        
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Input"))        
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Output"))
        self.label_rotors.setText(_translate("MainWindow", "Rotors:"))
        self.label_rotorsPositions.setText(_translate("MainWindow", "Rotors Positions:"))
        self.label_reflector.setText(_translate("MainWindow", "Reflector:"))
        self.label_title.setText(_translate("MainWindow", "Enimga Machine"))
        self.label_plugboard.setText(_translate("MainWindow", "Plugboard:"))
        self.lineEdit_plugboard.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_plugboard.setPlaceholderText(_translate("MainWindow", "BQ CR DI EJ KW"))


    def eventHandler(self):
        inputMessage = self.textEdit.toPlainText()
        if inputMessage == "":
            self.textEdit_2.setText("")
            return
        
        rotor1 = self.comboBox_rotor1.currentText()
        rotor2 = self.comboBox_rotor2.currentText()
        rotor3 = self.comboBox_rotor3.currentText()
        rotors = f"{rotor1} {rotor2} {rotor3}"
        
        wiringSetting1 = self.comboBox_wiringSetting1.currentText()
        wiringSetting2 = self.comboBox_wiringSetting2.currentText()
        wiringSetting3 = self.comboBox_wiringSetting3.currentText()
        rotorsSettings = f"{wiringSetting1} {wiringSetting2} {wiringSetting3}"
        
        reflector = self.comboBox_reflector.currentText()
        plugboard = self.lineEdit_plugboard.text().upper()
        
        try:
            EM = EnigmaMachine(rotors, rotorsSettings, reflector, plugboard, inputMessage)

            self.textEdit_2.setStyleSheet("")
            self.textEdit_2.setPlainText(EM.encryptDecryptMessage())
        except Exception as e:
            self.textEdit_2.setPlainText("Error!\n" + e.args[0])
            self.textEdit_2.setStyleSheet("color: red")
                            
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

## check how to auto-adjust the size of the window

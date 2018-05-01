# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import massMailerwithBCC as mail
from PyQt4 import QtTest

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_9.setMargin(5)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.HTML_Label = QtGui.QLabel(self.centralwidget)
        self.HTML_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HTML_Label.setFrameShadow(QtGui.QFrame.Raised)
        self.HTML_Label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.HTML_Label.setWordWrap(False)
        self.HTML_Label.setObjectName(_fromUtf8("HTML_Label"))
        self.verticalLayout_3.addWidget(self.HTML_Label)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.HTML_Button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HTML_Button.sizePolicy().hasHeightForWidth())
        self.HTML_Button.setSizePolicy(sizePolicy)
        self.HTML_Button.setObjectName(_fromUtf8("HTML_Button"))
        self.horizontalLayout_8.addWidget(self.HTML_Button)
        self.HTML_Edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HTML_Edit.sizePolicy().hasHeightForWidth())
        self.HTML_Edit.setSizePolicy(sizePolicy)
        self.HTML_Edit.setObjectName(_fromUtf8("HTML_Edit"))
        self.horizontalLayout_8.addWidget(self.HTML_Edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.CSV_Label = QtGui.QLabel(self.centralwidget)
        self.CSV_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CSV_Label.setFrameShadow(QtGui.QFrame.Raised)
        self.CSV_Label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.CSV_Label.setWordWrap(False)
        self.CSV_Label.setObjectName(_fromUtf8("CSV_Label"))
        self.verticalLayout_2.addWidget(self.CSV_Label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.CSV_Button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CSV_Button.sizePolicy().hasHeightForWidth())
        self.CSV_Button.setSizePolicy(sizePolicy)
        self.CSV_Button.setObjectName(_fromUtf8("CSV_Button"))
        self.horizontalLayout_4.addWidget(self.CSV_Button)
        self.CSV_Edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CSV_Edit.sizePolicy().hasHeightForWidth())
        self.CSV_Edit.setSizePolicy(sizePolicy)
        self.CSV_Edit.setObjectName(_fromUtf8("CSV_Edit"))
        self.horizontalLayout_4.addWidget(self.CSV_Edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.Info_Label = QtGui.QLabel(self.centralwidget)
        self.Info_Label.setText(_fromUtf8(""))
        self.Info_Label.setObjectName(_fromUtf8("Info_Label"))
        self.verticalLayout_6.addWidget(self.Info_Label)
        self.Mail_Label = QtGui.QListView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mail_Label.sizePolicy().hasHeightForWidth())
        self.Mail_Label.setSizePolicy(sizePolicy)
        self.Mail_Label.setObjectName(_fromUtf8("Mail_Label"))
        self.verticalLayout_6.addWidget(self.Mail_Label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.lcdMail = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMail.setObjectName(_fromUtf8("lcdMail"))
        self.horizontalLayout_2.addWidget(self.lcdMail)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_8.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('plastique'))

        self.model = QtGui.QStandardItemModel(self.Mail_Label)
        self.Mail_Label.setModel(self.model)
        self.Mail_Label.setAutoScroll(True)
        self.Mail_Label.setAlternatingRowColors(True)
        self.Mail_Label.setFont(QtGui.QFont('timesnewroman'))


        self.CSV_Button.clicked.connect(self.csv_clicked)
        self.HTML_Button.clicked.connect(self.html_clicked)
        self.runButton.clicked.connect(self.pushBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mass Mail Sender by Tayyip Gören", None))
        MainWindow.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.progressBar.setVisible(False)
        self.HTML_Label.setText(_translate("MainWindow", "Please select HTML file :", None))
        self.HTML_Button.setText(_translate("MainWindow", "Open HTML File", None))
        self.CSV_Label.setText(_translate("MainWindow", "Please select CSV file :", None))
        self.CSV_Button.setText(_translate("MainWindow", "Open CSV File", None))
        self.runButton.setText(_translate("MainWindow", "RUN", None))

    def csv_clicked(self):
        text = QtGui.QFileDialog.getOpenFileName(self.CSV_Button, 'Open CSV File')
        self.user = mail.readUserFile(text)
        self.CSV_Edit.setText(text)
        self.Info_Label.setText("ID : %s\nMail Subject : %s\nTime Interval : %s" % (self.user['username'], self.user['subject'], self.user['timeInterval']))

    def html_clicked(self):
        text = QtGui.QFileDialog.getOpenFileName(self.HTML_Button, 'Open HTML File')
        self.html = mail.readHTML(text)
        self.HTML_Edit.setText(text)


    def pushBtn(self):
        self.HTML_Button.setVisible(False)
        self.CSV_Button.setVisible(False)
        self.HTML_Edit.setDisabled(True)
        self.CSV_Edit.setDisabled(True)
        self.runButton.setDisabled(True)

        self.login = mail.login(self.user['username'],self.user['password'])
        if (self.login is not None):
            self.Info_Label.setText(self.Info_Label.text()+"\n\nLogin as [%s] is success." % self.user['username'])
        else:
            sys.exit(0)
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)

        if (mail.sendMailFromFile("mail.txt", self.user, self.login, self.html,self)):
            self.runButton.setText("Success")
            mail.logout(self.login)
        else:
            self.runButton.setText("ERROR")
            mail.logout(self.login)

    def mail_text(self,text):
        item = QtGui.QStandardItem(text)
        item.setIcon(QtGui.QIcon('mail.png'))
        item.isSelectable()
        item.setEditable(False)
        self.model.appendRow(item)

    def wait(self,msecs):
        QtTest.QTest.qWait(msecs*1000)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


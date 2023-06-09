
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import sys
import sqlite3


class Ui_MainWindow(object):
    adminusername = "savv"
    adminpassword = "savv8"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 595)
        MainWindow.setStyleSheet(
            "\n""background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidgetmain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetmain.setStyleSheet(
            "\n""background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabWidgetmain.setObjectName("tabWidgetmain")
        self.tabwelcome = QtWidgets.QWidget()
        self.tabwelcome.setObjectName("tabwelcome")
        self.labelimage = QtWidgets.QLabel(self.tabwelcome)
        self.labelimage.setGeometry(QtCore.QRect(310, 0, 721, 531))
        self.labelimage.setAutoFillBackground(False)
        self.labelimage.setText("")
        self.labelimage.setPixmap(QtGui.QPixmap(
            "ICC-Cricket-World-Cup-CS-_8.jpg"))
        self.labelimage.setScaledContents(True)
        self.labelimage.setObjectName("labelimage")
        self.label_15 = QtWidgets.QLabel(self.tabwelcome)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 291, 211))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(25)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tabwelcome)
        self.label_16.setGeometry(QtCore.QRect(30, 240, 251, 271))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("2019worldcup.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.tabWidgetmain.addTab(self.tabwelcome, "")
        self.tabuser = QtWidgets.QWidget()
        self.tabuser.setObjectName("tabuser")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabuser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidgetuser = QtWidgets.QTabWidget(self.tabuser)
        self.tabWidgetuser.setStyleSheet(
            "\n""background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabWidgetuser.setObjectName("tabWidgetuser")
        self.tabteams = QtWidgets.QWidget()
        self.tabteams.setObjectName("tabteams")
        self.pushButtonallteams = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonallteams.setGeometry(QtCore.QRect(380, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonallteams.setFont(font)
        self.pushButtonallteams.setObjectName("pushButtonallteams")
        self.tableWidgetteams = QtWidgets.QTableWidget(self.tabteams)
        self.tableWidgetteams.setGeometry(QtCore.QRect(370, 60, 621, 411))
        self.tableWidgetteams.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidgetteams.setObjectName("tableWidgetteams")
        self.tableWidgetteams.setColumnCount(11)
        self.tableWidgetteams.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetteams.setHorizontalHeaderItem(10, item)
        self.pushButtonindia = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonindia.setGeometry(QtCore.QRect(120, 10, 121, 91))
        self.pushButtonindia.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ind.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonindia.setIcon(icon)
        self.pushButtonindia.setIconSize(QtCore.QSize(110, 100))
        self.pushButtonindia.setObjectName("pushButtonindia")
        self.label_2 = QtWidgets.QLabel(self.tabteams)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 121, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tabteams)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButtonafg = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonafg.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.pushButtonafg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("afg.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonafg.setIcon(icon1)
        self.pushButtonafg.setIconSize(QtCore.QSize(90, 85))
        self.pushButtonafg.setObjectName("pushButtonafg")
        self.label_7 = QtWidgets.QLabel(self.tabteams)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 101, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButtonaus = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonaus.setGeometry(QtCore.QRect(10, 260, 101, 131))
        self.pushButtonaus.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("aus.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonaus.setIcon(icon2)
        self.pushButtonaus.setIconSize(QtCore.QSize(130, 120))
        self.pushButtonaus.setObjectName("pushButtonaus")
        self.label_8 = QtWidgets.QLabel(self.tabteams)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 101, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButtonnz = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonnz.setGeometry(QtCore.QRect(10, 130, 101, 101))
        self.pushButtonnz.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("NZ.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonnz.setIcon(icon3)
        self.pushButtonnz.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonnz.setObjectName("pushButtonnz")
        self.label_9 = QtWidgets.QLabel(self.tabteams)
        self.label_9.setGeometry(QtCore.QRect(250, 390, 91, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButtonengland = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonengland.setGeometry(QtCore.QRect(250, 260, 91, 131))
        self.pushButtonengland.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("eng.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonengland.setIcon(icon4)
        self.pushButtonengland.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonengland.setObjectName("pushButtonengland")
        self.pushButtonpak = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonpak.setGeometry(QtCore.QRect(130, 390, 101, 71))
        self.pushButtonpak.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pak.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonpak.setIcon(icon5)
        self.pushButtonpak.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonpak.setObjectName("pushButtonpak")
        self.label_10 = QtWidgets.QLabel(self.tabteams)
        self.label_10.setGeometry(QtCore.QRect(130, 460, 101, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButtonban = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonban.setGeometry(QtCore.QRect(250, 10, 91, 91))
        self.pushButtonban.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ban.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonban.setIcon(icon6)
        self.pushButtonban.setIconSize(QtCore.QSize(80, 80))
        self.pushButtonban.setObjectName("pushButtonban")
        self.label_11 = QtWidgets.QLabel(self.tabteams)
        self.label_11.setGeometry(QtCore.QRect(250, 100, 91, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tabteams)
        self.label_12.setGeometry(QtCore.QRect(130, 230, 101, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButtonsl = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonsl.setGeometry(QtCore.QRect(130, 260, 101, 101))
        self.pushButtonsl.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("sl.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonsl.setIcon(icon7)
        self.pushButtonsl.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonsl.setObjectName("pushButtonsl")
        self.label_13 = QtWidgets.QLabel(self.tabteams)
        self.label_13.setGeometry(QtCore.QRect(130, 360, 101, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButtonwi = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonwi.setGeometry(QtCore.QRect(250, 130, 91, 101))
        self.pushButtonwi.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("wi.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonwi.setIcon(icon8)
        self.pushButtonwi.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonwi.setObjectName("pushButtonwi")
        self.label_14 = QtWidgets.QLabel(self.tabteams)
        self.label_14.setGeometry(QtCore.QRect(250, 230, 91, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pushButtonsa = QtWidgets.QPushButton(self.tabteams)
        self.pushButtonsa.setGeometry(QtCore.QRect(130, 130, 101, 101))
        self.pushButtonsa.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("sa.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonsa.setIcon(icon9)
        self.pushButtonsa.setIconSize(QtCore.QSize(90, 90))
        self.pushButtonsa.setObjectName("pushButtonsa")
        self.tabWidgetuser.addTab(self.tabteams, "")
        self.tabplayers = QtWidgets.QWidget()
        self.tabplayers.setObjectName("tabplayers")
        self.linesearchplayersbyteamid = QtWidgets.QLineEdit(self.tabplayers)
        self.linesearchplayersbyteamid.setGeometry(
            QtCore.QRect(210, 80, 133, 20))
        self.linesearchplayersbyteamid.setObjectName(
            "linesearchplayersbyteamid")
        self.label = QtWidgets.QLabel(self.tabplayers)
        self.label.setGeometry(QtCore.QRect(33, 80, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioallplayers = QtWidgets.QRadioButton(self.tabplayers)
        self.radioallplayers.setGeometry(QtCore.QRect(210, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioallplayers.setFont(font)
        self.radioallplayers.setObjectName("radioallplayers")
        self.radiobatsmen = QtWidgets.QRadioButton(self.tabplayers)
        self.radiobatsmen.setGeometry(QtCore.QRect(210, 160, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radiobatsmen.setFont(font)
        self.radiobatsmen.setObjectName("radiobatsmen")
        self.tableWidgetplayers = QtWidgets.QTableWidget(self.tabplayers)
        self.tableWidgetplayers.setGeometry(QtCore.QRect(400, 10, 591, 461))
        self.tableWidgetplayers.setObjectName("tableWidgetplayers")
        self.tableWidgetplayers.setColumnCount(15)
        self.tableWidgetplayers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers.setHorizontalHeaderItem(14, item)
        self.radiobowlers = QtWidgets.QRadioButton(self.tabplayers)
        self.radiobowlers.setGeometry(QtCore.QRect(210, 190, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radiobowlers.setFont(font)
        self.radiobowlers.setObjectName("radiobowlers")
        self.linesearchplayerbyid = QtWidgets.QLineEdit(self.tabplayers)
        self.linesearchplayerbyid.setGeometry(QtCore.QRect(90, 300, 141, 21))
        self.linesearchplayerbyid.setObjectName("linesearchplayerbyid")
        self.pushButtonsearchplayerbyid = QtWidgets.QPushButton(
            self.tabplayers)
        self.pushButtonsearchplayerbyid.setGeometry(
            QtCore.QRect(230, 300, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButtonsearchplayerbyid.setFont(font)
        self.pushButtonsearchplayerbyid.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtonsearchplayerbyid.setObjectName(
            "pushButtonsearchplayerbyid")
        self.label_5 = QtWidgets.QLabel(self.tabplayers)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButtontopbatsmen = QtWidgets.QPushButton(self.tabplayers)
        self.pushButtontopbatsmen.setGeometry(QtCore.QRect(90, 360, 211, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtontopbatsmen.setFont(font)
        self.pushButtontopbatsmen.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtontopbatsmen.setObjectName("pushButtontopbatsmen")
        self.pushButtontopbowlers = QtWidgets.QPushButton(self.tabplayers)
        self.pushButtontopbowlers.setGeometry(QtCore.QRect(90, 400, 211, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtontopbowlers.setFont(font)
        self.pushButtontopbowlers.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtontopbowlers.setObjectName("pushButtontopbowlers")
        self.tabWidgetuser.addTab(self.tabplayers, "")
        self.tabmatches = QtWidgets.QWidget()
        self.tabmatches.setObjectName("tabmatches")
        self.radioallmatches = QtWidgets.QRadioButton(self.tabmatches)
        self.radioallmatches.setGeometry(QtCore.QRect(210, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioallmatches.setFont(font)
        self.radioallmatches.setObjectName("radioallmatches")
        self.linesearchmatchbyteamid = QtWidgets.QLineEdit(self.tabmatches)
        self.linesearchmatchbyteamid.setGeometry(
            QtCore.QRect(450, 40, 133, 20))
        self.linesearchmatchbyteamid.setObjectName("linesearchmatchbyteamid")
        self.pushButtonsearchmatchbyteamid = QtWidgets.QPushButton(
            self.tabmatches)
        self.pushButtonsearchmatchbyteamid.setGeometry(
            QtCore.QRect(630, 40, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonsearchmatchbyteamid.setFont(font)
        self.pushButtonsearchmatchbyteamid.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtonsearchmatchbyteamid.setObjectName(
            "pushButtonsearchmatchbyteamid")
        self.tableWidgetplayers_3 = QtWidgets.QTableWidget(self.tabmatches)
        self.tableWidgetplayers_3.setGeometry(QtCore.QRect(10, 110, 981, 371))
        self.tableWidgetplayers_3.setObjectName("tableWidgetplayers_3")
        self.tableWidgetplayers_3.setColumnCount(13)
        self.tableWidgetplayers_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetplayers_3.setHorizontalHeaderItem(12, item)
        self.radioButtonsearchmatchbyteamid = QtWidgets.QRadioButton(
            self.tabmatches)
        self.radioButtonsearchmatchbyteamid.setGeometry(
            QtCore.QRect(210, 40, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonsearchmatchbyteamid.setFont(font)
        self.radioButtonsearchmatchbyteamid.setObjectName(
            "radioButtonsearchmatchbyteamid")
        self.radioButtonsearchmatchbydate = QtWidgets.QRadioButton(
            self.tabmatches)
        self.radioButtonsearchmatchbydate.setGeometry(
            QtCore.QRect(210, 70, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonsearchmatchbydate.setFont(font)
        self.radioButtonsearchmatchbydate.setObjectName(
            "radioButtonsearchmatchbydate")
        self.pushButtonsearchmatchbydate = QtWidgets.QPushButton(
            self.tabmatches)
        self.pushButtonsearchmatchbydate.setGeometry(
            QtCore.QRect(630, 70, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonsearchmatchbydate.setFont(font)
        self.pushButtonsearchmatchbydate.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtonsearchmatchbydate.setObjectName(
            "pushButtonsearchmatchbydate")
        self.linesearchmatchbydate = QtWidgets.QLineEdit(self.tabmatches)
        self.linesearchmatchbydate.setGeometry(QtCore.QRect(450, 70, 133, 20))
        self.linesearchmatchbydate.setObjectName("linesearchmatchbydate")
        self.tabWidgetuser.addTab(self.tabmatches, "")
        self.tabotherinfo = QtWidgets.QWidget()
        self.tabotherinfo.setObjectName("tabotherinfo")
        self.radiocaptains = QtWidgets.QRadioButton(self.tabotherinfo)
        self.radiocaptains.setGeometry(QtCore.QRect(220, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radiocaptains.setFont(font)
        self.radiocaptains.setObjectName("radiocaptains")
        self.radiocoaches = QtWidgets.QRadioButton(self.tabotherinfo)
        self.radiocoaches.setGeometry(QtCore.QRect(220, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radiocoaches.setFont(font)
        self.radiocoaches.setObjectName("radiocoaches")
        self.radioumpires = QtWidgets.QRadioButton(self.tabotherinfo)
        self.radioumpires.setGeometry(QtCore.QRect(560, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioumpires.setFont(font)
        self.radioumpires.setObjectName("radioumpires")
        self.radioallstadiums = QtWidgets.QRadioButton(self.tabotherinfo)
        self.radioallstadiums.setGeometry(QtCore.QRect(560, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioallstadiums.setFont(font)
        self.radioallstadiums.setObjectName("radioallstadiums")
        self.tableWidgetotherinfo = QtWidgets.QTableWidget(self.tabotherinfo)
        self.tableWidgetotherinfo.setGeometry(QtCore.QRect(150, 120, 741, 341))
        self.tableWidgetotherinfo.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidgetotherinfo.setObjectName("tableWidgetotherinfo")
        self.tableWidgetotherinfo.setColumnCount(7)
        self.tableWidgetotherinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetotherinfo.setHorizontalHeaderItem(6, item)
        self.radiocaptains_2 = QtWidgets.QRadioButton(self.tabotherinfo)
        self.radiocaptains_2.setGeometry(QtCore.QRect(220, 80, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radiocaptains_2.setFont(font)
        self.radiocaptains_2.setObjectName("radiocaptains_2")
        self.tabWidgetuser.addTab(self.tabotherinfo, "")
        self.gridLayout_2.addWidget(self.tabWidgetuser, 0, 0, 1, 1)
        self.tabWidgetmain.addTab(self.tabuser, "")
        self.tabadmin = QtWidgets.QWidget()
        self.tabadmin.setObjectName("tabadmin")
        self.pushButtonlogin = QtWidgets.QPushButton(self.tabadmin)
        self.pushButtonlogin.setGeometry(QtCore.QRect(590, 310, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonlogin.setFont(font)
        self.pushButtonlogin.setStyleSheet(
            "\n""background-color: rgb(75, 153, 255);\n""background-color: rgb(139, 224, 255);\n""")
        self.pushButtonlogin.setObjectName("pushButtonlogin")
        self.lineusername = QtWidgets.QLineEdit(self.tabadmin)
        self.lineusername.setGeometry(QtCore.QRect(490, 180, 181, 31))
        self.lineusername.setObjectName("lineusername")
        self.linepassword = QtWidgets.QLineEdit(self.tabadmin)
        self.linepassword.setGeometry(QtCore.QRect(490, 240, 181, 31))
        self.linepassword.setObjectName("linepassword")
        self.label_3 = QtWidgets.QLabel(self.tabadmin)
        self.label_3.setGeometry(QtCore.QRect(350, 180, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabadmin)
        self.label_4.setGeometry(QtCore.QRect(350, 240, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidgetmain.addTab(self.tabadmin, "")
        self.gridLayout.addWidget(self.tabWidgetmain, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidgetmain.setCurrentIndex(0)
        self.tabWidgetuser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonlogin.clicked.connect(self.adminlogin)
        self.pushButtonallteams.clicked.connect(self.allteams)
        self.pushButtonindia.clicked.connect(self.teamind)
        self.pushButtonafg.clicked.connect(self.teamafg)
        self.pushButtonnz.clicked.connect(self.teamnz)
        self.pushButtonengland.clicked.connect(self.teameng)
        self.pushButtonpak.clicked.connect(self.teampak)
        self.pushButtonban.clicked.connect(self.teamban)
        self.pushButtonsl.clicked.connect(self.teamsl)
        self.pushButtonwi.clicked.connect(self.teamafg)
        self.pushButtonsa.clicked.connect(self.teamsa)
        self.radioallplayers.clicked.connect(self.allplayer)
        self.radiobatsmen.clicked.connect(self.batsmen)
        self.radiobowlers.clicked.connect(self.bowler)
        self.pushButtonsearchplayerbyid.clicked.connect(self.playerBYname)
        self.pushButtontopbatsmen.clicked.connect(self.topbatsmen)
        self.pushButtontopbowlers.clicked.connect(self.tobowlers)
        self.radioallmatches.clicked.connect(self.allmatchs)
        self.radioButtonsearchmatchbyteamid.clicked.connect(
            self.searchmatchbyteamid)
        self.radioButtonsearchmatchbydate.clicked.connect(
            self.searchmatchbydate)
        self.radiocaptains.clicked.connect(self.captain)
        self.radiocoaches.clicked.connect(self.coach)
        self.radioumpires.clicked.connect(self.umpire)
        self.radioallstadiums.clicked.connect(self.stadiums)
        self.radiocaptains_2.clicked.connect(self.umpired_by)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate(
            "MainWindow", "WELCOME,\n"" GET  DATA \n""RELATED TO \n"" WORLDCUP...! "))
        self.tabWidgetmain.setTabText(self.tabWidgetmain.indexOf(
            self.tabwelcome), _translate("MainWindow", "WELCOME"))
        self.pushButtonallteams.setText(_translate("MainWindow", "ALL TEAMS"))
        item = self.tableWidgetteams.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team_id"))
        item = self.tableWidgetteams.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Country_name"))
        item = self.tableWidgetteams.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "No. of Bowlers"))
        item = self.tableWidgetteams.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "No. of Batsmen"))
        item = self.tableWidgetteams.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "No. of Wins"))
        item = self.tableWidgetteams.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "No. of Loss"))
        item = self.tableWidgetteams.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "No. of Draws"))
        item = self.tableWidgetteams.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Points"))
        item = self.tableWidgetteams.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Run Rate"))
        item = self.tableWidgetteams.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Team Rank"))
        self.label_2.setText(_translate("MainWindow", " INDIA"))
        self.label_6.setText(_translate("MainWindow", "AFGHANISTAN"))
        self.label_7.setText(_translate("MainWindow", "AUSTRALIA"))
        self.label_8.setText(_translate("MainWindow", "NEW ZEALAND"))
        self.label_9.setText(_translate("MainWindow", " ENGLAND"))
        self.label_10.setText(_translate("MainWindow", " PAKISTAN"))
        self.label_11.setText(_translate("MainWindow", "BANGLADESH"))
        self.label_12.setText(_translate("MainWindow", "SOUTH AFRICA"))
        self.label_13.setText(_translate("MainWindow", "SRI LANKA"))
        self.label_14.setText(_translate("MainWindow", "WEST INDIES"))
        self.tabWidgetuser.setTabText(self.tabWidgetuser.indexOf(
            self.tabteams), _translate("MainWindow", "TEAMS"))
        self.linesearchplayersbyteamid.setPlaceholderText(
            _translate("MainWindow", "TEAM ID (ex:IND)"))
        self.label.setText(_translate("MainWindow", "  SEARCH BY TEAMID :"))
        self.radioallplayers.setText(_translate("MainWindow", "ALL PLAYERS"))
        self.radiobatsmen.setText(_translate("MainWindow", "BATSMEN"))
        self.radiobowlers.setText(_translate("MainWindow", "BOWLERS"))
        self.linesearchplayerbyid.setPlaceholderText(
            _translate("MainWindow", "PLAYER NAME IN CAPS"))
        self.pushButtonsearchplayerbyid.setText(
            _translate("MainWindow", "SEARCH"))
        self.label_5.setText(_translate(
            "MainWindow", "  SEARCH BY PLAYER NAME :"))
        self.pushButtontopbatsmen.setText(
            _translate("MainWindow", "TOP 10 BATSMEN"))
        self.pushButtontopbowlers.setText(
            _translate("MainWindow", "TOP 10 BOWLERS"))
        self.tabWidgetuser.setTabText(self.tabWidgetuser.indexOf(
            self.tabplayers), _translate("MainWindow", "PLAYERS"))
        self.radioallmatches.setText(_translate(
            "MainWindow", "DISPLAY ALL MATCHES"))
        self.linesearchmatchbyteamid.setPlaceholderText(
            _translate("MainWindow", " TEAM ID (ex:IND)"))
        self.pushButtonsearchmatchbyteamid.setText(
            _translate("MainWindow", "SEARCH"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Match_id"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team1"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Team2"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stadium_id"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "match date time"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Result_id"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "winner_team"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Won by"))
        item = self.tableWidgetplayers_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Man of the match"))
        self.radioButtonsearchmatchbyteamid.setText(
            _translate("MainWindow", "SEARCH BY TEAMID "))
        self.radioButtonsearchmatchbydate.setText(
            _translate("MainWindow", "SEARCH BY DATE  "))
        self.pushButtonsearchmatchbydate.setText(
            _translate("MainWindow", "SEARCH"))
        self.linesearchmatchbydate.setPlaceholderText(
            _translate("MainWindow", "DATE Ex:dd-mm-yyyy"))
        self.tabWidgetuser.setTabText(self.tabWidgetuser.indexOf(
            self.tabmatches), _translate("MainWindow", "MATCHES"))
        self.radiocaptains.setText(_translate(
            "MainWindow", "DISPLAY ALL CAPTAINS"))
        self.radiocoaches.setText(_translate(
            "MainWindow", "DISPLAY ALL COACHES"))
        self.radioumpires.setText(_translate(
            "MainWindow", "DISPLAY ALL UMPIRES"))
        self.radioallstadiums.setText(_translate(
            "MainWindow", "DISPLAY ALL STADIUMS"))
        self.radiocaptains_2.setText(_translate(
            "MainWindow", "DISPLAY UMPIRE MAPPING TO MATCHES"))
        self.tabWidgetuser.setTabText(self.tabWidgetuser.indexOf(
            self.tabotherinfo), _translate("MainWindow", "OTHER INFO"))
        self.tabWidgetmain.setTabText(self.tabWidgetmain.indexOf(
            self.tabuser), _translate("MainWindow", "USER"))
        self.pushButtonlogin.setText(_translate("MainWindow", "LOGIN"))
        self.lineusername.setPlaceholderText(
            _translate("MainWindow", "USERNAME"))
        self.linepassword.setPlaceholderText(
            _translate("MainWindow", "PASSWORD"))
        self.label_3.setText(_translate("MainWindow", "     USERNAME:"))
        self.label_4.setText(_translate("MainWindow", "    PASSWORD:"))
        self.tabWidgetmain.setTabText(self.tabWidgetmain.indexOf(
            self.tabadmin), _translate("MainWindow", "ADMIN"))

    def stadiums(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetotherinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stadium ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Stadium Name"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pitch Type"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Capacity"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Matches"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " "))
        self.connection = sqlite3.connect("worldcup.db")
        query = "select *from stadium"
        result = self.connection.execute(query)
        self.tableWidgetotherinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetotherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetotherinfo.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def umpire(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetotherinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Umpire ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO. of Matchs"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Experience"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " "))
        self.connection = sqlite3.connect("worldcup.db")
        query = "select *from umpire "
        result = self.connection.execute(query)
        self.tableWidgetotherinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetotherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetotherinfo.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def umpired_by(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetotherinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Umpire Name"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Match ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Umpire ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", " "))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " "))
        self.connection = sqlite3.connect("worldcup.db")
        query = "select u.u_name,ub.* from umpire u, umpired_by ub where u.u_id=ub.u_id"
        result = self.connection.execute(query)
        self.tableWidgetotherinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetotherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetotherinfo.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def coach(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetotherinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Coach ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Coach Name"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Coach Country"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Coach Type"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Coach Experience"))
        self.connection = sqlite3.connect("worldcup.db")
        query = "select * from coach"
        result = self.connection.execute(query)
        self.tableWidgetotherinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetotherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetotherinfo.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def searchmatchbyteamid(self):
        self.pushButtonsearchmatchbyteamid.clicked.connect(self.fun)

    def fun(self):
        teamid = ""
        teamid = self.linesearchmatchbyteamid.text()
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT m.*,r.result_id,r.winner_team,r.won_by_runs_or_wickets,r.man_of_the_match  from matches m,results r where m.match_id=r.match_id and (m.team1_id = '" + str(
            teamid)+"' or m.team2_id = '" + str(teamid)+"');"
        result = self.connection.execute(query)
        self.tableWidgetplayers_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers_3.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def captain(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetotherinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Years of Captaincy"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Number of Wins"))
        item = self.tableWidgetotherinfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Number of Trophies "))
        self.connection = sqlite3.connect("worldcup.db")
        query = "select * from captain"
        result = self.connection.execute(query)
        self.tableWidgetotherinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetotherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetotherinfo.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def searchmatchbydate(self):
        self.pushButtonsearchmatchbydate.clicked.connect(self.fun2)

    def fun2(self):
        teamid = ""
        teamid = self.linesearchmatchbydate.text()
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT m.*,r.result_id,r.winner_team,r.won_by_runs_or_wickets,r.man_of_the_match  from matches m,results r where m.match_id=r.match_id and m.match_date_time like '%" + \
            str(teamid)+"%';"
        result = self.connection.execute(query)
        self.tableWidgetplayers_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers_3.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def allmatchs(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT m.*,r.result_id,r.winner_team,r.won_by_runs_or_wickets,r.man_of_the_match  from matches m,results r where m.match_id=r.match_id;"
        result = self.connection.execute(query)
        self.tableWidgetplayers_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers_3.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def tobowlers(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player Name"))
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bowler Type"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO Of Wickets"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Highest Speed"))
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Economy"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", ""))
        item.setText(_translate("MainWindow", ""))
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT p.player_name,b.* FROM player p, bowler b where p_disqualified like 'NO' and p.player_id=b.player_id ORDER by b.number_of_wickets  desc LIMIT 10"

        result = self.connection.execute(query)
        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def topbatsmen(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player Name"))
        teamid = self.linesearchplayersbyteamid.text()
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Batsman Type"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO. Of Sixes"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Runs"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Highest Score"))
        item = self.tableWidgetplayers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Batting Avg"))
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT p.player_name,b.* FROM player p, batsman b where p_disqualified like 'NO' and p.player_id=b.player_id ORDER by b.total_runs desc LIMIT 10 "

        result = self.connection.execute(query)
        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def playerBYname(self):
        teamid = ""
        teamid = self.linesearchplayerbyid.text()
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player Name"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DOB"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type Of Player"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NO. Of Tests"))
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NO Of T20s"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "NO OF ODIs"))
        item = self.tableWidgetplayers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TEAM ID"))
        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT player_id,player_name ,dob,type_of_player ,no_of_tests ,no_of_t20s ,no_of_ODIs ,team_id  FROM player where p_disqualified like 'NO' and upper(player_name) like '%" + str(
            teamid) + "%'"

        result = self.connection.execute(query)
        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def batsmen(self):
        self.connection = sqlite3.connect("worldcup.db")
        teamid = ""
        teamid = self.linesearchplayersbyteamid.text()
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player Name"))
        teamid = self.linesearchplayersbyteamid.text()
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Batsman Type"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO. Of Sixes"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Runs"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Highest Score"))
        item = self.tableWidgetplayers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Batting Avg"))

        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT p.player_name,b.* FROM player p, batsman b where p_disqualified like 'NO' and  p.player_id=b.player_id and p.team_id like '" + \
            str(teamid) + "'"

        result = self.connection.execute(query)
        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def bowler(self):
        teamid = ""
        teamid = self.linesearchplayersbyteamid.text()
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player Name"))
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bowler Type"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO Of Wickets"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Highest Speed"))
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Economy"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", ""))
        item.setText(_translate("MainWindow", ""))

        self.connection = sqlite3.connect("worldcup.db")
        query = "SELECT p.player_name,b.* FROM player p, bowler b where  p_disqualified like 'NO' and  p.player_id=b.player_id and p.team_id like '" + \
            str(teamid) + "'"

        result = self.connection.execute(query)
        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def allplayer(self):
        self.connection = sqlite3.connect("worldcup.db")
        teamid = ""
        teamid = self.linesearchplayersbyteamid.text()
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetplayers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player ID"))
        item = self.tableWidgetplayers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player Name"))
        item = self.tableWidgetplayers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DOB"))
        item = self.tableWidgetplayers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type Of Player"))
        item = self.tableWidgetplayers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NO. Of Tests"))
        item = self.tableWidgetplayers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NO Of T20s"))
        item = self.tableWidgetplayers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "NO OF ODIs"))
        item = self.tableWidgetplayers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TEAM ID"))
        query = "SELECT player_id,player_name ,dob,type_of_player ,no_of_tests ,no_of_t20s ,no_of_ODIs ,team_id  FROM player where p_disqualified like 'NO' and team_id like'" + \
            str(teamid) + "'"
        result = self.connection.execute(query)

        self.tableWidgetplayers.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetplayers.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetplayers.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def allteams(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamafg(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'AFG' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamind(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'IND' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamban(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'BAN' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamnz(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'NZ' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamsa(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'SA' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamwi(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'WI' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamaus(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'AUS' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teamsl(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'SL' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teameng(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'ENG' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def teampak(self):
        self.connection = sqlite3.connect("worldcup.db")
        query = "select t.team_id,t.country_name,t.no_of_bowlers,t.no_of_batsmen,p.number_of_wins,p.number_of_loss ,p.number_of_draw ,p.points,p.run_rate ,p.team_rank  from team t,points_table p where t.team_id=p.team_id and t.team_id = 'PAK' and t.disqualified like 'NO';"
        result = self.connection.execute(query)
        self.tableWidgetteams.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetteams.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetteams.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def adminlogin(self):
        lusername = ""
        lpassword = ""

        lusername = self.lineusername.text()
        lpassword = self.linepassword.text()
        if (lusername == self.adminusername) and (self.adminpassword == lpassword):
            self.openAdmin()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("username password didn't match")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def openAdmin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.window)
        self.window.show()


class Ui_Admin(object):
    awonby = ""

    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(1057, 588)
        Admin.setStyleSheet(
            "background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayout = QtWidgets.QGridLayout(Admin)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidgetadmin = QtWidgets.QTabWidget(Admin)
        self.tabWidgetadmin.setStyleSheet(
            "background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabWidgetadmin.setObjectName("tabWidgetadmin")
        self.tabachedulematches = QtWidgets.QWidget()
        self.tabachedulematches.setObjectName("tabachedulematches")
        self.lineEditteam1 = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditteam1.setGeometry(QtCore.QRect(210, 90, 141, 20))
        self.lineEditteam1.setObjectName("lineEditteam1")
        self.lineEditteam2 = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditteam2.setGeometry(QtCore.QRect(210, 130, 141, 20))
        self.lineEditteam2.setObjectName("lineEditteam2")
        self.labelteam1id = QtWidgets.QLabel(self.tabachedulematches)
        self.labelteam1id.setGeometry(QtCore.QRect(60, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelteam1id.setFont(font)
        self.labelteam1id.setAlignment(QtCore.Qt.AlignCenter)
        self.labelteam1id.setObjectName("labelteam1id")
        self.labelteam2id = QtWidgets.QLabel(self.tabachedulematches)
        self.labelteam2id.setGeometry(QtCore.QRect(60, 130, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelteam2id.setFont(font)
        self.labelteam2id.setAlignment(QtCore.Qt.AlignCenter)
        self.labelteam2id.setObjectName("labelteam2id")
        self.labeldate = QtWidgets.QLabel(self.tabachedulematches)
        self.labeldate.setGeometry(QtCore.QRect(60, 170, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeldate.setFont(font)
        self.labeldate.setAlignment(QtCore.Qt.AlignCenter)
        self.labeldate.setObjectName("labeldate")
        self.labeltime = QtWidgets.QLabel(self.tabachedulematches)
        self.labeltime.setGeometry(QtCore.QRect(60, 210, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeltime.setFont(font)
        self.labeltime.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltime.setObjectName("labeltime")
        self.lineEditdate = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditdate.setGeometry(QtCore.QRect(210, 170, 141, 20))
        self.lineEditdate.setObjectName("lineEditdate")
        self.lineEdittime = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEdittime.setGeometry(QtCore.QRect(210, 210, 141, 20))
        self.lineEdittime.setObjectName("lineEdittime")
        self.pushButtonschedulematch = QtWidgets.QPushButton(
            self.tabachedulematches)
        self.pushButtonschedulematch.setGeometry(
            QtCore.QRect(270, 400, 75, 23))
        self.pushButtonschedulematch.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonschedulematch.setObjectName("pushButtonschedulematch")
        self.line = QtWidgets.QFrame(self.tabachedulematches)
        self.line.setGeometry(QtCore.QRect(430, 0, 20, 541))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelschedulematches = QtWidgets.QLabel(self.tabachedulematches)
        self.labelschedulematches.setGeometry(QtCore.QRect(60, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelschedulematches.setFont(font)
        self.labelschedulematches.setAlignment(QtCore.Qt.AlignCenter)
        self.labelschedulematches.setObjectName("labelschedulematches")
        self.labelupdateresult = QtWidgets.QLabel(self.tabachedulematches)
        self.labelupdateresult.setGeometry(QtCore.QRect(550, 50, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelupdateresult.setFont(font)
        self.labelupdateresult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelupdateresult.setObjectName("labelupdateresult")
        self.lineEditresultwinner = QtWidgets.QLineEdit(
            self.tabachedulematches)
        self.lineEditresultwinner.setGeometry(QtCore.QRect(800, 190, 161, 21))
        self.lineEditresultwinner.setObjectName("lineEditresultwinner")
        self.labelwinnerteam = QtWidgets.QLabel(self.tabachedulematches)
        self.labelwinnerteam.setGeometry(QtCore.QRect(550, 190, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelwinnerteam.setFont(font)
        self.labelwinnerteam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelwinnerteam.setObjectName("labelwinnerteam")
        self.labelmatchid = QtWidgets.QLabel(self.tabachedulematches)
        self.labelmatchid.setGeometry(QtCore.QRect(550, 140, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelmatchid.setFont(font)
        self.labelmatchid.setAlignment(QtCore.Qt.AlignCenter)
        self.labelmatchid.setObjectName("labelmatchid")
        self.lineEditresultmatchid = QtWidgets.QLineEdit(
            self.tabachedulematches)
        self.lineEditresultmatchid.setGeometry(QtCore.QRect(800, 140, 161, 21))
        self.lineEditresultmatchid.setObjectName("lineEditresultmatchid")
        self.labelmanofthematch = QtWidgets.QLabel(self.tabachedulematches)
        self.labelmanofthematch.setGeometry(QtCore.QRect(550, 240, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelmanofthematch.setFont(font)
        self.labelmanofthematch.setAlignment(QtCore.Qt.AlignCenter)
        self.labelmanofthematch.setObjectName("labelmanofthematch")
        self.lineEditresultmanofmatch = QtWidgets.QLineEdit(
            self.tabachedulematches)
        self.lineEditresultmanofmatch.setGeometry(
            QtCore.QRect(800, 240, 161, 21))
        self.lineEditresultmanofmatch.setObjectName("lineEditresultmanofmatch")
        self.labelwonby = QtWidgets.QLabel(self.tabachedulematches)
        self.labelwonby.setGeometry(QtCore.QRect(550, 350, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelwonby.setFont(font)
        self.labelwonby.setAlignment(QtCore.Qt.AlignCenter)
        self.labelwonby.setObjectName("labelwonby")
        self.lineEditresultrunsorwickets = QtWidgets.QLineEdit(
            self.tabachedulematches)
        self.lineEditresultrunsorwickets.setGeometry(
            QtCore.QRect(800, 350, 161, 21))
        self.lineEditresultrunsorwickets.setObjectName(
            "lineEditresultrunsorwickets")
        self.radioButtonwonbywickets = QtWidgets.QRadioButton(
            self.tabachedulematches)
        self.radioButtonwonbywickets.setGeometry(
            QtCore.QRect(800, 310, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonwonbywickets.setFont(font)
        self.radioButtonwonbywickets.setObjectName("radioButtonwonbywickets")
        self.radioButtonwonbyruns = QtWidgets.QRadioButton(
            self.tabachedulematches)
        self.radioButtonwonbyruns.setGeometry(QtCore.QRect(800, 280, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonwonbyruns.setFont(font)
        self.radioButtonwonbyruns.setObjectName("radioButtonwonbyruns")
        self.pushButtonupdateresult = QtWidgets.QPushButton(
            self.tabachedulematches)
        self.pushButtonupdateresult.setGeometry(QtCore.QRect(880, 410, 75, 23))
        self.pushButtonupdateresult.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdateresult.setObjectName("pushButtonupdateresult")
        self.labeltime_2 = QtWidgets.QLabel(self.tabachedulematches)
        self.labeltime_2.setGeometry(QtCore.QRect(60, 290, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeltime_2.setFont(font)
        self.labeltime_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltime_2.setObjectName("labeltime_2")
        self.lineEditumpire1 = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditumpire1.setGeometry(QtCore.QRect(210, 290, 141, 20))
        self.lineEditumpire1.setObjectName("lineEditumpire1")
        self.labeltime_3 = QtWidgets.QLabel(self.tabachedulematches)
        self.labeltime_3.setGeometry(QtCore.QRect(60, 330, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeltime_3.setFont(font)
        self.labeltime_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltime_3.setObjectName("labeltime_3")
        self.lineEditumpire2 = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditumpire2.setGeometry(QtCore.QRect(210, 330, 141, 20))
        self.lineEditumpire2.setText("")
        self.lineEditumpire2.setObjectName("lineEditumpire2")
        self.labeltime_4 = QtWidgets.QLabel(self.tabachedulematches)
        self.labeltime_4.setGeometry(QtCore.QRect(60, 370, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labeltime_4.setFont(font)
        self.labeltime_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltime_4.setObjectName("labeltime_4")
        self.lineEditumpire3 = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditumpire3.setGeometry(QtCore.QRect(210, 370, 141, 20))
        self.lineEditumpire3.setText("")
        self.lineEditumpire3.setObjectName("lineEditumpire3")
        self.pushButtonsupdatematch = QtWidgets.QPushButton(
            self.tabachedulematches)
        self.pushButtonsupdatematch.setGeometry(QtCore.QRect(270, 460, 75, 23))
        self.pushButtonsupdatematch.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonsupdatematch.setObjectName("pushButtonsupdatematch")
        self.labelteam1id_2 = QtWidgets.QLabel(self.tabachedulematches)
        self.labelteam1id_2.setGeometry(QtCore.QRect(60, 250, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelteam1id_2.setFont(font)
        self.labelteam1id_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelteam1id_2.setObjectName("labelteam1id_2")
        self.lineEditstadiumid = QtWidgets.QLineEdit(self.tabachedulematches)
        self.lineEditstadiumid.setGeometry(QtCore.QRect(210, 250, 141, 20))
        self.lineEditstadiumid.setObjectName("lineEditstadiumid")
        self.lineEditschedulematchid = QtWidgets.QLineEdit(
            self.tabachedulematches)
        self.lineEditschedulematchid.setGeometry(
            QtCore.QRect(210, 430, 141, 21))
        self.lineEditschedulematchid.setObjectName("lineEditschedulematchid")
        self.labelmatchid_2 = QtWidgets.QLabel(self.tabachedulematches)
        self.labelmatchid_2.setGeometry(QtCore.QRect(60, 430, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelmatchid_2.setFont(font)
        self.labelmatchid_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelmatchid_2.setObjectName("labelmatchid_2")
        self.pushButtondraw = QtWidgets.QPushButton(self.tabachedulematches)
        self.pushButtondraw.setGeometry(QtCore.QRect(840, 160, 121, 23))
        self.pushButtondraw.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondraw.setObjectName("pushButtondraw")
        self.pushButtonscancelmatch = QtWidgets.QPushButton(
            self.tabachedulematches)
        self.pushButtonscancelmatch.setGeometry(QtCore.QRect(180, 460, 75, 23))
        self.pushButtonscancelmatch.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonscancelmatch.setObjectName("pushButtonscancelmatch")
        self.tabWidgetadmin.addTab(self.tabachedulematches, "")
        self.tabdisqualify = QtWidgets.QWidget()
        self.tabdisqualify.setObjectName("tabdisqualify")
        self.labeldisqualifyplayer_2 = QtWidgets.QLabel(self.tabdisqualify)
        self.labeldisqualifyplayer_2.setGeometry(QtCore.QRect(20, 20, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labeldisqualifyplayer_2.setFont(font)
        self.labeldisqualifyplayer_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labeldisqualifyplayer_2.setObjectName("labeldisqualifyplayer_2")
        self.labeldisqualifyplayerid = QtWidgets.QLabel(self.tabdisqualify)
        self.labeldisqualifyplayerid.setGeometry(QtCore.QRect(20, 50, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labeldisqualifyplayerid.setFont(font)
        self.labeldisqualifyplayerid.setAlignment(QtCore.Qt.AlignCenter)
        self.labeldisqualifyplayerid.setObjectName("labeldisqualifyplayerid")
        self.lineEditdisqualifyplayer = QtWidgets.QLineEdit(self.tabdisqualify)
        self.lineEditdisqualifyplayer.setGeometry(
            QtCore.QRect(270, 50, 161, 21))
        self.lineEditdisqualifyplayer.setObjectName("lineEditdisqualifyplayer")
        self.lineEditdisqualifyteam = QtWidgets.QLineEdit(self.tabdisqualify)
        self.lineEditdisqualifyteam.setGeometry(
            QtCore.QRect(270, 170, 161, 21))
        self.lineEditdisqualifyteam.setObjectName("lineEditdisqualifyteam")
        self.labeldisqualifyteam_2 = QtWidgets.QLabel(self.tabdisqualify)
        self.labeldisqualifyteam_2.setGeometry(QtCore.QRect(20, 130, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labeldisqualifyteam_2.setFont(font)
        self.labeldisqualifyteam_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labeldisqualifyteam_2.setObjectName("labeldisqualifyteam_2")
        self.labeldisqualifyteam = QtWidgets.QLabel(self.tabdisqualify)
        self.labeldisqualifyteam.setGeometry(QtCore.QRect(20, 170, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labeldisqualifyteam.setFont(font)
        self.labeldisqualifyteam.setAlignment(QtCore.Qt.AlignCenter)
        self.labeldisqualifyteam.setObjectName("labeldisqualifyteam")
        self.pushButtondisqlalifyplayer = QtWidgets.QPushButton(
            self.tabdisqualify)
        self.pushButtondisqlalifyplayer.setGeometry(
            QtCore.QRect(430, 50, 51, 23))
        self.pushButtondisqlalifyplayer.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondisqlalifyplayer.setObjectName(
            "pushButtondisqlalifyplayer")
        self.pushButtondisqlalifyteam = QtWidgets.QPushButton(
            self.tabdisqualify)
        self.pushButtondisqlalifyteam.setGeometry(
            QtCore.QRect(430, 170, 51, 23))
        self.pushButtondisqlalifyteam.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondisqlalifyteam.setObjectName("pushButtondisqlalifyteam")
        self.tabWidgetadmin.addTab(self.tabdisqualify, "")
        self.tabadddata = QtWidgets.QWidget()
        self.tabadddata.setObjectName("tabadddata")
        self.label = QtWidgets.QLabel(self.tabadddata)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditaddteamid = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditaddteamid.setGeometry(QtCore.QRect(180, 50, 151, 21))
        self.lineEditaddteamid.setObjectName("lineEditaddteamid")
        self.label_2 = QtWidgets.QLabel(self.tabadddata)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabadddata)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdiaddtcounrtyname = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEdiaddtcounrtyname.setGeometry(QtCore.QRect(180, 80, 151, 21))
        self.lineEdiaddtcounrtyname.setObjectName("lineEdiaddtcounrtyname")
        self.label_4 = QtWidgets.QLabel(self.tabadddata)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEditaddnoofbatsmen = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditaddnoofbatsmen.setGeometry(
            QtCore.QRect(180, 110, 151, 21))
        self.lineEditaddnoofbatsmen.setObjectName("lineEditaddnoofbatsmen")
        self.label_5 = QtWidgets.QLabel(self.tabadddata)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditaddnoofbowlers = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditaddnoofbowlers.setGeometry(
            QtCore.QRect(180, 140, 151, 21))
        self.lineEditaddnoofbowlers.setObjectName("lineEditaddnoofbowlers")
        self.label_6 = QtWidgets.QLabel(self.tabadddata)
        self.label_6.setGeometry(QtCore.QRect(350, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditadminaddbatsmandob = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmandob.setGeometry(
            QtCore.QRect(520, 110, 151, 21))
        self.lineEditadminaddbatsmandob.setObjectName(
            "lineEditadminaddbatsmandob")
        self.label_7 = QtWidgets.QLabel(self.tabadddata)
        self.label_7.setGeometry(QtCore.QRect(350, 10, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tabadddata)
        self.label_8.setGeometry(QtCore.QRect(350, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tabadddata)
        self.label_9.setGeometry(QtCore.QRect(350, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEditadminaddplayerbatsmantype = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddplayerbatsmantype.setGeometry(
            QtCore.QRect(520, 140, 151, 21))
        self.lineEditadminaddplayerbatsmantype.setObjectName(
            "lineEditadminaddplayerbatsmantype")
        self.label_10 = QtWidgets.QLabel(self.tabadddata)
        self.label_10.setGeometry(QtCore.QRect(350, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lineEditadminaddbatsmanname = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmanname.setGeometry(
            QtCore.QRect(520, 80, 151, 21))
        self.lineEditadminaddbatsmanname.setObjectName(
            "lineEditadminaddbatsmanname")
        self.lineEditadminaddbatsmanid = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmanid.setGeometry(
            QtCore.QRect(520, 50, 151, 21))
        self.lineEditadminaddbatsmanid.setObjectName(
            "lineEditadminaddbatsmanid")
        self.label_11 = QtWidgets.QLabel(self.tabadddata)
        self.label_11.setGeometry(QtCore.QRect(350, 260, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.lineEditadminaddbatsmanodis = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmanodis.setGeometry(
            QtCore.QRect(520, 230, 151, 21))
        self.lineEditadminaddbatsmanodis.setObjectName(
            "lineEditadminaddbatsmanodis")
        self.label_13 = QtWidgets.QLabel(self.tabadddata)
        self.label_13.setGeometry(QtCore.QRect(350, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabadddata)
        self.label_14.setGeometry(QtCore.QRect(350, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.lineEditadminaddbatsmanteamid = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbatsmanteamid.setGeometry(
            QtCore.QRect(520, 260, 151, 21))
        self.lineEditadminaddbatsmanteamid.setObjectName(
            "lineEditadminaddbatsmanteamid")
        self.label_15 = QtWidgets.QLabel(self.tabadddata)
        self.label_15.setGeometry(QtCore.QRect(350, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.lineEditadminaddbatsmant20s = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmant20s.setGeometry(
            QtCore.QRect(520, 200, 151, 21))
        self.lineEditadminaddbatsmant20s.setObjectName(
            "lineEditadminaddbatsmant20s")
        self.lineEditadminaddbatsmantests = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbatsmantests.setGeometry(
            QtCore.QRect(520, 170, 151, 21))
        self.lineEditadminaddbatsmantests.setObjectName(
            "lineEditadminaddbatsmantests")
        self.label_12 = QtWidgets.QLabel(self.tabadddata)
        self.label_12.setGeometry(QtCore.QRect(350, 320, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(self.tabadddata)
        self.label_16.setGeometry(QtCore.QRect(350, 380, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.tabadddata)
        self.label_18.setGeometry(QtCore.QRect(350, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lineEditadminaddbatsmansix = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmansix.setGeometry(
            QtCore.QRect(520, 320, 151, 21))
        self.lineEditadminaddbatsmansix.setObjectName(
            "lineEditadminaddbatsmansix")
        self.label_19 = QtWidgets.QLabel(self.tabadddata)
        self.label_19.setGeometry(QtCore.QRect(350, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.lineEditadminaddbatsmantot = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmantot.setGeometry(
            QtCore.QRect(520, 380, 151, 21))
        self.lineEditadminaddbatsmantot.setObjectName(
            "lineEditadminaddbatsmantot")
        self.lineEditadminaddbatsmantype = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmantype.setGeometry(
            QtCore.QRect(520, 290, 151, 21))
        self.lineEditadminaddbatsmantype.setObjectName(
            "lineEditadminaddbatsmantype")
        self.label_20 = QtWidgets.QLabel(self.tabadddata)
        self.label_20.setGeometry(QtCore.QRect(350, 440, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.tabadddata)
        self.label_22.setGeometry(QtCore.QRect(350, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.lineEditadminaddbatsmanhigh = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmanhigh.setGeometry(
            QtCore.QRect(520, 410, 151, 21))
        self.lineEditadminaddbatsmanhigh.setObjectName(
            "lineEditadminaddbatsmanhigh")
        self.lineEditadminaddbatsmanfours = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbatsmanfours.setGeometry(
            QtCore.QRect(520, 350, 151, 21))
        self.lineEditadminaddbatsmanfours.setObjectName(
            "lineEditadminaddbatsmanfours")
        self.lineEditadminaddbatsmanavg = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbatsmanavg.setGeometry(
            QtCore.QRect(520, 440, 151, 21))
        self.lineEditadminaddbatsmanavg.setObjectName(
            "lineEditadminaddbatsmanavg")
        self.pushButtonaddteam = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonaddteam.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.pushButtonaddteam.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddteam.setObjectName("pushButtonaddteam")
        self.pushButtonupdateteam = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonupdateteam.setGeometry(QtCore.QRect(130, 170, 75, 23))
        self.pushButtonupdateteam.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdateteam.setObjectName("pushButtonupdateteam")
        self.pushButtondeleteteam = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtondeleteteam.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.pushButtondeleteteam.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeleteteam.setObjectName("pushButtondeleteteam")
        self.lineEditadminaddbowlerteamid = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbowlerteamid.setGeometry(
            QtCore.QRect(860, 260, 151, 21))
        self.lineEditadminaddbowlerteamid.setObjectName(
            "lineEditadminaddbowlerteamid")
        self.lineEditadminaddbowlerid = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlerid.setGeometry(
            QtCore.QRect(860, 50, 151, 21))
        self.lineEditadminaddbowlerid.setObjectName("lineEditadminaddbowlerid")
        self.label_21 = QtWidgets.QLabel(self.tabadddata)
        self.label_21.setGeometry(QtCore.QRect(690, 380, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.tabadddata)
        self.label_17.setGeometry(QtCore.QRect(690, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_23 = QtWidgets.QLabel(self.tabadddata)
        self.label_23.setGeometry(QtCore.QRect(690, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tabadddata)
        self.label_24.setGeometry(QtCore.QRect(690, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.lineEditadminaddbowlerhigh = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlerhigh.setGeometry(
            QtCore.QRect(860, 350, 151, 21))
        self.lineEditadminaddbowlerhigh.setObjectName(
            "lineEditadminaddbowlerhigh")
        self.label_25 = QtWidgets.QLabel(self.tabadddata)
        self.label_25.setGeometry(QtCore.QRect(690, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tabadddata)
        self.label_26.setGeometry(QtCore.QRect(690, 320, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.lineEditadminaddbowlert20s = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlert20s.setGeometry(
            QtCore.QRect(860, 200, 151, 21))
        self.lineEditadminaddbowlert20s.setObjectName(
            "lineEditadminaddbowlert20s")
        self.lineEditadminaddbowlername = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlername.setGeometry(
            QtCore.QRect(860, 80, 151, 21))
        self.lineEditadminaddbowlername.setObjectName(
            "lineEditadminaddbowlername")
        self.label_27 = QtWidgets.QLabel(self.tabadddata)
        self.label_27.setGeometry(QtCore.QRect(690, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tabadddata)
        self.label_28.setGeometry(QtCore.QRect(690, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_30 = QtWidgets.QLabel(self.tabadddata)
        self.label_30.setGeometry(QtCore.QRect(690, 260, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.lineEditadminaddbowlerdob = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlerdob.setGeometry(
            QtCore.QRect(860, 110, 151, 21))
        self.lineEditadminaddbowlerdob.setObjectName(
            "lineEditadminaddbowlerdob")
        self.lineEditadminaddbowlerwickets = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbowlerwickets.setGeometry(
            QtCore.QRect(860, 320, 151, 21))
        self.lineEditadminaddbowlerwickets.setObjectName(
            "lineEditadminaddbowlerwickets")
        self.lineEditadminaddbowlertests = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlertests.setGeometry(
            QtCore.QRect(860, 170, 151, 21))
        self.lineEditadminaddbowlertests.setObjectName(
            "lineEditadminaddbowlertests")
        self.label_31 = QtWidgets.QLabel(self.tabadddata)
        self.label_31.setGeometry(QtCore.QRect(690, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.lineEditadminaddbowlereconomy = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbowlereconomy.setGeometry(
            QtCore.QRect(860, 380, 151, 21))
        self.lineEditadminaddbowlereconomy.setObjectName(
            "lineEditadminaddbowlereconomy")
        self.lineEditadminaddbowlerplayertype = QtWidgets.QLineEdit(
            self.tabadddata)
        self.lineEditadminaddbowlerplayertype.setGeometry(
            QtCore.QRect(860, 140, 151, 21))
        self.lineEditadminaddbowlerplayertype.setObjectName(
            "lineEditadminaddbowlerplayertype")
        self.label_32 = QtWidgets.QLabel(self.tabadddata)
        self.label_32.setGeometry(QtCore.QRect(690, 10, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tabadddata)
        self.label_33.setGeometry(QtCore.QRect(690, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tabadddata)
        self.label_34.setGeometry(QtCore.QRect(690, 290, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.lineEditadminaddbowlertype = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlertype.setGeometry(
            QtCore.QRect(860, 290, 151, 21))
        self.lineEditadminaddbowlertype.setObjectName(
            "lineEditadminaddbowlertype")
        self.lineEditadminaddbowlerodi2 = QtWidgets.QLineEdit(self.tabadddata)
        self.lineEditadminaddbowlerodi2.setGeometry(
            QtCore.QRect(860, 230, 151, 21))
        self.lineEditadminaddbowlerodi2.setObjectName(
            "lineEditadminaddbowlerodi2")
        self.pushButtonaddbatsman = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonaddbatsman.setGeometry(QtCore.QRect(400, 480, 75, 23))
        self.pushButtonaddbatsman.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddbatsman.setObjectName("pushButtonaddbatsman")
        self.pushButtonupdatebatsman = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonupdatebatsman.setGeometry(
            QtCore.QRect(480, 480, 75, 23))
        self.pushButtonupdatebatsman.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdatebatsman.setObjectName("pushButtonupdatebatsman")
        self.pushButtondeletebatsman = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtondeletebatsman.setGeometry(
            QtCore.QRect(560, 480, 75, 23))
        self.pushButtondeletebatsman.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletebatsman.setObjectName("pushButtondeletebatsman")
        self.pushButtonaddbowler = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonaddbowler.setGeometry(QtCore.QRect(740, 410, 75, 23))
        self.pushButtonaddbowler.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddbowler.setObjectName("pushButtonaddbowler")
        self.pushButtonupdatebowler = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtonupdatebowler.setGeometry(QtCore.QRect(820, 410, 75, 23))
        self.pushButtonupdatebowler.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdatebowler.setObjectName("pushButtonupdatebowler")
        self.pushButtondeletebowler = QtWidgets.QPushButton(self.tabadddata)
        self.pushButtondeletebowler.setGeometry(QtCore.QRect(900, 410, 75, 23))
        self.pushButtondeletebowler.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletebowler.setObjectName("pushButtondeletebowler")
        self.tabWidgetadmin.addTab(self.tabadddata, "")
        self.tabdeletedata = QtWidgets.QWidget()
        self.tabdeletedata.setObjectName("tabdeletedata")
        self.lineEditadminaddcoachid = QtWidgets.QLineEdit(self.tabdeletedata)
        self.lineEditadminaddcoachid.setGeometry(
            QtCore.QRect(270, 70, 151, 21))
        self.lineEditadminaddcoachid.setObjectName("lineEditadminaddcoachid")
        self.label_35 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_35.setGeometry(QtCore.QRect(100, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_36.setGeometry(QtCore.QRect(100, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_37.setGeometry(QtCore.QRect(100, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_38.setGeometry(QtCore.QRect(100, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.lineEditadminaddcoachexperience = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcoachexperience.setGeometry(
            QtCore.QRect(270, 220, 151, 21))
        self.lineEditadminaddcoachexperience.setObjectName(
            "lineEditadminaddcoachexperience")
        self.lineEditadminaddcoachteamid = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcoachteamid.setGeometry(
            QtCore.QRect(270, 100, 151, 21))
        self.lineEditadminaddcoachteamid.setObjectName(
            "lineEditadminaddcoachteamid")
        self.label_40 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_40.setGeometry(QtCore.QRect(100, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.lineEditadminaddcoachname = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcoachname.setGeometry(
            QtCore.QRect(270, 130, 151, 21))
        self.lineEditadminaddcoachname.setObjectName(
            "lineEditadminaddcoachname")
        self.lineEditadminaddcoachtype = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcoachtype.setGeometry(
            QtCore.QRect(270, 190, 151, 21))
        self.lineEditadminaddcoachtype.setObjectName(
            "lineEditadminaddcoachtype")
        self.pushButtonaddcoach = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonaddcoach.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.pushButtonaddcoach.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddcoach.setObjectName("pushButtonaddcoach")
        self.lineEditadminaddcoachcountry = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcoachcountry.setGeometry(
            QtCore.QRect(270, 160, 151, 21))
        self.lineEditadminaddcoachcountry.setObjectName(
            "lineEditadminaddcoachcountry")
        self.label_45 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_45.setGeometry(QtCore.QRect(100, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_46.setGeometry(QtCore.QRect(100, 160, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.pushButtondeletecoach = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtondeletecoach.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.pushButtondeletecoach.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletecoach.setObjectName("pushButtondeletecoach")
        self.pushButtonupdatecoach = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonupdatecoach.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.pushButtonupdatecoach.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdatecoach.setObjectName("pushButtonupdatecoach")
        self.lineEditadminaddstadiumid = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddstadiumid.setGeometry(
            QtCore.QRect(810, 340, 151, 21))
        self.lineEditadminaddstadiumid.setObjectName(
            "lineEditadminaddstadiumid")
        self.label_39 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_39.setGeometry(QtCore.QRect(640, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.label_47 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_47.setGeometry(QtCore.QRect(640, 430, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.lineEditadminaddstadiumpitch = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddstadiumpitch.setGeometry(
            QtCore.QRect(810, 400, 151, 21))
        self.lineEditadminaddstadiumpitch.setObjectName(
            "lineEditadminaddstadiumpitch")
        self.label_41 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_41.setGeometry(QtCore.QRect(640, 460, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.label_48 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_48.setGeometry(QtCore.QRect(640, 300, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.label_42 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_42.setGeometry(QtCore.QRect(640, 370, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.pushButtonaddstadium = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonaddstadium.setGeometry(QtCore.QRect(690, 490, 75, 23))
        self.pushButtonaddstadium.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddstadium.setObjectName("pushButtonaddstadium")
        self.lineEditadminaddstadiumcapacity = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddstadiumcapacity.setGeometry(
            QtCore.QRect(810, 430, 151, 21))
        self.lineEditadminaddstadiumcapacity.setObjectName(
            "lineEditadminaddstadiumcapacity")
        self.lineEditadminaddstadiumname = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddstadiumname.setGeometry(
            QtCore.QRect(810, 370, 151, 21))
        self.lineEditadminaddstadiumname.setObjectName(
            "lineEditadminaddstadiumname")
        self.pushButtonupdatestadium = QtWidgets.QPushButton(
            self.tabdeletedata)
        self.pushButtonupdatestadium.setGeometry(
            QtCore.QRect(770, 490, 75, 23))
        self.pushButtonupdatestadium.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdatestadium.setObjectName("pushButtonupdatestadium")
        self.label_44 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_44.setGeometry(QtCore.QRect(640, 340, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.lineEditadminaddstadiummatches = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddstadiummatches.setGeometry(
            QtCore.QRect(810, 460, 151, 21))
        self.lineEditadminaddstadiummatches.setObjectName(
            "lineEditadminaddstadiummatches")
        self.pushButtondeletestadium = QtWidgets.QPushButton(
            self.tabdeletedata)
        self.pushButtondeletestadium.setGeometry(
            QtCore.QRect(850, 490, 75, 23))
        self.pushButtondeletestadium.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletestadium.setObjectName("pushButtondeletestadium")
        self.lineEditadminaddumpirename = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddumpirename.setGeometry(
            QtCore.QRect(260, 370, 151, 21))
        self.lineEditadminaddumpirename.setObjectName(
            "lineEditadminaddumpirename")
        self.label_49 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_49.setGeometry(QtCore.QRect(90, 340, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.pushButtonupdateumpire = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonupdateumpire.setGeometry(QtCore.QRect(220, 490, 75, 23))
        self.pushButtonupdateumpire.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonupdateumpire.setObjectName("pushButtonupdateumpire")
        self.lineEditadminaddumpirematches = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddumpirematches.setGeometry(
            QtCore.QRect(260, 430, 151, 21))
        self.lineEditadminaddumpirematches.setObjectName(
            "lineEditadminaddumpirematches")
        self.pushButtonaddumpire = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonaddumpire.setGeometry(QtCore.QRect(140, 490, 75, 23))
        self.pushButtonaddumpire.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddumpire.setObjectName("pushButtonaddumpire")
        self.label_43 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_43.setGeometry(QtCore.QRect(90, 400, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.lineEditadminaddumpirecountry = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddumpirecountry.setGeometry(
            QtCore.QRect(260, 400, 151, 21))
        self.lineEditadminaddumpirecountry.setObjectName(
            "lineEditadminaddumpirecountry")
        self.lineEditadminaddumpireexperience = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddumpireexperience.setGeometry(
            QtCore.QRect(260, 460, 151, 21))
        self.lineEditadminaddumpireexperience.setObjectName(
            "lineEditadminaddumpireexperience")
        self.pushButtonadddelete = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonadddelete.setGeometry(QtCore.QRect(300, 490, 75, 23))
        self.pushButtonadddelete.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonadddelete.setObjectName("pushButtonadddelete")
        self.lineEditadminaddumpireid = QtWidgets.QLineEdit(self.tabdeletedata)
        self.lineEditadminaddumpireid.setGeometry(
            QtCore.QRect(260, 340, 151, 21))
        self.lineEditadminaddumpireid.setObjectName("lineEditadminaddumpireid")
        self.label_50 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_50.setGeometry(QtCore.QRect(90, 430, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_51.setGeometry(QtCore.QRect(90, 370, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_52.setGeometry(QtCore.QRect(90, 300, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_53.setGeometry(QtCore.QRect(90, 460, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.line_2 = QtWidgets.QFrame(self.tabdeletedata)
        self.line_2.setGeometry(QtCore.QRect(520, 10, 21, 541))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEditadminaddcaptainplayerid = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptainplayerid.setGeometry(
            QtCore.QRect(810, 90, 151, 21))
        self.lineEditadminaddcaptainplayerid.setObjectName(
            "lineEditadminaddcaptainplayerid")
        self.label_54 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_54.setGeometry(QtCore.QRect(640, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.pushButtondeletecaptain = QtWidgets.QPushButton(
            self.tabdeletedata)
        self.pushButtondeletecaptain.setGeometry(
            QtCore.QRect(770, 240, 75, 23))
        self.pushButtondeletecaptain.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletecaptain.setObjectName("pushButtondeletecaptain")
        self.lineEditadminaddcaptainwins = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptainwins.setGeometry(
            QtCore.QRect(810, 180, 151, 21))
        self.lineEditadminaddcaptainwins.setObjectName(
            "lineEditadminaddcaptainwins")
        self.pushButtonaddcaptain = QtWidgets.QPushButton(self.tabdeletedata)
        self.pushButtonaddcaptain.setGeometry(QtCore.QRect(690, 240, 75, 23))
        self.pushButtonaddcaptain.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtonaddcaptain.setObjectName("pushButtonaddcaptain")
        self.pushButtondeletecaptain_2 = QtWidgets.QPushButton(
            self.tabdeletedata)
        self.pushButtondeletecaptain_2.setGeometry(
            QtCore.QRect(850, 240, 75, 23))
        self.pushButtondeletecaptain_2.setStyleSheet(
            "background-color: rgb(139, 224, 255);")
        self.pushButtondeletecaptain_2.setObjectName(
            "pushButtondeletecaptain_2")
        self.lineEditadminaddcaptaintrophies = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptaintrophies.setGeometry(
            QtCore.QRect(810, 210, 151, 21))
        self.lineEditadminaddcaptaintrophies.setObjectName(
            "lineEditadminaddcaptaintrophies")
        self.lineEditadminaddcaptainyears = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptainyears.setGeometry(
            QtCore.QRect(810, 150, 151, 21))
        self.lineEditadminaddcaptainyears.setObjectName(
            "lineEditadminaddcaptainyears")
        self.label_55 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_55.setGeometry(QtCore.QRect(640, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_56.setGeometry(QtCore.QRect(640, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_57.setGeometry(QtCore.QRect(640, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.lineEditadminaddcaptainid = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptainid.setGeometry(
            QtCore.QRect(810, 60, 151, 21))
        self.lineEditadminaddcaptainid.setObjectName(
            "lineEditadminaddcaptainid")
        self.label_58 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_58.setGeometry(QtCore.QRect(640, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_59.setGeometry(QtCore.QRect(640, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.lineEditadminaddcaptainname = QtWidgets.QLineEdit(
            self.tabdeletedata)
        self.lineEditadminaddcaptainname.setGeometry(
            QtCore.QRect(810, 120, 151, 21))
        self.lineEditadminaddcaptainname.setObjectName(
            "lineEditadminaddcaptainname")
        self.label_60 = QtWidgets.QLabel(self.tabdeletedata)
        self.label_60.setGeometry(QtCore.QRect(640, 120, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.tabWidgetadmin.addTab(self.tabdeletedata, "")
        self.gridLayout.addWidget(self.tabWidgetadmin, 0, 0, 1, 1)

        self.retranslateUi(Admin)
        self.tabWidgetadmin.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Admin)

        self.pushButtonschedulematch.clicked.connect(self.schedule)
        self.pushButtonsupdatematch.clicked.connect(self.reschedule)
        self.pushButtonupdateresult.clicked.connect(self.updateresult)
        self.radioButtonwonbyruns.clicked.connect(self.setrun)
        self.radioButtonwonbywickets.clicked.connect(self.setwicket)
        self.pushButtondisqlalifyplayer.clicked.connect(self.disqualifyplayer)
        self.pushButtondisqlalifyteam.clicked.connect(self.disqualifyteam)
        self.pushButtondraw.clicked.connect(self.resultdraw)
        self.pushButtonscancelmatch.clicked.connect(self.cancelmatch)
        self.pushButtonaddteam.clicked.connect(self.addTeam)
        self.pushButtonupdateteam.clicked.connect(self.updateTeam)
        self.pushButtondeleteteam.clicked.connect(self.deleteTeam)
        self.pushButtonaddbatsman.clicked.connect(self.addBatsman)
        self.pushButtonupdatebatsman.clicked.connect(self.updateBatsman)
        self.pushButtondeletebatsman.clicked.connect(self.deleteBatsman)
        self.pushButtonaddbowler.clicked.connect(self.addBowler)
        self.pushButtonupdatebowler.clicked.connect(self.updateBowler)
        self.pushButtondeletebowler.clicked.connect(self.deleteBowler)
        self.pushButtonaddcoach.clicked.connect(self.addCoach)
        self.pushButtonupdatecoach.clicked.connect(self.updateCoach)
        self.pushButtondeletecoach.clicked.connect(self.deleteCoach)
        self.pushButtonaddumpire.clicked.connect(self.addUmpire)
        self.pushButtonupdateumpire.clicked.connect(self.updateUmpire)
        self.pushButtonadddelete.clicked.connect(self.deleteUmpire)
        self.pushButtonaddcaptain.clicked.connect(self.addCaptain)
        self.pushButtondeletecaptain.clicked.connect(self.updateCaptain)
        self.pushButtondeletecaptain_2.clicked.connect(self.deleteCaptain)
        self.pushButtonaddstadium.clicked.connect(self.addStadium)
        self.pushButtonupdatestadium.clicked.connect(self.updateStadium)
        self.pushButtondeletestadium.clicked.connect(self.deleteStadium)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Form"))
        self.lineEditteam1.setPlaceholderText(
            _translate("Admin", "Team 1 ID (ex:IND)"))
        self.lineEditteam2.setPlaceholderText(
            _translate("Admin", "Team 2 ID (ex:AUS)"))
        self.labelteam1id.setText(_translate("Admin", "TEAM 1 ID :"))
        self.labelteam2id.setText(_translate("Admin", "TEAM 2 ID :"))
        self.labeldate.setText(_translate("Admin", "ENTER DATE :"))
        self.labeltime.setText(_translate("Admin", "ENTER TIME :"))
        self.lineEditdate.setPlaceholderText(
            _translate("Admin", "Date (DD-MMM-YYYY)"))
        self.lineEdittime.setPlaceholderText(
            _translate("Admin", "Time (HH-MM-SS am/pm)"))
        self.pushButtonschedulematch.setText(_translate("Admin", "SCHEDULE"))
        self.labelschedulematches.setText(
            _translate("Admin", "SCHEDULE MATCH"))
        self.labelupdateresult.setText(_translate("Admin", "UPDATE RESULT"))
        self.lineEditresultwinner.setPlaceholderText(
            _translate("Admin", "Winner Team ID (ex:IND)"))
        self.labelwinnerteam.setText(_translate("Admin", "WINNER TEAM ID"))
        self.labelmatchid.setText(_translate("Admin", "MATCH ID"))
        self.lineEditresultmatchid.setPlaceholderText(
            _translate("Admin", "Match ID (ex:1)"))
        self.labelmanofthematch.setText(
            _translate("Admin", "MAN OF THE MATCH"))
        self.lineEditresultmanofmatch.setPlaceholderText(
            _translate("Admin", "Player ID (ex:IND01)"))
        self.labelwonby.setText(_translate("Admin", "WON BY WICKETS OR RUNS"))
        self.lineEditresultrunsorwickets.setPlaceholderText(
            _translate("Admin", "Number of Runs or Wickets"))
        self.radioButtonwonbywickets.setText(
            _translate("Admin", "WON BY WICKETS"))
        self.radioButtonwonbyruns.setText(_translate("Admin", "WON BY RUNS"))
        self.pushButtonupdateresult.setText(_translate("Admin", "UPDATE"))
        self.labeltime_2.setText(_translate("Admin", "UMPIRE 1 ID:"))
        self.lineEditumpire1.setPlaceholderText(
            _translate("Admin", "Umpire ID(ex : ump01)"))
        self.labeltime_3.setText(_translate("Admin", "UMPIRE 2 ID:"))
        self.lineEditumpire2.setPlaceholderText(
            _translate("Admin", "Umpire ID(ex : ump02)"))
        self.labeltime_4.setText(_translate("Admin", "UMPIRE 3 ID:"))
        self.lineEditumpire3.setPlaceholderText(
            _translate("Admin", "Umpire ID(ex : ump03)"))
        self.pushButtonsupdatematch.setText(_translate("Admin", "RESCHEDULE"))
        self.labelteam1id_2.setText(_translate("Admin", "STADIUM ID:"))
        self.lineEditstadiumid.setPlaceholderText(
            _translate("Admin", "Stadium id (ex : ST01)"))
        self.lineEditschedulematchid.setPlaceholderText(
            _translate("Admin", "Match ID (ex:1)"))
        self.labelmatchid_2.setText(_translate("Admin", "MATCH ID"))
        self.pushButtondraw.setText(_translate("Admin", "UPDATE MATCH DRAW"))
        self.pushButtonscancelmatch.setText(_translate("Admin", "CANCEL"))
        self.tabWidgetadmin.setTabText(self.tabWidgetadmin.indexOf(
            self.tabachedulematches), _translate("Admin", "SCHEDULE MATCHES"))
        self.labeldisqualifyplayer_2.setText(
            _translate("Admin", "DISQUALIFY A PLAYER"))
        self.labeldisqualifyplayerid.setText(_translate("Admin", " PLAYER ID"))
        self.lineEditdisqualifyplayer.setPlaceholderText(
            _translate("Admin", "Player ID (ex:PAK01)"))
        self.lineEditdisqualifyteam.setPlaceholderText(
            _translate("Admin", "Team ID (ex:PAK)"))
        self.labeldisqualifyteam_2.setText(
            _translate("Admin", "DISQUALIFY A TEAM"))
        self.labeldisqualifyteam.setText(_translate("Admin", "TEAM ID"))
        self.pushButtondisqlalifyplayer.setText(_translate("Admin", "GO"))
        self.pushButtondisqlalifyteam.setText(_translate("Admin", "GO"))
        self.tabWidgetadmin.setTabText(self.tabWidgetadmin.indexOf(
            self.tabdisqualify), _translate("Admin", "DISQUALIFY"))
        self.label.setText(_translate("Admin", "TEAM"))
        self.label_2.setText(_translate("Admin", "TEAM ID"))
        self.label_3.setText(_translate("Admin", "COUNTRY NAME"))
        self.label_4.setText(_translate("Admin", "NUM OF BATSMEN"))
        self.label_5.setText(_translate("Admin", "NUM OF BOWLERS"))
        self.label_6.setText(_translate("Admin", "TYPE OF PLAYER"))
        self.label_7.setText(_translate("Admin", "BATSMAN"))
        self.label_8.setText(_translate("Admin", "NAME"))
        self.label_9.setText(_translate("Admin", "DOB"))
        self.label_10.setText(_translate("Admin", "PLAYER ID"))
        self.label_11.setText(_translate("Admin", "TEAM ID"))
        self.label_13.setText(_translate("Admin", "NUM OF T20S"))
        self.label_14.setText(_translate("Admin", "NUM OF ODIS"))
        self.label_15.setText(_translate("Admin", "NUM OF TESTS"))
        self.label_12.setText(_translate("Admin", "NUM OF SIXES"))
        self.label_16.setText(_translate("Admin", "TOTAL RUNS"))
        self.label_18.setText(_translate("Admin", "HIGHEST RUNS"))
        self.label_19.setText(_translate("Admin", "BATSMAN TYPE"))
        self.label_20.setText(_translate("Admin", "BATTING AVG"))
        self.label_22.setText(_translate("Admin", "NUM OF FOURS"))
        self.pushButtonaddteam.setText(_translate("Admin", "INSERT"))
        self.pushButtonupdateteam.setText(_translate("Admin", "UPDATE"))
        self.pushButtondeleteteam.setText(_translate("Admin", "DELETE"))
        self.label_21.setText(_translate("Admin", "ECONOMY"))
        self.label_17.setText(_translate("Admin", "NUM OF TESTS"))
        self.label_23.setText(_translate("Admin", "NUM OF T20S"))
        self.label_24.setText(_translate("Admin", "DOB"))
        self.label_25.setText(_translate("Admin", "NAME"))
        self.label_26.setText(_translate("Admin", "NUM OF WICKETS"))
        self.label_27.setText(_translate("Admin", "PLAYER ID"))
        self.label_28.setText(_translate("Admin", "NUM OF ODIS"))
        self.label_30.setText(_translate("Admin", "TEAM ID"))
        self.label_31.setText(_translate("Admin", "HIGHEST SPEED"))
        self.label_32.setText(_translate("Admin", "BOWLER"))
        self.label_33.setText(_translate("Admin", "TYPE OF PLAYER"))
        self.label_34.setText(_translate("Admin", "BOWLER TYPE"))
        self.pushButtonaddbatsman.setText(_translate("Admin", "INSERT"))
        self.pushButtonupdatebatsman.setText(_translate("Admin", "UPDATE"))
        self.pushButtondeletebatsman.setText(_translate("Admin", "DELETE"))
        self.pushButtonaddbowler.setText(_translate("Admin", "INSERT"))
        self.pushButtonupdatebowler.setText(_translate("Admin", "UPDATE"))
        self.pushButtondeletebowler.setText(_translate("Admin", "DELETE"))
        self.tabWidgetadmin.setTabText(self.tabWidgetadmin.indexOf(
            self.tabadddata), _translate("Admin", "MODIFY DATA"))
        self.label_35.setText(_translate("Admin", "TYPE"))
        self.label_36.setText(_translate("Admin", "EXPERIENCE"))
        self.label_37.setText(_translate("Admin", "NAME"))
        self.label_38.setText(_translate("Admin", "TEAM ID"))
        self.label_40.setText(_translate("Admin", "COACH ID"))
        self.pushButtonaddcoach.setText(_translate("Admin", "INSERT"))
        self.label_45.setText(_translate("Admin", "COACH"))
        self.label_46.setText(_translate("Admin", "COUNTRY"))
        self.pushButtondeletecoach.setText(_translate("Admin", "DELETE"))
        self.pushButtonupdatecoach.setText(_translate("Admin", "UPDATE"))
        self.label_39.setText(_translate("Admin", "PITCH TYPE"))
        self.label_47.setText(_translate("Admin", "CAPACITY"))
        self.label_41.setText(_translate("Admin", "NUM OF MATCHES"))
        self.label_48.setText(_translate("Admin", "STADIUM"))
        self.label_42.setText(_translate("Admin", "NAME"))
        self.pushButtonaddstadium.setText(_translate("Admin", "INSERT"))
        self.pushButtonupdatestadium.setText(_translate("Admin", "UPDATE"))
        self.label_44.setText(_translate("Admin", "STADIUM ID"))
        self.pushButtondeletestadium.setText(_translate("Admin", "DELETE"))
        self.label_49.setText(_translate("Admin", "UMPIRE ID"))
        self.pushButtonupdateumpire.setText(_translate("Admin", "UPDATE"))
        self.pushButtonaddumpire.setText(_translate("Admin", "INSERT"))
        self.label_43.setText(_translate("Admin", "COUNTRY"))
        self.pushButtonadddelete.setText(_translate("Admin", "DELETE"))
        self.label_50.setText(_translate("Admin", "NUM OF MATCHES"))
        self.label_51.setText(_translate("Admin", "NAME"))
        self.label_52.setText(_translate("Admin", "UMPIRE"))
        self.label_53.setText(_translate("Admin", "EXPERIENCE"))
        self.label_54.setText(_translate("Admin", "TEAM ID"))
        self.pushButtondeletecaptain.setText(_translate("Admin", "UPDATE"))
        self.pushButtonaddcaptain.setText(_translate("Admin", "INSERT"))
        self.pushButtondeletecaptain_2.setText(_translate("Admin", "DELETE"))
        self.label_55.setText(_translate("Admin", "YEARS"))
        self.label_56.setText(_translate("Admin", "PLAYER ID"))
        self.label_57.setText(_translate("Admin", "NUM OF WINS"))
        self.label_58.setText(_translate("Admin", "CAPTAIN"))
        self.label_59.setText(_translate("Admin", "NUM OF TROPHIES"))
        self.label_60.setText(_translate("Admin", "NAME"))
        self.tabWidgetadmin.setTabText(self.tabWidgetadmin.indexOf(
            self.tabdeletedata), _translate("Admin", "MODIFY DATA2"))

    def schedule(self):
        team1 = ""
        team2 = ""
        sdate = ""
        stime = ""
        stid = ""
        uid1 = ""
        uid2 = ""
        uid3 = ""

        team1 = self.lineEditteam1.text()
        team2 = self.lineEditteam2.text()
        sdate = self.lineEditdate.text()
        stime = self.lineEdittime.text()
        stid = self.lineEditstadiumid.text()
        uid1 = self.lineEditumpire1.text()
        uid2 = self.lineEditumpire2.text()
        uid3 = self.lineEditumpire3.text()

        self.conn = sqlite3.connect("worldcup.db")
        self.c = self.conn.cursor()
        self.c.execute("select disqualified from team where team_id like '" +
                       team1+"' or team_id like '"+team2+"'")
        status = ["A"] * 10
        i = 0
        for row in self.c:
            status[i] = row[0]
            i = i+1
        if status[0] == "YES" or status[1] == "YES":
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Schedule Match")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            try:
                self.c.execute(
                    "INSERT INTO matches(team1_id,team2_id, stadium_id, match_date_time ) VALUES (?, ?, ?, ?)", (team1, team2, stid, sdate+" "+stime))
                self.c.execute(
                    "select seq from sqlite_sequence where name like 'matches'")
                for row in self.c:
                    matchid = row[0]
                self.c.execute(
                    "insert into umpired_by(match_id,u_id) values (?,?)", (matchid, uid1))
                self.c.execute(
                    "insert into umpired_by(match_id,u_id) values (?,?)", (matchid, uid2))
                self.c.execute(
                    "insert into umpired_by(match_id,u_id) values (?,?)", (matchid, uid3))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                msg = QMessageBox()
                msg.setWindowTitle("Message Display")
                msg.setText("Scheduled Successfully Match id = "+str(matchid))
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()

            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle("Message Display")
                msg.setText("Cannot Schedule")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

    def reschedule(self):

        matchid = ""
        sdate = ""
        stime = ""

        sdate = self.lineEditdate.text()
        stime = self.lineEdittime.text()
        matchid = self.lineEditschedulematchid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute("update matches set match_date_time ='" +
                           str(sdate)+" "+str(stime)+"' where match_id = " + str(matchid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Rescheduled Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Reschedule")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def cancelmatch(self):
        matchid = ""
        matchid = self.lineEditschedulematchid.text()
        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from matches where match_id = " + str(matchid))
            self.c.execute(
                "delete from umpired_by where match_id = " + str(matchid))
            self.c.execute(
                "delete from umpired_by where match_id = " + str(matchid))
            self.c.execute(
                "delete from umpired_by where match_id = " + str(matchid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cancelled Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cancel Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def setwicket(self):
        self.awonby = " wickets"

    def setrun(self):
        self.awonby = " runs"

    def updateresult(self):
        amatchid = ""
        awinner = ""
        amanofmatch = ""
        awon = ""

        amatchid = self.lineEditresultmatchid.text()
        awinner = self.lineEditresultwinner.text()
        amanofmatch = self.lineEditresultmanofmatch.text()
        awon = self.lineEditresultrunsorwickets.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            cur = self.conn.cursor()
            self.c.execute(
                "INSERT INTO results(match_id, winner_team, won_by_runs_or_wickets, man_of_the_match  ) VALUES (?, ?, ?, ?)", (amatchid, awinner, awinner+" won by "+awon + self.awonby, amanofmatch))
            self.c.execute(
                "update points_table set points = (points + 2) where team_id = '"+awinner+"'")
            self.c.execute(
                "update points_table set number_of_wins = (number_of_wins + 1) where team_id = '"+awinner+"'")
            rank = 1
            cur.execute(
                "select team_id from points_table order by points desc")
            for row_data in cur:
                self.c.execute("update points_table set team_rank = " +
                               str(rank)+" where team_id like '"+row_data[0]+"'")
                print(row_data[0]+"-"+str(rank))
                rank = rank+1

            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Result Updated Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Result Unsuccesful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def disqualifyplayer(self):
        aplayerid = ""
        aplayerid = self.lineEditdisqualifyplayer.text()
        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update player set p_disqualified ='YES' where player_id='"+str(aplayerid)+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Player disqualified Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Player Disqualification Unsuccesful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def disqualifyteam(self):
        ateamid = ""
        ateamid = self.lineEditdisqualifyteam.text()
        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update team set disqualified ='YES' where team_id='"+str(ateamid)+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Team disqualified Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Team Disqualification Unsuccesful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def resultdraw(self):
        amatchid = ""

        amatchid = self.lineEditresultmatchid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            cur = self.conn.cursor()
            self.c.execute(
                "INSERT INTO results(match_id, won_by_runs_or_wickets ) VALUES (?, ?)", (amatchid, "draw"))
            self.c.execute(
                "update points_table set points = (points + 1) where team_id = (select team1_id from matches where match_id="+str(amatchid)+")")
            self.c.execute(
                "update points_table set points = (points + 1) where team_id = (select team2_id from matches where match_id="+str(amatchid)+")")
            self.c.execute(
                "update points_table set number_of_draw = (number_of_draw + 1) where team_id = (select team1_id from matches where match_id="+str(amatchid)+")")
            self.c.execute(
                "update points_table set number_of_draw = (number_of_draw + 1) where team_id = (select team2_id from matches where match_id="+str(amatchid)+")")

            rank = 1
            cur.execute(
                "select team_id from points_table order by points desc")
            for row_data in cur:
                self.c.execute("update points_table set team_rank = " +
                               str(rank)+" where team_id like '"+row_data[0]+"'")
                print(row_data[0]+"-"+str(rank))
                rank = rank+1

            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Result Updated Successfully")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Result Unsuccesful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addTeam(self):
        team_id = ""
        country_name = ""
        no_of_batsmen = ""
        no_of_bowlers = ""

        team_id = self.lineEditaddteamid.text()
        country_name = self.lineEdiaddtcounrtyname.text()
        no_of_batsmen = self.lineEditaddnoofbatsmen.text()
        no_of_bowlers = self.lineEditaddnoofbowlers.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO team VALUES (?, ?, ?, ?, ?)", (team_id, country_name, no_of_batsmen, no_of_bowlers, 'NO'))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateTeam(self):
        team_id = ""
        country_name = ""
        no_of_batsmen = ""
        no_of_bowlers = ""

        team_id = self.lineEditaddteamid.text()
        country_name = self.lineEdiaddtcounrtyname.text()
        no_of_batsmen = self.lineEditaddnoofbatsmen.text()
        no_of_bowlers = self.lineEditaddnoofbowlers.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update team set country_name= '"+country_name+"', no_of_batsmen= "+str(no_of_batsmen) +
                ", no_of_bowlers= "+str(no_of_bowlers)+" where team_id = '"+team_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteTeam(self):
        team_id = ""

        team_id = self.lineEditaddteamid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from team where team_id='"+team_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addBatsman(self):
        player_id = ""
        player_name = ""
        dob = ""
        type_of_player = ""
        no_of_tests = ""
        no_of_t20s = ""
        no_of_ODIs = ""
        team_id = ""
        batsman_type = ""
        number_of_sixes = ""
        number_of_fours = ""
        total_runs = ""
        highest_runs = ""
        batting_average = ""

        player_id = self.lineEditadminaddbatsmanid.text()
        player_name = self.lineEditadminaddbatsmanname.text()
        dob = self.lineEditadminaddbatsmandob.text()
        type_of_player = self.lineEditadminaddplayerbatsmantype.text()
        no_of_tests = self.lineEditadminaddbatsmantests.text()
        no_of_t20s = self.lineEditadminaddbatsmant20s.text()
        no_of_ODIs = self.lineEditadminaddbatsmanodis.text()
        team_id = self.lineEditadminaddbatsmanteamid.text()
        batsman_type = self.lineEditadminaddbatsmantype.text()
        number_of_sixes = self.lineEditadminaddbatsmansix.text()
        number_of_fours = self.lineEditadminaddbatsmanfours.text()
        total_runs = self.lineEditadminaddbatsmantot.text()
        highest_runs = self.lineEditadminaddbatsmanhigh.text()
        batting_average = self.lineEditadminaddbatsmanavg.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO player VALUES (?, ?, ?, ?, ?,?,?,?,?)", (player_id, player_name, dob, type_of_player, no_of_tests, no_of_t20s, no_of_ODIs, team_id, 'NO'))
            self.c.execute(
                "INSERT INTO batsman VALUES (?, ?, ?, ?, ?,?,?)", (player_id, batsman_type, number_of_sixes, number_of_fours, total_runs, highest_runs, batting_average))

            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateBatsman(self):
        player_id = ""
        player_name = ""
        dob = ""
        type_of_player = ""
        no_of_tests = ""
        no_of_t20s = ""
        no_of_ODIs = ""
        team_id = ""
        batsman_type = ""
        number_of_sixes = ""
        number_of_fours = ""
        total_runs = ""
        highest_runs = ""
        batting_average = ""

        player_id = self.lineEditadminaddbatsmanid.text()
        player_name = self.lineEditadminaddbatsmanname.text()
        dob = self.lineEditadminaddbatsmandob.text()
        type_of_player = self.lineEditadminaddplayerbatsmantype.text()
        no_of_tests = self.lineEditadminaddbatsmantests.text()
        no_of_t20s = self.lineEditadminaddbatsmant20s.text()
        no_of_ODIs = self.lineEditadminaddbatsmanodis.text()
        team_id = self.lineEditadminaddbatsmanteamid.text()
        batsman_type = self.lineEditadminaddbatsmantype.text()
        number_of_sixes = self.lineEditadminaddbatsmansix.text()
        number_of_fours = self.lineEditadminaddbatsmanfours.text()
        total_runs = self.lineEditadminaddbatsmantot.text()
        highest_runs = self.lineEditadminaddbatsmanhigh.text()
        batting_average = self.lineEditadminaddbatsmanavg.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update player set player_name='"+player_name+"', dob='"+dob+"', type_of_player='"+type_of_player+"', no_of_tests="+str(no_of_tests)+", no_of_t20s="+str(no_of_t20s)+", no_of_ODIs="+str(no_of_ODIs)+", team_id='"+team_id+"' where player_id='"+player_id+"'")
            self.c.execute(
                "update batsman set player_id='"+player_id+"', batsman_type='"+batsman_type+"', number_of_sixes='"+str(number_of_sixes)+"', number_of_fours="+str(number_of_fours)+", total_runs="+str(total_runs)+", highest_runs="+str(highest_runs)+", batting_average='"+str(batting_average)+"' where player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteBatsman(self):
        player_id = ""

        player_id = self.lineEditadminaddbatsmanid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from batsman where player_id='"+player_id+"'")
            self.c.execute(
                "delete from player where player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addBowler(self):
        player_id = ""
        player_name = ""
        dob = ""
        type_of_player = ""
        no_of_tests = ""
        no_of_t20s = ""
        no_of_ODIs = ""
        team_id = ""
        bowler_type = ""
        number_of_wickets = ""
        highest_speed = ""
        economy = ""

        player_id = self.lineEditadminaddbowlerid.text()
        player_name = self.lineEditadminaddbowlername.text()
        dob = self.lineEditadminaddbowlerdob.text()
        type_of_player = self.lineEditadminaddbowlerplayertype.text()
        no_of_tests = self.lineEditadminaddbowlertests.text()
        no_of_t20s = self.lineEditadminaddbowlert20s.text()
        no_of_ODIs = self.lineEditadminaddbowlerodi2.text()
        team_id = self.lineEditadminaddbowlerteamid.text()
        bowler_type = self.lineEditadminaddbowlertype.text()
        number_of_wickets = self.lineEditadminaddbowlerwickets.text()
        highest_speed = self.lineEditadminaddbowlerhigh.text()
        economy = self.lineEditadminaddbowlereconomy.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO player VALUES (?, ?, ?, ?, ?,?,?,?,?)", (player_id, player_name, dob, type_of_player, no_of_tests, no_of_t20s, no_of_ODIs, team_id, 'NO'))
            self.c.execute(
                "INSERT INTO bowler VALUES (?, ?, ?, ?, ?)", (player_id, bowler_type, number_of_wickets, highest_speed, economy))

            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateBowler(self):
        player_id = ""
        player_name = ""
        dob = ""
        type_of_player = ""
        no_of_tests = ""
        no_of_t20s = ""
        no_of_ODIs = ""
        team_id = ""
        bowler_type = ""
        number_of_wickets = ""
        highest_speed = ""
        economy = ""

        player_id = self.lineEditadminaddbowlerid.text()
        player_name = self.lineEditadminaddbowlername.text()
        dob = self.lineEditadminaddbowlerdob.text()
        type_of_player = self.lineEditadminaddbowlerplayertype.text()
        no_of_tests = self.lineEditadminaddbowlertests.text()
        no_of_t20s = self.lineEditadminaddbowlert20s.text()
        no_of_ODIs = self.lineEditadminaddbowlerodi2.text()
        team_id = self.lineEditadminaddbowlerteamid.text()
        bowler_type = self.lineEditadminaddbowlertype.text()
        number_of_wickets = self.lineEditadminaddbowlerwickets.text()
        highest_speed = self.lineEditadminaddbowlerhigh.text()
        economy = self.lineEditadminaddbowlereconomy.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update player set player_name='"+player_name+"', dob='"+dob+"', type_of_player='"+type_of_player+"', no_of_tests="+str(no_of_tests)+", no_of_t20s="+str(no_of_t20s)+", no_of_ODIs="+str(no_of_ODIs)+", team_id='"+team_id+"' where player_id='"+player_id+"'")
            self.c.execute(
                "update bowler set player_id='"+player_id+"', bowler_type='"+bowler_type+"', number_of_wickets="+str(number_of_wickets)+", highest_speed="+str(highest_speed)+", economy="+str(economy)+" where player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteBowler(self):
        player_id = ""

        player_id = self.lineEditadminaddbowlerid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from bowler where player_id='"+player_id+"'")
            self.c.execute(
                "delete from player where player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addCoach(self):
        coach_id = ""
        team_id = ""
        coach_name = ""
        coach_country = ""
        coach_type = ""
        coach_experience = ""

        coach_id = self.lineEditadminaddcoachid.text()
        team_id = self.lineEditadminaddcoachteamid.text()
        coach_name = self.lineEditadminaddcoachname.text()
        coach_country = self.lineEditadminaddcoachcountry.text()
        coach_type = self.lineEditadminaddcoachtype.text()
        coach_experience = self.lineEditadminaddcoachexperience.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO coach VALUES (?, ?, ?, ?, ?,?)", (coach_id, team_id, coach_name, coach_country, coach_type, coach_experience))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateCoach(self):
        coach_id = ""
        team_id = ""
        coach_name = ""
        coach_country = ""
        coach_type = ""
        coach_experience = ""

        coach_id = self.lineEditadminaddcoachid.text()
        team_id = self.lineEditadminaddcoachteamid.text()
        coach_name = self.lineEditadminaddcoachname.text()
        coach_country = self.lineEditadminaddcoachcountry.text()
        coach_type = self.lineEditadminaddcoachtype.text()
        coach_experience = self.lineEditadminaddcoachexperience.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update coach set team_id='"+team_id+"', coach_name='"+coach_name+"', coach_country='"+coach_country+"', coach_type='"+coach_type+"', coach_experience='"+str(coach_experience)+"' where coach_id='"+coach_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteCoach(self):
        coach_id = ""
        coach_id = self.lineEditadminaddcoachid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from coach where coach_id='"+coach_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addUmpire(self):
        u_id = ""
        u_name = ""
        u_country = ""
        number_of_matches = ""
        u_experience = ""

        u_id = self.lineEditadminaddumpireid.text()
        u_name = self.lineEditadminaddumpirename.text()
        u_country = self.lineEditadminaddumpirecountry.text()
        number_of_matches = self.lineEditadminaddumpirematches.text()
        u_experienceype = self.lineEditadminaddumpireexperience.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO umpire VALUES (?, ?, ?, ?, ?)", (u_id, u_name, u_country, number_of_matches, u_experienceype))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateUmpire(self):
        u_id = ""
        u_name = ""
        u_country = ""
        number_of_matches = ""
        u_experience = ""

        u_id = self.lineEditadminaddumpireid.text()
        u_name = self.lineEditadminaddumpirename.text()
        u_country = self.lineEditadminaddumpirecountry.text()
        number_of_matches = self.lineEditadminaddumpirematches.text()
        u_experience = self.lineEditadminaddumpireexperience.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update umpire set u_name='"+u_name+"', u_country='"+u_country+"', number_of_matches="+str(number_of_matches)+", u_experience="+str(u_experience)+" where u_id='"+u_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteUmpire(self):
        u_id = ""
        u_id = self.lineEditadminaddumpireid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from umpire where u_id='"+u_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addCaptain(self):
        team_id = ""
        player_id = ""
        name = ""
        years_of_captaincy = ""
        number_of_wins = ""
        number_of_trophies = ""

        team_id = self.lineEditadminaddcaptainid.text()
        player_id = self.lineEditadminaddcaptainplayerid.text()
        name = self.lineEditadminaddcaptainname.text()
        years_of_captaincy = self.lineEditadminaddcaptainyears.text()
        number_of_wins = self.lineEditadminaddcaptainwins.text()
        number_of_trophies = self.lineEditadminaddcaptaintrophies.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO captain VALUES (?, ?, ?, ?, ?, ?)", (team_id, player_id, name, years_of_captaincy, number_of_wins, number_of_trophies))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateCaptain(self):
        team_id = ""
        player_id = ""
        name = ""
        years_of_captaincy = ""
        number_of_wins = ""
        number_of_trophies = ""

        team_id = self.lineEditadminaddcaptainid.text()
        player_id = self.lineEditadminaddcaptainplayerid.text()
        name = self.lineEditadminaddcaptainname.text()
        years_of_captaincy = self.lineEditadminaddcaptainyears.text()
        number_of_wins = self.lineEditadminaddcaptainwins.text()
        number_of_trophies = self.lineEditadminaddcaptaintrophies.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update captain set name='"+name+"', years_of_captaincy="+str(years_of_captaincy)+", number_of_wins="+str(number_of_wins)+", number_of_trophies="+str(number_of_trophies)+" where team_id='"+team_id+"' and player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteCaptain(self):
        team_id = ""
        player_id = ""
        team_id = self.lineEditadminaddcaptainid.text()
        player_id = self.lineEditadminaddcaptainplayerid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from captain where team_id='"+team_id+"' and player_id='"+player_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def addStadium(self):
        stadium_id = ""
        stadium_name = ""
        pitch_type = ""
        scapacity = ""
        matches_in_std = ""

        stadium_id = self.lineEditadminaddstadiumid.text()
        stadium_name = self.lineEditadminaddstadiumname.text()
        pitch_type = self.lineEditadminaddstadiumpitch.text()
        scapacity = self.lineEditadminaddstadiumcapacity.text()
        matches_in_std = self.lineEditadminaddstadiummatches.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "INSERT INTO stadium VALUES (?, ?, ?, ?, ?)", (stadium_id, stadium_name, pitch_type, scapacity, matches_in_std))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Successfully Added")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Cannot Add!")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def updateStadium(self):
        stadium_id = ""
        stadium_name = ""
        pitch_type = ""
        scapacity = ""
        matches_in_std = ""

        stadium_id = self.lineEditadminaddstadiumid.text()
        stadium_name = self.lineEditadminaddstadiumname.text()
        pitch_type = self.lineEditadminaddstadiumpitch.text()
        scapacity = self.lineEditadminaddstadiumcapacity.text()
        matches_in_std = self.lineEditadminaddstadiummatches.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "update stadium set stadium_name='"+stadium_name+"', pitch_type='"+pitch_type+"', scapacity="+str(scapacity)+", matches_in_std="+str(matches_in_std)+" where stadium_id='"+stadium_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Update Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()

    def deleteStadium(self):
        stadium_id = ""
        stadium_id = self.lineEditadminaddstadiumid.text()

        try:
            self.conn = sqlite3.connect("worldcup.db")
            self.c = self.conn.cursor()
            self.c.execute(
                "delete from stadium where stadium_id='"+stadium_id+"'")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Successful")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle("Message Display")
            msg.setText("Delete Unsuccessful")
            msg.setIcon(QMessageBox.Warning)

            x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())

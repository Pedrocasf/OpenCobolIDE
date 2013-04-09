# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_preferences.ui'
#
# Created: Tue Apr  9 12:29:15 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 670)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/Preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lwMenu = QtGui.QListWidget(Dialog)
        self.lwMenu.setMaximumSize(QtCore.QSize(72, 16777215))
        self.lwMenu.setIconSize(QtCore.QSize(64, 64))
        self.lwMenu.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.lwMenu.setViewMode(QtGui.QListView.IconMode)
        self.lwMenu.setObjectName("lwMenu")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/Preferences-system-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.lwMenu)
        item.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ide-icons/rc/Mypaint-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item = QtGui.QListWidgetItem(self.lwMenu)
        item.setIcon(icon2)
        self.gridLayout.addWidget(self.lwMenu, 0, 0, 1, 1)
        self.swMain = QtGui.QStackedWidget(Dialog)
        self.swMain.setObjectName("swMain")
        self.pGeneral = QtGui.QWidget()
        self.pGeneral.setObjectName("pGeneral")
        self.formLayout = QtGui.QFormLayout(self.pGeneral)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.cbCodeCompletion = QtGui.QCheckBox(self.pGeneral)
        self.cbCodeCompletion.setChecked(True)
        self.cbCodeCompletion.setObjectName("cbCodeCompletion")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.cbCodeCompletion)
        self.cbUseExtShell = QtGui.QCheckBox(self.pGeneral)
        self.cbUseExtShell.setObjectName("cbUseExtShell")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.cbUseExtShell)
        self.lblExternalTerminal = QtGui.QLabel(self.pGeneral)
        self.lblExternalTerminal.setObjectName("lblExternalTerminal")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblExternalTerminal)
        self.leTerminal = QtGui.QLineEdit(self.pGeneral)
        self.leTerminal.setObjectName("leTerminal")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.leTerminal)
        self.swMain.addWidget(self.pGeneral)
        self.pStyle = QtGui.QWidget()
        self.pStyle.setObjectName("pStyle")
        self.gridLayout_2 = QtGui.QGridLayout(self.pStyle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblFont = QtGui.QLabel(self.pStyle)
        self.lblFont.setObjectName("lblFont")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFont)
        self.lblFontSize = QtGui.QLabel(self.pStyle)
        self.lblFontSize.setObjectName("lblFontSize")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblFontSize)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sbFontSize = QtGui.QSpinBox(self.pStyle)
        self.sbFontSize.setMinimumSize(QtCore.QSize(50, 0))
        self.sbFontSize.setMinimum(1)
        self.sbFontSize.setProperty("value", 10)
        self.sbFontSize.setObjectName("sbFontSize")
        self.horizontalLayout_3.addWidget(self.sbFontSize)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.lblPygmentStyle = QtGui.QLabel(self.pStyle)
        self.lblPygmentStyle.setObjectName("lblPygmentStyle")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblPygmentStyle)
        self.lwColors = QtGui.QListWidget(self.pStyle)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lwColors.sizePolicy().hasHeightForWidth())
        self.lwColors.setSizePolicy(sizePolicy)
        self.lwColors.setMaximumSize(QtCore.QSize(129, 16777215))
        self.lwColors.setObjectName("lwColors")
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        QtGui.QListWidgetItem(self.lwColors)
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.lwColors)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbColor = QtGui.QPushButton(self.pStyle)
        self.pbColor.setMinimumSize(QtCore.QSize(50, 0))
        self.pbColor.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pbColor.setText("")
        self.pbColor.setAutoDefault(True)
        self.pbColor.setFlat(False)
        self.pbColor.setObjectName("pbColor")
        self.horizontalLayout_2.addWidget(self.pbColor)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fcbFont = QtGui.QFontComboBox(self.pStyle)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbFont.sizePolicy().hasHeightForWidth())
        self.fcbFont.setSizePolicy(sizePolicy)
        self.fcbFont.setMinimumSize(QtCore.QSize(200, 0))
        self.fcbFont.setFontFilters(QtGui.QFontComboBox.MonospacedFonts)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(6)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.fcbFont.setCurrentFont(font)
        self.fcbFont.setObjectName("fcbFont")
        self.horizontalLayout.addWidget(self.fcbFont)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmbPygmentsStyle = QtGui.QComboBox(self.pStyle)
        self.cmbPygmentsStyle.setMinimumSize(QtCore.QSize(200, 0))
        self.cmbPygmentsStyle.setObjectName("cmbPygmentsStyle")
        self.horizontalLayout_4.addWidget(self.cmbPygmentsStyle)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.cbLineNbr = QtGui.QCheckBox(self.pStyle)
        self.cbLineNbr.setChecked(True)
        self.cbLineNbr.setObjectName("cbLineNbr")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.cbLineNbr)
        self.cbWhitespaces = QtGui.QCheckBox(self.pStyle)
        self.cbWhitespaces.setChecked(False)
        self.cbWhitespaces.setObjectName("cbWhitespaces")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.cbWhitespaces)
        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.plainTextEdit = CobolEditor(self.pStyle)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        self.swMain.addWidget(self.pStyle)
        self.gridLayout.addWidget(self.swMain, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.swMain.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.lwMenu.isSortingEnabled()
        self.lwMenu.setSortingEnabled(False)
        self.lwMenu.item(0).setText(QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.lwMenu.item(1).setText(QtGui.QApplication.translate("Dialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.lwMenu.setSortingEnabled(__sortingEnabled)
        self.cbCodeCompletion.setText(QtGui.QApplication.translate("Dialog", "Code completion", None, QtGui.QApplication.UnicodeUTF8))
        self.cbUseExtShell.setText(QtGui.QApplication.translate("Dialog", "Run program in external terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.lblExternalTerminal.setText(QtGui.QApplication.translate("Dialog", "External terminal command:", None, QtGui.QApplication.UnicodeUTF8))
        self.leTerminal.setText(QtGui.QApplication.translate("Dialog", "gnome-terminal -e", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFont.setText(QtGui.QApplication.translate("Dialog", "Font: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFontSize.setText(QtGui.QApplication.translate("Dialog", "Font size: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPygmentStyle.setText(QtGui.QApplication.translate("Dialog", "Pygments style: ", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.lwColors.isSortingEnabled()
        self.lwColors.setSortingEnabled(False)
        self.lwColors.item(0).setText(QtGui.QApplication.translate("Dialog", "Margin", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(1).setText(QtGui.QApplication.translate("Dialog", "ActiveLine", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(2).setText(QtGui.QApplication.translate("Dialog", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(3).setText(QtGui.QApplication.translate("Dialog", "SelectedText", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(4).setText(QtGui.QApplication.translate("Dialog", "LineNumber", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(5).setText(QtGui.QApplication.translate("Dialog", "PanelBackground", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(6).setText(QtGui.QApplication.translate("Dialog", "PanelBackground2", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(7).setText(QtGui.QApplication.translate("Dialog", "TextOccurences", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(8).setText(QtGui.QApplication.translate("Dialog", "SearchResults", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(9).setText(QtGui.QApplication.translate("Dialog", "Warning", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.item(10).setText(QtGui.QApplication.translate("Dialog", "Error", None, QtGui.QApplication.UnicodeUTF8))
        self.lwColors.setSortingEnabled(__sortingEnabled)
        self.cbLineNbr.setText(QtGui.QApplication.translate("Dialog", "Show line numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.cbWhitespaces.setText(QtGui.QApplication.translate("Dialog", "Show whitespaces", None, QtGui.QApplication.UnicodeUTF8))

from cobcide.editor import CobolEditor
import ide_rc

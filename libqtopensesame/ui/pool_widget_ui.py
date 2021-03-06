# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/pool_widget.ui'
#
# Created: Sat Mar 31 16:00:40 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(355, 291)
        Form.setAcceptDrops(True)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setStyleSheet(_fromUtf8("background-color: #729fcf;\n"
"color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_pool = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pool.sizePolicy().hasHeightForWidth())
        self.label_pool.setSizePolicy(sizePolicy)
        self.label_pool.setText(_fromUtf8(""))
        self.label_pool.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pool_large.png")))
        self.label_pool.setObjectName(_fromUtf8("label_pool"))
        self.horizontalLayout.addWidget(self.label_pool)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_pool = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_pool.sizePolicy().hasHeightForWidth())
        self.widget_pool.setSizePolicy(sizePolicy)
        self.widget_pool.setObjectName(_fromUtf8("widget_pool"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_pool)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_pool_search = QtGui.QLabel(self.widget_pool)
        self.label_pool_search.setText(_fromUtf8(""))
        self.label_pool_search.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/variable_inspector.png")))
        self.label_pool_search.setObjectName(_fromUtf8("label_pool_search"))
        self.horizontalLayout_3.addWidget(self.label_pool_search)
        self.edit_pool_filter = QtGui.QLineEdit(self.widget_pool)
        self.edit_pool_filter.setObjectName(_fromUtf8("edit_pool_filter"))
        self.horizontalLayout_3.addWidget(self.edit_pool_filter)
        self.button_pool_filter_clear = QtGui.QPushButton(self.widget_pool)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pool_filter_clear.sizePolicy().hasHeightForWidth())
        self.button_pool_filter_clear.setSizePolicy(sizePolicy)
        self.button_pool_filter_clear.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pool_filter_clear.setIcon(icon)
        self.button_pool_filter_clear.setIconSize(QtCore.QSize(16, 16))
        self.button_pool_filter_clear.setObjectName(_fromUtf8("button_pool_filter_clear"))
        self.horizontalLayout_3.addWidget(self.button_pool_filter_clear)
        self.button_help_pool = QtGui.QPushButton(self.widget_pool)
        self.button_help_pool.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_help_pool.setIcon(icon1)
        self.button_help_pool.setIconSize(QtCore.QSize(16, 16))
        self.button_help_pool.setObjectName(_fromUtf8("button_help_pool"))
        self.horizontalLayout_3.addWidget(self.button_help_pool)
        self.verticalLayout.addWidget(self.widget_pool)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_pool_add = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pool_add.sizePolicy().hasHeightForWidth())
        self.button_pool_add.setSizePolicy(sizePolicy)
        self.button_pool_add.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pool_add.setIcon(icon2)
        self.button_pool_add.setIconSize(QtCore.QSize(16, 16))
        self.button_pool_add.setObjectName(_fromUtf8("button_pool_add"))
        self.horizontalLayout_2.addWidget(self.button_pool_add)
        self.button_refresh = QtGui.QPushButton(self.widget_2)
        self.button_refresh.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_refresh.setIcon(icon3)
        self.button_refresh.setIconSize(QtCore.QSize(16, 16))
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.horizontalLayout_2.addWidget(self.button_refresh)
        self.button_browse_pool = QtGui.QPushButton(self.widget_2)
        self.button_browse_pool.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/browse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_pool.setIcon(icon4)
        self.button_browse_pool.setIconSize(QtCore.QSize(16, 16))
        self.button_browse_pool.setObjectName(_fromUtf8("button_browse_pool"))
        self.horizontalLayout_2.addWidget(self.button_browse_pool)
        self.combobox_view = QtGui.QComboBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_view.sizePolicy().hasHeightForWidth())
        self.combobox_view.setSizePolicy(sizePolicy)
        self.combobox_view.setObjectName(_fromUtf8("combobox_view"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/variable_inspector.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combobox_view.addItem(icon5, _fromUtf8(""))
        self.combobox_view.addItem(icon5, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.combobox_view)
        self.verticalLayout.addWidget(self.widget_2)
        self.list_pool = QtGui.QListWidget(Form)
        self.list_pool.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.list_pool.setAcceptDrops(True)
        self.list_pool.setAlternatingRowColors(True)
        self.list_pool.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.list_pool.setViewMode(QtGui.QListView.ListMode)
        self.list_pool.setUniformItemSizes(True)
        self.list_pool.setWordWrap(True)
        self.list_pool.setSelectionRectVisible(True)
        self.list_pool.setObjectName(_fromUtf8("list_pool"))
        self.verticalLayout.addWidget(self.list_pool)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.button_pool_filter_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.edit_pool_filter.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">File pool</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">You can drag and drop files into the pool</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_pool_filter.setToolTip(QtGui.QApplication.translate("Form", "Enter a filter", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pool_filter_clear.setToolTip(QtGui.QApplication.translate("Form", "Clear filter", None, QtGui.QApplication.UnicodeUTF8))
        self.button_help_pool.setToolTip(QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.button_pool_add.setToolTip(QtGui.QApplication.translate("Form", "Add file", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse_pool.setToolTip(QtGui.QApplication.translate("Form", "Open file pool in file manager", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_view.setItemText(0, QtGui.QApplication.translate("Form", "View as list", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_view.setItemText(1, QtGui.QApplication.translate("Form", "View as icons", None, QtGui.QApplication.UnicodeUTF8))
        self.list_pool.setSortingEnabled(True)


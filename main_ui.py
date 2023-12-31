# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 460)
        Form.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.view = QVideoWidget(Form)
        self.view.setAutoFillBackground(True)
        self.view.setObjectName("view")
        self.verticalLayout_2.addWidget(self.view)
        self.bar = QtWidgets.QSlider(Form)
        self.bar.setOrientation(QtCore.Qt.Horizontal)
        self.bar.setObjectName("bar")
        self.verticalLayout_2.addWidget(self.bar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.state = QtWidgets.QLabel(Form)
        self.state.setObjectName("state")
        self.horizontalLayout_2.addWidget(self.state)
        self.playtime = QtWidgets.QLabel(Form)
        self.playtime.setObjectName("playtime")
        self.horizontalLayout_2.addWidget(self.playtime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_stop = QtWidgets.QPushButton(Form)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_play = QtWidgets.QPushButton(Form)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_forward = QtWidgets.QPushButton(Form)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        self.btn_pause = QtWidgets.QPushButton(Form)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout.addWidget(self.btn_pause)
        self.btn_prev = QtWidgets.QPushButton(Form)
        self.btn_prev.setObjectName("btn_prev")
        self.horizontalLayout.addWidget(self.btn_prev)
        self.vol = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol.sizePolicy().hasHeightForWidth())
        self.vol.setSizePolicy(sizePolicy)
        self.vol.setMinimumSize(QtCore.QSize(0, 0))
        self.vol.setOrientation(QtCore.Qt.Horizontal)
        self.vol.setObjectName("vol")
        self.horizontalLayout.addWidget(self.vol)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 90)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(3, 5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list = QtWidgets.QListWidget(Form)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setObjectName("btn_del")
        self.verticalLayout.addWidget(self.btn_del)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "VideoPlayer / Ocean Coding School"))
        self.state.setText(_translate("Form", "Media Status"))
        self.playtime.setText(_translate("Form", "Running time"))
        self.btn_stop.setText(_translate("Form", "■"))
        self.btn_play.setText(_translate("Form", "▶"))
        self.btn_forward.setText(_translate("Form", "▶▶"))
        self.btn_pause.setText(_translate("Form", "❚❚"))
        self.btn_prev.setText(_translate("Form", "◀◀"))
        self.label.setText(_translate("Form", "Play List"))
        self.btn_add.setText(_translate("Form", "Add"))
        self.btn_del.setText(_translate("Form", "Del"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

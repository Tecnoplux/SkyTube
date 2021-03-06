# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created: Sat Jan 10 22:54:02 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(880, 480)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.btn_valida = QtWidgets.QPushButton(Form)
        self.btn_valida.setGeometry(QtCore.QRect(487, 20, 41, 24))
        self.btn_valida.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_valida.setIcon(icon1)
        self.btn_valida.setFlat(True)
        self.btn_valida.setObjectName("btn_valida")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 461, 20))
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 43, 361, 21))
        self.label_7.setAutoFillBackground(True)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.lbl_desc = QtWidgets.QLabel(Form)
        self.lbl_desc.setGeometry(QtCore.QRect(40, 20, 441, 20))
        self.lbl_desc.setAutoFillBackground(True)
        self.lbl_desc.setObjectName("lbl_desc")
        self.btn_folder = QtWidgets.QPushButton(Form)
        self.btn_folder.setGeometry(QtCore.QRect(536, 44, 41, 24))
        self.btn_folder.setAutoFillBackground(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_folder.setIcon(icon2)
        self.btn_folder.setFlat(True)
        self.btn_folder.setObjectName("btn_folder")
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setGeometry(QtCore.QRect(593, 40, 281, 371))
        self.treeView.setAutoFillBackground(True)
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName("treeView")
        self.lbl_perfil = QtWidgets.QLabel(Form)
        self.lbl_perfil.setGeometry(QtCore.QRect(597, 5, 231, 16))
        self.lbl_perfil.setAutoFillBackground(True)
        self.lbl_perfil.setObjectName("lbl_perfil")
        self.btn_folder_2 = QtWidgets.QPushButton(Form)
        self.btn_folder_2.setGeometry(QtCore.QRect(823, 4, 51, 24))
        self.btn_folder_2.setAutoFillBackground(True)
        self.btn_folder_2.setIcon(icon2)
        self.btn_folder_2.setFlat(True)
        self.btn_folder_2.setObjectName("btn_folder_2")
        self.lst_encola = QtWidgets.QListWidget(Form)
        self.lst_encola.setGeometry(QtCore.QRect(590, 40, 281, 371))
        self.lst_encola.setAutoFillBackground(True)
        self.lst_encola.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lst_encola.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.lst_encola.setAlternatingRowColors(True)
        self.lst_encola.setObjectName("lst_encola")
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(536, 20, 41, 24))
        self.btn_add.setAutoFillBackground(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon3)
        self.btn_add.setFlat(True)
        self.btn_add.setObjectName("btn_add")
        self.ck_captura = QtWidgets.QCheckBox(Form)
        self.ck_captura.setGeometry(QtCore.QRect(440, 83, 140, 20))
        self.ck_captura.setAutoFillBackground(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagenes/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_captura.setIcon(icon4)
        self.ck_captura.setObjectName("ck_captura")
        self.ck_lst_auto = QtWidgets.QCheckBox(Form)
        self.ck_lst_auto.setGeometry(QtCore.QRect(440, 63, 137, 20))
        self.ck_lst_auto.setAutoFillBackground(True)
        self.ck_lst_auto.setIcon(icon3)
        self.ck_lst_auto.setObjectName("ck_lst_auto")
        self.btn_add_video = QtWidgets.QPushButton(Form)
        self.btn_add_video.setGeometry(QtCore.QRect(595, 430, 118, 27))
        self.btn_add_video.setAutoFillBackground(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imagenes/add_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_video.setIcon(icon5)
        self.btn_add_video.setFlat(True)
        self.btn_add_video.setObjectName("btn_add_video")
        self.btn_add_lista = QtWidgets.QPushButton(Form)
        self.btn_add_lista.setGeometry(QtCore.QRect(730, 430, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add_lista.setFont(font)
        self.btn_add_lista.setAutoFillBackground(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imagenes/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_lista.setIcon(icon6)
        self.btn_add_lista.setFlat(True)
        self.btn_add_lista.setObjectName("btn_add_lista")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 411, 31))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(16, 7, 61, 16))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.f_box = QtWidgets.QComboBox(self.groupBox_2)
        self.f_box.setGeometry(QtCore.QRect(72, 5, 71, 22))
        self.f_box.setAutoFillBackground(True)
        self.f_box.setObjectName("f_box")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("imagenes/mp4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("imagenes/mp3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("imagenes/3gp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("imagenes/webm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("imagenes/flv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon11, "")
        self.ck_play = QtWidgets.QCheckBox(self.groupBox_2)
        self.ck_play.setGeometry(QtCore.QRect(282, 5, 91, 20))
        self.ck_play.setAutoFillBackground(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("imagenes/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_play.setIcon(icon12)
        self.ck_play.setObjectName("ck_play")
        self.btn_ayuda = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ayuda.setGeometry(QtCore.QRect(376, 6, 31, 21))
        self.btn_ayuda.setAutoFillBackground(True)
        self.btn_ayuda.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("imagenes/ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ayuda.setIcon(icon13)
        self.btn_ayuda.setIconSize(QtCore.QSize(24, 24))
        self.btn_ayuda.setFlat(True)
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.btn_actualiza = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_actualiza.setGeometry(QtCore.QRect(150, 4, 121, 21))
        self.btn_actualiza.setAutoFillBackground(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("imagenes/actualiza.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualiza.setIcon(icon14)
        self.btn_actualiza.setIconSize(QtCore.QSize(80, 20))
        self.btn_actualiza.setFlat(True)
        self.btn_actualiza.setObjectName("btn_actualiza")
        self.btn_de_item = QtWidgets.QPushButton(Form)
        self.btn_de_item.setGeometry(QtCore.QRect(740, 11, 124, 21))
        self.btn_de_item.setAutoFillBackground(True)
        self.btn_de_item.setIcon(icon6)
        self.btn_de_item.setFlat(True)
        self.btn_de_item.setObjectName("btn_de_item")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(575, 14, 20, 451))
        self.line_2.setAutoFillBackground(True)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_facebook = QtWidgets.QPushButton(Form)
        self.btn_facebook.setGeometry(QtCore.QRect(80, 450, 38, 27))
        self.btn_facebook.setAutoFillBackground(True)
        self.btn_facebook.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("imagenes/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_facebook.setIcon(icon15)
        self.btn_facebook.setIconSize(QtCore.QSize(16, 16))
        self.btn_facebook.setFlat(True)
        self.btn_facebook.setObjectName("btn_facebook")
        self.btn_google = QtWidgets.QPushButton(Form)
        self.btn_google.setGeometry(QtCore.QRect(42, 449, 38, 27))
        self.btn_google.setAutoFillBackground(True)
        self.btn_google.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("imagenes/googleplus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_google.setIcon(icon16)
        self.btn_google.setIconSize(QtCore.QSize(16, 16))
        self.btn_google.setFlat(True)
        self.btn_google.setObjectName("btn_google")
        self.btn_twitter = QtWidgets.QPushButton(Form)
        self.btn_twitter.setGeometry(QtCore.QRect(4, 449, 38, 27))
        self.btn_twitter.setAutoFillBackground(True)
        self.btn_twitter.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("imagenes/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_twitter.setIcon(icon17)
        self.btn_twitter.setIconSize(QtCore.QSize(16, 16))
        self.btn_twitter.setFlat(True)
        self.btn_twitter.setObjectName("btn_twitter")
        self.ck_vlc = QtWidgets.QCheckBox(Form)
        self.ck_vlc.setGeometry(QtCore.QRect(440, 100, 58, 20))
        self.ck_vlc.setAutoFillBackground(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("imagenes/vlc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_vlc.setIcon(icon18)
        self.ck_vlc.setIconSize(QtCore.QSize(16, 16))
        self.ck_vlc.setObjectName("ck_vlc")
        self.lbl_barr = QtWidgets.QLabel(Form)
        self.lbl_barr.setGeometry(QtCore.QRect(70, 60, 351, 20))
        self.lbl_barr.setAutoFillBackground(True)
        self.lbl_barr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_barr.setObjectName("lbl_barr")
        self.p_bar = QtWidgets.QProgressBar(Form)
        self.p_bar.setGeometry(QtCore.QRect(40, 40, 451, 23))
        self.p_bar.setProperty("value", 0)
        self.p_bar.setObjectName("p_bar")
        self.web = QtWebKitWidgets.QWebView(Form)
        self.web.setGeometry(QtCore.QRect(9, 124, 571, 281))
        self.web.setAutoFillBackground(True)
        self.web.setObjectName("web")
        self.lbl_autor = QtWidgets.QLabel(Form)
        self.lbl_autor.setGeometry(QtCore.QRect(64, 411, 411, 16))
        self.lbl_autor.setAutoFillBackground(True)
        self.lbl_autor.setObjectName("lbl_autor")
        self.btn_valida_2 = QtWidgets.QPushButton(Form)
        self.btn_valida_2.setGeometry(QtCore.QRect(470, 406, 101, 27))
        self.btn_valida_2.setAutoFillBackground(True)
        self.btn_valida_2.setIcon(icon6)
        self.btn_valida_2.setFlat(True)
        self.btn_valida_2.setObjectName("btn_valida_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(14, 410, 40, 16))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.btn_paypal = QtWidgets.QPushButton(Form)
        self.btn_paypal.setGeometry(QtCore.QRect(470, 444, 51, 31))
        self.btn_paypal.setAutoFillBackground(True)
        self.btn_paypal.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("imagenes/paypal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_paypal.setIcon(icon19)
        self.btn_paypal.setIconSize(QtCore.QSize(100, 30))
        self.btn_paypal.setFlat(True)
        self.btn_paypal.setObjectName("btn_paypal")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(179, 451, 291, 20))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(600, 430, 271, 31))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn_play = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_play.setGeometry(QtCore.QRect(2, 4, 31, 21))
        self.btn_play.setAutoFillBackground(True)
        self.btn_play.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("imagenes/reproduce.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon20)
        self.btn_play.setIconSize(QtCore.QSize(20, 20))
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.lbl_autor_2 = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_autor_2.setGeometry(QtCore.QRect(39, 6, 231, 20))
        self.lbl_autor_2.setAutoFillBackground(True)
        self.lbl_autor_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor_2.setObjectName("lbl_autor_2")
        self.lbl_autor_3 = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_autor_3.setGeometry(QtCore.QRect(20, 30, 241, 20))
        self.lbl_autor_3.setAutoFillBackground(True)
        self.lbl_autor_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor_3.setObjectName("lbl_autor_3")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-1, 85, 35, 35))
        self.label_8.setBaseSize(QtCore.QSize(45, 45))
        self.label_8.setAutoFillBackground(True)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("imagenes/python-3.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_valida.setToolTip(_translate("Form", "Buscar Video"))
        self.btn_valida.setText(_translate("Form", "..."))
        self.label_7.setText(_translate("Form", "Ejemplo: http://www.youtube.com/watch?v=QJO3ROT-A4E "))
        self.lbl_desc.setToolTip(_translate("Form", "Introduce la URL de Youtube"))
        self.lbl_desc.setText(_translate("Form", "TextLabel"))
        self.btn_folder.setToolTip(_translate("Form", "Motrar Videos"))
        self.btn_folder.setText(_translate("Form", ">"))
        self.treeView.setToolTip(_translate("Form", "Directorio Videos"))
        self.lbl_perfil.setText(_translate("Form", "TextLabel"))
        self.btn_folder_2.setToolTip(_translate("Form", "<html><head/><body><p>Abrir Carpeta de Videos</p></body></html>"))
        self.btn_folder_2.setText(_translate("Form", "..."))
        self.lst_encola.setToolTip(_translate("Form", "Lista de Descarga"))
        self.btn_add.setToolTip(_translate("Form", "Mostrar Lista"))
        self.btn_add.setText(_translate("Form", ">"))
        self.ck_captura.setToolTip(_translate("Form", "Capturar Enlaces de Youtube en Automatico"))
        self.ck_captura.setText(_translate("Form", "Capturar Enlaces"))
        self.ck_lst_auto.setToolTip(_translate("Form", "Lista Automatica"))
        self.ck_lst_auto.setText(_translate("Form", "Lista Automatica"))
        self.btn_add_video.setToolTip(_translate("Form", "Añadir Link a la Lista de Descargas"))
        self.btn_add_video.setText(_translate("Form", "Añadir Video"))
        self.btn_add_lista.setToolTip(_translate("Form", "Descargar Lista de videos"))
        self.btn_add_lista.setText(_translate("Form", "Descargar Lista"))
        self.label.setText(_translate("Form", "Formato:"))
        self.f_box.setToolTip(_translate("Form", "Formato"))
        self.f_box.setItemText(0, _translate("Form", "mp4"))
        self.f_box.setItemText(1, _translate("Form", "mp3"))
        self.f_box.setItemText(2, _translate("Form", "3gp"))
        self.f_box.setItemText(3, _translate("Form", "webm"))
        self.f_box.setItemText(4, _translate("Form", "flv"))
        self.ck_play.setToolTip(_translate("Form", "AutoReproduccion de Videos Youtube y Videos Locales"))
        self.ck_play.setText(_translate("Form", "AutoPlay"))
        self.btn_ayuda.setToolTip(_translate("Form", "Como Usar SkyTube! Ayuda en Linea!"))
        self.btn_actualiza.setToolTip(_translate("Form", "Actualiza Version"))
        self.btn_actualiza.setText(_translate("Form", "Actualiza v.0.0."))
        self.btn_de_item.setToolTip(_translate("Form", "Eliminar Link"))
        self.btn_de_item.setText(_translate("Form", "Eliminar Link"))
        self.btn_facebook.setToolTip(_translate("Form", "Sigueme en Facebook"))
        self.btn_google.setToolTip(_translate("Form", "Sigueme en G+"))
        self.btn_twitter.setToolTip(_translate("Form", "Sigueme en Twitter"))
        self.ck_vlc.setToolTip(_translate("Form", "Reproducir Videos en VLC"))
        self.ck_vlc.setText(_translate("Form", "vlc"))
        self.lbl_barr.setText(_translate("Form", "-----"))
        self.lbl_autor.setText(_translate("Form", "Autor:"))
        self.btn_valida_2.setToolTip(_translate("Form", "Descarga el Video"))
        self.btn_valida_2.setText(_translate("Form", "Descargar"))
        self.label_2.setText(_translate("Form", "Autor:"))
        self.btn_paypal.setToolTip(_translate("Form", "Donar en PayPal"))
        self.label_3.setText(_translate("Form", "Por Favor Considera una Donacion al Proyecto -->"))
        self.btn_play.setToolTip(_translate("Form", "Roproducir Multimedia"))
        self.lbl_autor_2.setText(_translate("Form", "Reproducir en  -  SkyTube Play d(-_-)b"))
        self.lbl_autor_3.setText(_translate("Form", "Reproducir en  -  SkyTube Play d(-_-)b"))
        self.label_8.setToolTip(_translate("Form", "<html><head/><body><p>Programado en Python! y PyQt4 ..  xskyofx@gmail.com</p></body></html>"))

from PyQt5 import QtWebKitWidgets

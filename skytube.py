__author__ = 'xskylarx'
 #!/usr/bi/python3
# -*- coding: utf8 -*-
# Python 3.4.2  + PyQt5 By Skylar
#
# Creado: 29 - sep - 2013
# Ultima modificacion: 11 - Enero - 2015
#      Por: xskylarx
# xskyofx@gmail.com
#Version 3.0
# se Migra Codigo fuente a PyQt5, se agrega reproductor nativo en html5 para youtube videos de vevo y para videos locales,
# se agrega funcion para actualizar software de forma semiautomatica, funcion de mensaje proporcionada por Juan Carlos Paco, Comunidad python espanol
#
# Version 2.0-  se añade compatibilidad con listas de reproduccion, se pueden escoger que videos descargar de
#       dicha lista, se añade reproductor nativo en la aplicacion para ver el video en vez de una imagen previa
#       se actualiza plugin para descargar videos de VEVO
#v1.5 se corrige fallo, el cual no permitia descargar de vevo, se añade formato mp3, se cambia interface y se añade
#       combo en vez de opciones individuales al escoger el formato a descargar.
#v1.4 se añade compatibilidad con linux, mac, windows, se agrega funcion para abrir reproductor predeterminado, o vlc
#v1.3 se añade lista automatica, capturador de enlaces, lista de descarga
#V1.2 ->
# Se agrega Directorio de videos, con la cual se puede dar doble clic y abrir el video en VLC.
#
# Por favor si modificas algo haz referencia al autor.

import pafy
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKit
from inicio import Ui_Form
import urllib.request
import os
import sys
import webbrowser
import time
import subprocess

__source__ = ('http://expocoin.com/software/skytube/version.txt')
__version__ = ('3.0')
__ayuda__ = ('http://expocoin.com/software/skytube/link/link_ayuda.txt')
__youtube__ = ('https://www.youtube.com')
__instalador__ = ('http://expocoin.com/software/skytube/SkyTube_install.txt')

class v_skytube(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.vskytube = Ui_Form()
        self.vskytube.setupUi(self)
        self.resize(585, 480)
        self.vskytube.label_7.setStyleSheet("color:grey;")
        self.setWindowTitle('SkyTube Download v.' + __version__)
        self.setMaximumSize(880, 480)
        self.setMinimumSize(489, 48)

        self.vskytube.btn_valida_2.clicked.connect(self.descarga)
        self.vskytube.btn_valida.clicked.connect(self.valida)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.ck_lst_auto.setEnabled(False)
        self.vskytube.btn_folder.clicked.connect(self.crea_directorio)
        self.vskytube.treeView.doubleClicked.connect(self.directorio)
        self.vskytube.treeView.clicked.connect(self.directorio2)
        self.vskytube.lineEdit.returnPressed.connect(self.valida)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        #self.setStyleSheet("background-image: url('imagenes/skylogo.png');")
        self.vskytube.btn_folder_2.clicked.connect(self.folder)

        self.vskytube.btn_add_video.clicked.connect(self.add)
        self.vskytube.btn_add.clicked.connect(self.crea_lista)
        self.vskytube.btn_paypal.clicked.connect(self.donapaypal)
        self.vskytube.ck_captura.stateChanged['int'].connect(self.CapturaClip)
        self.vskytube.ck_vlc.stateChanged['int'].connect(self.vlc_checked)
        self.vskytube.lst_encola.itemClicked['QListWidgetItem*'].connect(self.valida_lista)
        self.vskytube.lst_encola.itemDoubleClicked['QListWidgetItem*'].connect(self.elimina_item)
        self.vskytube.btn_de_item.clicked.connect(self.elimina_item)
        self.vskytube.btn_add_lista.clicked.connect(self.valida_descarga)
        self.vskytube.btn_google.clicked.connect(self.social_google)
        self.vskytube.btn_twitter.clicked.connect(self.social_twitter)
        self.vskytube.btn_facebook.clicked.connect(self.social_facebook)
        self.vskytube.btn_play.clicked.connect(self.btn_play)
        self.vskytube.web.showFullScreen()
        self.vskytube.ck_play.setChecked(True)
        self.vskytube.ck_play.clicked.connect(self.cambia_icono_play)
        self.vskytube.groupBox_3.setVisible(False)
        self.check_for_updates()
        self.vskytube.btn_actualiza.clicked.connect(self.actualiza_version)
        self.vskytube.btn_ayuda.clicked.connect(self.ayuda)

        self.vskytube.web.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
        self.vskytube.web.settings().setAttribute(QtWebKit.QWebSettings.JavascriptEnabled, True)
        self.vskytube.web.settings().setAttribute(QtWebKit.QWebSettings.JavascriptCanOpenWindows, True)
        self.vskytube.web.setUrl(QtCore.QUrl("http://expocoin.com/software/skytube/"))
        self.vskytube.lineEdit.setPlaceholderText('    Escribe o pega la direccion de tu video y da enter ..')
        self.oculta()
        self.vskytube.p_bar.setMinimum(0)
        self.process = QtCore.QProcess()
        self.setclipboard()
        self.vlc()

    def ayuda(self):
        link_ayuda = str(urllib.request.urlopen(__ayuda__).read().decode("utf8"))
        webbrowser.open(link_ayuda)


    def actualiza_version(self):
        self.vskytube.lineEdit.setVisible(False)
        self.vskytube.btn_valida.setVisible(False)
        self.vskytube.label_7.setVisible(False)
        self.vskytube.btn_folder.setVisible(False)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.btn_folder_2.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)

        self.vskytube.groupBox_2.setVisible(False)
        self.vskytube.btn_add.setVisible(False)
        self.vskytube.ck_lst_auto.setVisible(False)
        self.vskytube.ck_captura.setVisible(False)

        self.vskytube.lbl_barr.setVisible(True)
        self.vskytube.p_bar.setVisible(True)
        self.resize(489, 82)

        self.vskytube.lbl_desc.setStyleSheet("color:red;")
        self.vskytube.lbl_desc.setText('Descargando Nueva Version de SkyTube  ... ')
        self.vskytube.lbl_desc.setVisible(True)
        self.vskytube.p_bar.setMinimum(0)
        skytube_install = str(urllib.request.urlopen(__instalador__).read().decode("utf8"))
        file = skytube_install.split('/')

        if 'win32' in self.sistema() or 'win64' in self.sistema():
            desc = skytube_install + '.exe'
            filename = file[5] + '.exe'

        urllib.request.urlretrieve(desc, filename, reporthook=self.funcionprogreso)
        QtCore.QCoreApplication.processEvents()
        QtWidgets.QMessageBox.about(self,'Descargando Nueva Version   ', 'Finalizo la descarga de  ' + filename)
        self.process.start(filename)
        sys.exit(0)


    #"#### Funcion proporcionada por Luis Francisco Cesar - Enki Comunidad Python en español.
    def funcionprogreso(self,bloque, tamano_bloque, tamano_total):
        velocidad_descarga = 0
        tiempo_faltante = 0
        cant_descargada = bloque * tamano_bloque
        self.vskytube.p_bar.setMinimum(0)
        self.vskytube.p_bar.setMaximum(tamano_total)
        cant_descargada = bloque * tamano_bloque
        cant_descargada_MB = round(((cant_descargada/1024)/1024), 2)
        tamano_total_MB = round(((tamano_total/1024)/1024), 2)

        cant_descargada_KB = (cant_descargada/1024)
        tamano_total_KB = (tamano_total/1024)

        elapsed = time.clock()
        if elapsed > 0:
            velocidad_descarga = round((cant_descargada_KB/elapsed), 2)

        if velocidad_descarga > 0:
            tiempo_faltante = abs(round(((tamano_total_KB - cant_descargada_KB) / velocidad_descarga), 1))



        self.vskytube.lbl_barr.setText(str('\r %s MB / %s MB - %s kb/s - %s seg' % (cant_descargada_MB, tamano_total_MB, velocidad_descarga, tiempo_faltante)))
        self.vskytube.lbl_barr.repaint()
        self.vskytube.p_bar.setValue(cant_descargada)
        QtCore.QCoreApplication.processEvents()


    def check_for_updates(self):
                """Funcion para mostrar nueva version, proporcianada por Juancalos Paco Comunidad python espanol"""
                version_local = __version__
                version_web = str(urllib.request.urlopen(__source__).read().decode("utf8"))
                if version_local != version_web:
                    m = "Hay una Nueva Version! <br> Nueva Version:  " + version_web + " Version Actual: " + version_local
                    self.vskytube.btn_actualiza.setVisible(True)
                    self.vskytube.btn_actualiza.setText('Actualiza V.' + version_web)
                else:
                    m = "Tu Version esta  Actualizada !<br>Por favor concidera una Donacion al proyecto <br> Muchas Gracias!"
                    self.vskytube.btn_actualiza.setVisible(False)
                return QtWidgets.QMessageBox.information(self, 'SkyTube Download Version ' + version_local, "<b>" + m)

    def cambia_icono_play(self):
        if self.vskytube.ck_play.isChecked():
            play_ok = QtGui.QIcon()
            play_ok.addPixmap(QtGui.QPixmap("imagenes/reproduce.png"))
            self.vskytube.btn_play.setIcon(play_ok)
        else:
            play_no = QtGui.QIcon()
            play_no.addPixmap(QtGui.QPixmap("imagenes/loading.png"))
            self.vskytube.btn_play.setIcon(play_no)

    def webVid(self, video, imagen, vevo):
        self.vskytube.groupBox_3.setVisible(False)
        if self.vskytube.ck_play.isChecked():
         autoplay = 'controls autoplay'
        else:
         autoplay = ''


        if vevo == 'ok':

            self.vskytube.web.setHtml('''
           <!DOCTYPE html>
            <html>
            <head>
              <link href="http://expocoin.com/software/skytube/video-js.css" rel="stylesheet" type="text/css">
              <script src="http://expocoin.com/software/skytube/video.js"></script>

              <script>
                videojs.options.flash.swf = "http://expocoin.com/software/skytube/video-js.swf";
              </script>
            </head>
            <body>

              <video id="example_video_1" class="video-js"  controls="controls"''' + autoplay + '''  width="551" height="251"

                  data-setup='{}'>
             <source src="''' + video + '''" type="video/mp4"></video>


            </body>
            </html>
                       ''')
        else:
            self.vskytube.web.load(QtCore.QUrl(video))
            self.vskytube.web.show()
        QtCore.QCoreApplication.processEvents()

# revisado Linux, Windows
    def formato_combo(self):


        self.vskytube.lineEdit.setVisible(False)
        self.vskytube.btn_valida.setVisible(False)
        self.vskytube.label_7.setVisible(False)
        self.vskytube.btn_folder.setVisible(False)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.btn_folder_2.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        #self.vskytube.groupBox.setVisible(False)
        self.vskytube.groupBox_2.setVisible(False)
        self.vskytube.btn_add.setVisible(False)
        self.vskytube.ck_lst_auto.setVisible(False)
        self.vskytube.ck_captura.setVisible(False)

        self.vskytube.lbl_barr.setVisible(True)
        self.vskytube.p_bar.setVisible(True)
        self.resize(489, 82)


        self.vskytube.lbl_desc.setStyleSheet("color:red;")
        self.vskytube.lbl_desc.setText('Descargando ffmpeg  ... ')
        self.vskytube.lbl_desc.setVisible(True)
        self.vskytube.p_bar.setMinimum(0)
        if 'win32' in self.sistema() or 'win64' in self.sistema():
            desc = 'https://dl.dropboxusercontent.com/s/lxkyob6uypwewrc/ffmpeg.exe?dl=1&token_hash=AAEj_dwaE9372Y7tytJC_3kl0UtVKbH924p6ZjDFmmqf9A'
            filename = 'ffmpeg.exe'
        if 'darwin' in self.sistema():
            desc = 'https://dl.dropboxusercontent.com/s/ux463io3iyybh74/ffmpeg?dl=1&token_hash=AAHE6cs1LXreRN_mspjpLA_w7oaucYFUKeqxFJXZL8rh0Q'
            filename = 'ffmpeg'

        if 'linux' in self.sistema():
            #32bits
            desc = 'https://dl.dropboxusercontent.com/s/irpst77slohbjcy/ffmpeg?dl=1&token_hash=AAH3bYjsl8k-6x0CQnEC4VVkWq-BkrQ2Qac8QfTJGHEymg'
            #64bits
            #desc = 'https://dl.dropboxusercontent.com/s/bl464mn9da3778z/ffmpeg?dl=1&token_hash=AAGYU2ttPlIXFCrokHxVGXLutuoiGDG3QraD6SzkGJy76A'

            filename = 'ffmpeg'

        QtCore.QCoreApplication.processEvents()
        #QtGui.QMessageBox.about(self,'Descarga ..', 'Comenzara la descarga de  FFMPEG ')
        urllib.request.urlretrieve(desc, filename, reporthook=self.funcionprogreso)
        QtWidgets.QMessageBox.about(self,'Descarga ..', 'Finalizo la descarga de  FFMPEG ')


# revisado Linux, Windows
    def setclipboard(self):
        global data
        data = QtWidgets.QApplication.clipboard()
        data = data.setText('skylar')

#revisado Linux, Windows
    def elimina_item(self):
        try:
            for index in range(self.vskytube.lst_encola.count()):
                if self.vskytube.lst_encola.currentItem().text() == self.vskytube.lst_encola.item(index).text():

                    respuesta = QtWidgets.QMessageBox.question(self, 'Elimina Link ', 'Estas seguro de Eliminar el Link \n'
                    + self.vskytube.lst_encola.item(index).text() + ' ?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                    if respuesta == QtWidgets.QMessageBox.Yes:
                        item = self.vskytube.lst_encola.takeItem(index)
                        del item
                        #self.vskytube.groupBox.setVisible(False)

        except:
            QtWidgets.QMessageBox.about(self, 'Error Link', 'No hay Link Que eliminar')


    def ejecutaExe(self, var_archivo):
        if 'win32' in self.sistema() or 'win64' in self.sistema():
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            with (subprocess.Popen(var_archivo, stdout=subprocess.PIPE, startupinfo=startupinfo)):
                return
        else:
            os.system('chmod +x ffmpeg')
            output = subprocess.check_output(var_archivo, shell=True)



    def ffmpeg(self):
        if 'win32' in self.sistema() or 'win64' in self.sistema():
                if self.formato() == 'mp3':
                    if os.path.isfile('ffmpeg.exe'):
                        return True
                    else:
                        respuesta = QtWidgets.QMessageBox.question(self, 'Descarga Mp3 ', 'Necesitas ffmpeg  para descargar MP3 \n'
                                                        'Quieres descargarlo? ', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                        if respuesta == QtWidgets.QMessageBox.Yes:
                            self.formato_combo()
                            return True
                        else:
                            return False
                else:
                    return True

        if 'darwin' in self.sistema():
                if self.formato() == 'mp3':
                    if os.path.isfile('ffmpeg'):
                        return True
                    else:
                        respuesta = QtWidgets.QMessageBox.question(self, 'Descarga Mp3 ', 'Necesitas ffmpeg  para descargar MP3 \n'
                                                        'Quieres descargarlo? ', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                        if respuesta == QtWidgets.QMessageBox.Yes:
                            self.formato_combo()
                            return True
                        else:
                            return False
                else:
                    return True

        if 'linux' in self.sistema():
                if self.formato() == 'mp3':
                    if os.path.isfile('ffmpeg'):
                        return True
                    else:
                        respuesta = QtWidgets.QMessageBox.question(self, 'Descarga Mp3 ', 'Necesitas ffmpeg  para descargar MP3 \n'
                                                        'Quieres descargarlo? ', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                        if respuesta == QtWidgets.QMessageBox.Yes:
                            self.formato_combo()
                            return True
                        else:
                            return False
                else:
                    return True


    def descarga_lista(self):

        self.vskytube.p_bar.setMinimum(0)

        if self.ffmpeg():
            pass
        else:
            return


        self.vskytube.ck_captura.setChecked(False)

        items = []
        for index in range(self.vskytube.lst_encola.count()):
            items.append(self.vskytube.lst_encola.item(index).text())


        url = str(items)

        self.vskytube.lineEdit.setVisible(False)
        self.vskytube.btn_valida.setVisible(False)
        self.vskytube.label_7.setVisible(False)
        self.vskytube.btn_folder.setVisible(False)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.btn_folder_2.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        #self.vskytube.groupBox.setVisible(False)
        self.vskytube.groupBox_2.setVisible(False)
        self.vskytube.btn_add.setVisible(False)
        self.vskytube.ck_lst_auto.setVisible(False)
        self.vskytube.ck_captura.setVisible(False)

        self.vskytube.lbl_barr.setVisible(True)
        self.vskytube.p_bar.setVisible(True)
        self.resize(489,82)
        QtCore.QCoreApplication.processEvents()
        QtWidgets.QMessageBox.about(self,'Comenzando Descarga','Tu lista empezara a Descargarce, esto va a tardar varios minutos.')


        for i in items:
            self.vskytube.lbl_desc.setStyleSheet("color:red;")
            self.vskytube.lbl_desc.setVisible(True)
            self.vskytube.p_bar.setMinimum(0)
            video =pafy.new(i)
            if self.formato() == 'mp3':
                bestaudio = video.getbestaudio()
                size = bestaudio.get_filesize()
                titulo = bestaudio.title
                extension = bestaudio.extension
                desc = bestaudio.url
            else:
                stream = video.getbest(preftype=self.formato())
                size = stream.get_filesize()
                titulo = stream.title
                extension = stream.extension
                desc = stream.url

            titulo = str(titulo).replace('.','')
            titulo = str(titulo).replace('"','')
            titulo = str(titulo).replace(':','')
            titulo = str(titulo).replace('_','')
            titulo = str(titulo).replace('-','')
            titulo = str(titulo).replace(';','')
            titulo = str(titulo).replace('|','')
            titulo = str(titulo).replace("'",'')
            titulo = str(titulo).replace("+",'')
            titulo = str(titulo).replace("!",'')
            titulo = str(titulo).replace("/",'')
            titulo = str(titulo).replace("\\",'')
            titulo = str(titulo).replace("*",'')
            titulo = str(titulo).replace("#",'')
            titulo = str(titulo).replace("%",'')
            titulo = str(titulo).replace("&",'')
            titulo = str(titulo).replace("(",'')
            titulo = str(titulo).replace(")",'')
            titulo = str(titulo).replace("?",'')
            titulo = str(titulo).replace("¿",'')
            titulo = str(titulo).replace("¡",'')
            titulo = str(titulo).replace("[",'')
            titulo = str(titulo).replace("]",'')
            titulo = str(titulo).replace("{",'')
            titulo = str(titulo).replace("}",'')
            titulo = str(titulo).replace("=",'')
            titulo = str(titulo).replace("~",'')
            titulo = str(titulo).replace("<",'')
            titulo = str(titulo).replace(">",'')

            if 'win32' in self.sistema() or 'win64' in self.sistema():

                filename = os.path.join (os.environ['USERPROFILE'],'videos') + '\\' + titulo + '.' + extension
            else:
                filename = os.path.join (os.environ['HOME'],'Movies') + '/' + titulo + '.' + extension

            self.vskytube.lbl_desc.setText('Descargando ...' + titulo )
            urllib.request.urlretrieve(desc, filename,reporthook=self.funcionprogreso)
            if self.formato() == 'mp3':
                if self.sistema() == 'win32':
                    m4a = os.path.join (os.environ['USERPROFILE'],'videos') + '\\' + titulo + '.' + extension
                    mp3 = os.path.join (os.environ['USERPROFILE'],'videos') + '\\' + titulo + '.mp3'
                    self.ejecutaExe('ffmpeg.exe -i \"%s\" -y \"%s\"' % (m4a , mp3))
                    os.remove(filename)
                if 'darwin' in self.sistema() or 'linux' in self.sistema():
                    m4a = os.path.join (os.environ['HOME'],'Movies') + '/' + titulo + '.' + extension
                    mp3 = os.path.join (os.environ['HOME'],'Movies') + '/' + titulo + '.mp3'
                    self.ejecutaExe('./ffmpeg -i \"%s\" -y \"%s\"' % (m4a , mp3))
                    os.remove(filename)



        QtWidgets.QMessageBox.about(self,'Descarga Completada', 'La Lista se Descargo Correctamente..')
        self.setclipboard()
        self.vskytube.lineEdit.clear()
        self.crea_directorio()
        self.resize(880,480)
        QtCore.QCoreApplication.processEvents()
        self.muestra()
        self.vskytube.lst_encola.clear()


    def add(self):
        try:

            video_id = self.vskytube.lineEdit.text()

            if len(video_id.split('list=')) == 2:
                self.crea_lista()
                video_id = video_id.split('list=')
                if len(video_id) == 2:
                    QtWidgets.QMessageBox.about(self,'PlayList Detectada! ','Estas apunto de  agregar una Lista de '
                                                                        'reproduccion,  \n esto puede tardar varios minutos!' )
                    playlist=pafy.get_playlist(__youtube__ + '/playlist?list=' + video_id[1])
                    num = 0
                    for i in range (len(playlist['items'])):
                        global url
                        url = __youtube__ + '/watch?v=' + playlist['items'][num]['pafy'].videoid
                        print(url)
                        items = []
                        for index in range(self.vskytube.lst_encola.count()):
                            items.append(self.vskytube.lst_encola.item(index).text())

                        existe = 'No'
                        for i in items:
                             if url == i:
                                 existe = 'Si'

                        if existe == 'No':
                            self.setclipboard()
                            if pafy.new(url):
                                self.vskytube.lst_encola.addItem(url)
                                QtCore.QCoreApplication.processEvents()

                        else:

                            self.setclipboard()
                            QtWidgets.QMessageBox.about(self, ' Alerta Link! ', 'Este Link ya fue agregado a la lista!' )

                        num += 1
                self.vskytube.lineEdit.clear()
                url_vid = 'about:blank'
                return
            if len(video_id.split('v=')) == 2:
                video_id = video_id.split('v=')
                if len(video_id) == 2:
                    global url
                    url = __youtube__ + '/watch?v=' + video_id[1]
                    url_vid = __youtube__ + '/embed/' + video_id[1]
                else:
                    global url
                    url = __youtube__ + '/watch?v=' + video_id
                    url_vid = __youtube__ + '/embed/' + video_id

            else:
                self.setclipboard()
                self.vskytube.lineEdit.clear()
                QtWidgets.QMessageBox.about(self, 'Alerta Link! ', 'Link No valido!' )
                return




            items = []
            for index in range(self.vskytube.lst_encola.count()):
                items.append(self.vskytube.lst_encola.item(index).text())

            existe = 'No'
            for i in items:
                 if url == i:
                     existe = 'Si'


            if existe == 'No':
                self.setclipboard()
                if pafy.new(url):
                    self.vskytube.lst_encola.addItem(url)
                    self.vskytube.lineEdit.clear()
            else:
                self.vskytube.lineEdit.clear()
                self.setclipboard()
                QtWidgets.QMessageBox.about(self,'Alerta Link! ','Este Link ya fue agregado a la lista!' )
        except:
             self.vskytube.lineEdit.setText('Link No Valido')
             self.setclipboard()


    def clipboard(self):
        global data
        data = QtWidgets.QApplication.clipboard()
        data = data.text()


        if len(data) == 11:
            item = __youtube__ + ('/watch?v=' + data)
            self.vskytube.lineEdit.setText(item)
            if self.vskytube.ck_lst_auto.isChecked():
                    self.add()
            timer = QtCore.QTimer()
            timer.stop()
            self.CapturaClip()

        if len(str(data).split('?v=')) == 2:
            data = str(data).split('?v=')

            if len(data) == 2:

                item = (__youtube__ + '/watch?v=' + data[1])
                self.vskytube.lineEdit.setText(item)
                if self.vskytube.ck_lst_auto.isChecked():
                    self.add()

                timer = QtCore.QTimer()
                timer.stop()
                self.CapturaClip()

        else:
            timer = QtCore.QTimer()
            timer.stop()
            self.CapturaClip()


    def CapturaClip(self):
        if self.vskytube.ck_captura.isChecked():
            global timer
            timer = QtCore.QTimer()
            timer.start(3000)
            timer.timeout.connect(self.clipboard)
            self.vskytube.ck_lst_auto.setEnabled(True)


        else:
            self.vskytube.ck_lst_auto.setEnabled(False)
            self.vskytube.ck_lst_auto.setChecked(False)
            timer = QtCore.QTimer()
            self.setclipboard()
            timer.stop()

    def crea_directorio(self):

        if self.vskytube.btn_folder.text() == '>':
            self.oculta()
            self.resize(880, 480)
            self.vskytube.treeView.setVisible(True)
            self.vskytube.lbl_perfil.setVisible(True)
            self.vskytube.btn_folder_2.setVisible(True)
            self.vskytube.btn_folder.setText('<')
            self.vskytube.btn_folder.setToolTip('Motrar Videos')
            if 'win32' in self.sistema() or 'win64' in self.sistema():
                self.vskytube.lbl_perfil.setText((os.path.join(os.environ['USERPROFILE'], 'videos')))
            if 'darwin' in self.sistema():
                self.vskytube.lbl_perfil.setText((os.path.join(os.environ['HOME'], 'Movies')))
            if 'linux' in self.sistema():
                if os.path.isdir(os.path.join(os.environ['HOME'], 'Movies')):
                    self.vskytube.lbl_perfil.setText((os.path.join(os.environ['HOME'], 'Movies')))
                else:
                    os.system('mkdir $HOME/Movies')
                    self.vskytube.lbl_perfil.setText((os.path.join(os.environ['HOME'], 'Movies')))

        else:
            self.resize(585, 121)
            self.vskytube.treeView.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder_2.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder.setText('>')
            self.vskytube.btn_folder.setToolTip('Ocultar Videos')
            self.vskytube.lbl_perfil.setVisible(False)

        global fileSystemModel
        fileSystemModel = QtWidgets.QFileSystemModel(self.vskytube.treeView)
        fileSystemModel.setReadOnly(True)

        if 'win32' in self.sistema() or 'win64' in self.sistema():
            fileSystemModel.setRootPath(str((os.path.join(os.environ['USERPROFILE'], 'videos'))))
            indexRoot = fileSystemModel.index(fileSystemModel.rootPath())
            self.vskytube.treeView.setModel(fileSystemModel)
            self.vskytube.treeView.setRootIndex(indexRoot)
        elif 'darwin' in self.sistema() or 'linux' in self.sistema():
            fileSystemModel.setRootPath(str((os.path.join(os.environ['HOME'], 'Movies'))))
            indexRoot = fileSystemModel.index(fileSystemModel.rootPath())
            self.vskytube.treeView.setModel(fileSystemModel)
            self.vskytube.treeView.setRootIndex(indexRoot)


        self.vskytube.treeView.setColumnHidden(1, True)
        self.vskytube.treeView.setColumnHidden(2, True)
        self.vskytube.treeView.setColumnHidden(3, True)
        self.vskytube.treeView.setHeaderHidden(True)


    def crea_lista(self):

        if self.vskytube.btn_add.text() == '>':
            self.oculta()
            self.resize(880, 480)
            self.vskytube.lst_encola.setVisible(True)
            self.vskytube.btn_add_lista.setVisible(True)
            self.vskytube.btn_add_video.setVisible(True)
            self.vskytube.btn_de_item.setVisible(True)
            self.vskytube.btn_add.setText('<')
            self.vskytube.btn_folder.setToolTip('Mostrar Lista')

        else:
            self.resize(585, 121)
            self.vskytube.lst_encola.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_add_lista.setVisible(False)
            self.vskytube.btn_add_video.setVisible(False)
            self.vskytube.btn_de_item.setVisible(False)
            self.vskytube.btn_add.setText('>')
            self.vskytube.btn_folder.setToolTip('Ocultar Lista')


    def oculta(self):
        self.vskytube.lst_encola.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_add_lista.setVisible(False)
        self.vskytube.btn_add_video.setVisible(False)
        self.vskytube.btn_add.setText('>')
        self.vskytube.btn_folder.setToolTip('Ocultar Lista')
        self.vskytube.treeView.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_folder_2.setVisible(False)
        self.vskytube.btn_folder.setText('>')
        self.vskytube.btn_folder.setToolTip('Ocultar Videos')
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_de_item.setVisible(False)
        self.vskytube.lbl_barr.setVisible(False)
        self.vskytube.p_bar.setVisible(False)
        self.vskytube.groupBox_3.setVisible(False)



    def donapaypal(self):
        QtWidgets.QMessageBox.information(self, 'Donacion PayPal', 'Gracias por conciderar  hacer una donacion al proyecto SkyTube \n Todo el dinero seran utilizado para el Hosting \
                                                             \n Muchas Gracias =)')
        webbrowser.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2K6Y3B8AG39DQ')

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def directorio(self, index):
        if self.vskytube.ck_vlc.isChecked():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            self.directorio_vlc(filePath)
            self.vskytube.web.setHtml('''
           <!DOCTYPE html>

           <h1><center> SkyTube Play d(-_-)b </h1></center>
           <br>
             Reproduciendo  ''' + filePath + '''


            </html>
                       ''')

            return

        if 'win32' in self.sistema() or 'win64' in self.sistema():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            os.startfile(filePath)

        if 'darwin' in self.sistema():
            if os.path.isdir('/Applications/VLC.app'):
                indexItem = fileSystemModel.index(index.row(), 0, index.parent())
                filePath = fileSystemModel.filePath(indexItem)
                os.system('open -a /Applications/VLC.app/Contents/MacOS/VLC "' + filePath + '"')
            else:
                QtWidgets.QMessageBox.about(self,'\nError VlC', 'Para poder reproducir los videos desde SkyTube necesitas VLC \n tus videos estan en la  siguiente ruta:\n\n '\
                                                           + str((os.path.join (os.environ['HOME'],'Movies'))))

        if 'linux' in self.sistema():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            self.process.start('xdg-open "' + filePath + '"')

        self.vskytube.web.setHtml('''
           <!DOCTYPE html>

           <h1><center> SkyTube Play d(-_-)b </h1></center>
           <br>
             Reproduciendo  ''' + filePath + '''


            </html>
                       ''')



    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def directorio2(self, index):

        indexItem = fileSystemModel.index(index.row(), 0, index.parent())
        filePath = fileSystemModel.filePath(indexItem)
        self.vskytube.lbl_autor_3.setText(filePath)
        self.vskytube.groupBox_3.setVisible(True)
        if self.vskytube.ck_play.isChecked():
            play_ok = QtGui.QIcon()
            play_ok.addPixmap(QtGui.QPixmap("imagenes/reproduce.png"))
            self.vskytube.btn_play.setIcon(play_ok)
        else:
            play_no = QtGui.QIcon()
            play_no.addPixmap(QtGui.QPixmap("imagenes/loading.png"))
            self.vskytube.btn_play.setIcon(play_no)






    def btn_play(self):
        filePath = self.vskytube.lbl_autor_3.text()
        self.webVid(filePath, 'imagen', 'ok')


    def directorio_vlc(self, video_vlc):
        if 'win32' in self.sistema() or 'win64' in self.sistema():

            if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe'):
                 video_vlc = video_vlc.replace('/', '\\')
                 self.process.start('c:\progra~1\VideoLAN\VLC\\vlc.exe "' + video_vlc + '"')


            elif os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
                self.process.start('c:\progra~2\VideoLAN\VLC\\vlc.exe "' + video_vlc + '"')

        if 'darwin' in self.sistema():
            if os.path.isdir('/Applications/VLC.app'):
                self.process.start('open -a /Applications/VLC.app/Contents/MacOS/VLC "' + video_vlc + '"')

        if 'linux' in self.sistema():
            self.process.start('vlc "' + video_vlc + '"')

    def vlc(self):

        if os.path.isdir('/Applications/VLC.app') or os.path.isfile('/usr/bin/vlc') or os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe') or os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
            self.vskytube.ck_vlc.setChecked(True)
            vlc_ok = QtGui.QIcon()
            vlc_ok.addPixmap(QtGui.QPixmap("imagenes/vlc_ok.png"))
            self.vskytube.ck_vlc.setIcon(vlc_ok)
        else:
            vlc_no = QtGui.QIcon()
            vlc_no.addPixmap(QtGui.QPixmap("imagenes/vlc.png"))
            self.vskytube.ck_vlc.setIcon(vlc_no)
            self.vskytube.ck_vlc.setEnabled(False)

    def vlc_checked(self):
        if self.vskytube.ck_vlc.isChecked():
            vlc_ok = QtGui.QIcon()
            vlc_ok.addPixmap(QtGui.QPixmap("imagenes/vlc_ok.png"))
            self.vskytube.ck_vlc.setIcon(vlc_ok)
        else:
            vlc_no = QtGui.QIcon()
            vlc_no.addPixmap(QtGui.QPixmap("imagenes/vlc.png"))
            self.vskytube.ck_vlc.setIcon(vlc_no)

    def social_google(self):
        webbrowser.open('https://plus.google.com/114802605768559072519')

    def social_facebook(self):
        webbrowser.open('https://www.facebook.com/xskylarx')

    def social_twitter(self):
        webbrowser.open('https://www.twitter.com/xskylarx')


    def folder(self):
        if 'win32' in self.sistema() or 'win64' in self.sistema():
            perfil = (os.path.join(os.environ['USERPROFILE'], 'videos'))
            self.process.start('explorer ' + str(perfil))
        if 'darwin' in self.sistema():
            perfil = (os.path.join(os.environ['HOME'], 'Movies'))
            self.process.start('open ' + str(perfil))
        if 'linux' in self.sistema():
            perfil = (os.path.join(os.environ['HOME'], 'Movies'))
            self.process.start('xdg-open "' + perfil + '"')




    def descarga(self):
        try:
            self.vskytube.p_bar.setMinimum(0)

            if self.ffmpeg():
                pass
            else:
                return


            video =pafy.new(url)
            if self.formato() == 'mp3':
                bestaudio = video.getbestaudio()
                size = bestaudio.get_filesize()
                titulo = bestaudio.title
                extension = bestaudio.extension
                desc = bestaudio.url
            else:
                stream = video.getbest(preftype=self.formato())
                size = stream.get_filesize()
                titulo = stream.title
                extension = stream.extension
                desc = stream.url
            self.vskytube.lineEdit.setVisible(False)
            self.vskytube.btn_valida.setVisible(False)
            self.vskytube.label_7.setVisible(False)
            self.vskytube.btn_folder.setVisible(False)
            self.vskytube.treeView.setVisible(False)
            self.vskytube.btn_folder_2.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            #self.vskytube.groupBox.setVisible(False)
            self.vskytube.groupBox_2.setVisible(False)
            self.vskytube.btn_add.setVisible(False)
            self.vskytube.ck_lst_auto.setVisible(False)
            self.vskytube.ck_captura.setVisible(False)
            self.vskytube.lbl_desc.setStyleSheet("color:red;")
            self.vskytube.lbl_desc.setText('Descargando ...' + titulo)
            self.vskytube.lbl_desc.setVisible(True)
            self.vskytube.lbl_barr.setVisible(True)
            self.vskytube.p_bar.setVisible(True)
            self.resize(489, 82)
            QtWidgets.QMessageBox.about(self,'Empezando Descarga ... ', 'La descarga puede tardar varios minutos, dependiendo de tu conexion ...')



            titulo = str(titulo).replace('.', '')
            titulo = str(titulo).replace('"', '')
            titulo = str(titulo).replace(':', '')
            titulo = str(titulo).replace('_', '')
            titulo = str(titulo).replace('-', '')
            titulo = str(titulo).replace(';', '')
            titulo = str(titulo).replace('|', '')
            titulo = str(titulo).replace("'", '')
            titulo = str(titulo).replace("+", '')
            titulo = str(titulo).replace("!", '')
            titulo = str(titulo).replace("/", '')
            titulo = str(titulo).replace("\\", '')
            titulo = str(titulo).replace("*", '')
            titulo = str(titulo).replace("#", '')
            titulo = str(titulo).replace("%", '')
            titulo = str(titulo).replace("&", '')
            titulo = str(titulo).replace("(", '')
            titulo = str(titulo).replace(")", '')
            titulo = str(titulo).replace("?", '')
            titulo = str(titulo).replace("¿", '')
            titulo = str(titulo).replace("¡", '')
            titulo = str(titulo).replace("[", '')
            titulo = str(titulo).replace("]", '')
            titulo = str(titulo).replace("{", '')
            titulo = str(titulo).replace("}", '')
            titulo = str(titulo).replace("=", '')
            titulo = str(titulo).replace("~", '')
            titulo = str(titulo).replace("<", '')
            titulo = str(titulo).replace(">", '')

            if 'win32' in self.sistema() or 'win64' in self.sistema():

                filename = os.path.join(os.environ['USERPROFILE'], 'videos') + '\\' + titulo + '.' + extension
            else:
                filename = os.path.join(os.environ['HOME'], 'Movies') + '/' + titulo + '.' + extension


            urllib.request.urlretrieve(desc, filename, reporthook=self.funcionprogreso)

            if self.formato() == 'mp3':
                if 'win32' in self.sistema() or 'win64' in self.sistema():
                    m4a = os.path.join(os.environ['USERPROFILE'], 'videos') + '\\' + titulo + '.' + extension
                    mp3 = os.path.join(os.environ['USERPROFILE'], 'videos') + '\\' + titulo + '.mp3'


                    self.ejecutaExe('ffmpeg.exe -i \"%s\" -y \"%s\"' % (m4a, mp3))
                    os.remove(filename)
                if 'darwin' in self.sistema() or 'linux' in self.sistema():
                    m4a = os.path.join(os.environ['HOME'], 'Movies') + '/' + titulo + '.' + extension
                    mp3 = os.path.join(os.environ['HOME'], 'Movies') + '/' + titulo + '.mp3'

                    self.ejecutaExe('./ffmpeg -i \"%s\" -y \"%s\"' % (m4a, mp3))
                    os.remove(filename)


            self.setclipboard()
            self.vskytube.lineEdit.clear()
            QtWidgets.QMessageBox.about(self, 'Descarga Finalizada', ' Tu descarga Finalizo')
            self.crea_directorio()
            self.resize(880, 480)
            QtCore.QCoreApplication.processEvents()
            self.muestra()



        except Exception as e:
            QtWidgets.QMessageBox.about(self,'Error Descarga', str(e))


    def sistema(self):
        return sys.platform

    def muestra(self):
        QtCore.QCoreApplication.processEvents()
        self.vskytube.lineEdit.setVisible(True)
        self.vskytube.btn_valida.setVisible(True)
        self.vskytube.label_7.setVisible(True)
        self.vskytube.btn_folder.setVisible(True)
        self.vskytube.groupBox_2.setVisible(True)
        self.vskytube.btn_add.setVisible(True)
        self.vskytube.ck_lst_auto.setVisible(True)
        self.vskytube.ck_captura.setVisible(True)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.lbl_barr.setVisible(False)
        self.vskytube.p_bar.setVisible(False)
        self.vskytube.lineEdit.clear()


    def formato(self):
        formato = self.vskytube.f_box.currentText()
        return formato


    def valida_descarga(self):
        try:
            url = ''
            for index in range(self.vskytube.lst_encola.count()):
                url = self.vskytube.lst_encola.item(index).text()

            if  url == '':
                QtWidgets.QMessageBox.about(self,'Error Lista vacia','No hay Links para procesar')
            else:
                self.descarga_lista()
        except Exception as e:
            QtWidgets.QMessageBox.about(self,'Error en Link ','El Link : ' + url + ' No existe..\n Se eliminara de la lista..\n Por favor Vuelve a descargar la lista ')

    def valida_lista(self):
        try:
            self.vskytube.web.load(QtCore.QUrl('about:blank'))
            self.vskytube.web.show()

            item = self.vskytube.lst_encola.currentItem()
            url = item.text()

            video_id = url


            if len(video_id.split('v=')) == 2:
                video_id = video_id.split('v=')
            if len(video_id) == 2:
                url_vid = __youtube__ + '/embed/' + video_id[1]
            else:
                url_vid = __youtube__ + '/embed/' + video_id

            video = pafy.new(url)
            best = video.getbest(preftype=self.formato())
            self.vskytube.lbl_autor.setText(video.author)

            self.vskytube.btn_valida_2.setVisible(False)

            url_img = video.bigthumb

            if 'VEVO' in video.author:
                self.webVid(best.url, url_img, 'ok')

            else:
                self.webVid(url_vid, url_img, 'no')

        except Exception as e:

            QtWidgets.QMessageBox.about(self, 'Error en Link ', 'El Link : ' + item.text() + 'No existe..\n Se eliminara de la lista..' + str(e))
            self.elimina_item()


    def valida(self):
        try:
            self.oculta()
            self.resize(585, 121)
            video_id = self.vskytube.lineEdit.text()

            if len(video_id) == 11:
                url = __youtube__ + '/watch?v=' + video_id
                url_vid = __youtube__ + '/embed/' + video_id

            if len(video_id.split('list=')) == 2:
                video_id = video_id.split('list=')
                print(video_id)
                if len(video_id) == 2:
                    self.add()
                url_vid = 'about:blank'
                return 'termine'
                sys.exit(0)

            if len(video_id.split('v=')) == 2:
                video_id = video_id.split('v=')
                if len(video_id) == 2:
                    global url
                    url = __youtube__ + '/watch?v=' + video_id[1]
                    url_vid = __youtube__ + '/embed/' + video_id[1]
                else:
                    global url
                    url = __youtube__ + '/watch?v=' + video_id
                    url_vid = __youtube__ + '/embed/' + video_id




            global video
            global best

            video = pafy.new(url)
            url_img = video.title
            """if self.formato() == 'mp3':

                best = video.getbestaudio()


            else:

                best = video.getbest(preftype='mp4')"""


            best = video.getbest(preftype='mp4')
            self.vskytube.lbl_autor.setText(video.author)
            self.resize(579, 480)
            self.vskytube.btn_valida_2.setVisible(True)


            if 'VEVO' in video.author:
                self.webVid(best.url, url_img, 'ok')

            else:
                self.webVid(url_vid, url_img, 'no')


        except Exception as e:
            QtWidgets.QMessageBox.about(self,'Error SkyTube ', ' No existe el video favor de verificar.')
            QtWidgets.QMessageBox.about(self,'Error SkyTube', str(e))



def main():
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QImageReader.supportedImageFormats()
    vskytube = v_skytube()
    vskytube.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
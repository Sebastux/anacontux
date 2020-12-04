#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Titre             : anacontux.py
Description       : Classe principale permettant l'exploitation
                  : de la fenetre
Auteur            : Sebastux
Date              : 27/11/2020
Version           : 1.00
Utilisation	      : ./anacontux.py
Notes             :
Version de python : 3.9
"""
# Metadonnées du script
__author__     = "Sebastux"
__copyright__  = "None"
__license__    = "None"
__version__    = "1.00"
__date__       = "27/11/2020"
__maintainer__ = "Sebastux"
__email__      = "None"
__status__     = "alpha"

# Directive(s) d'importation
from kickstux import *
from fonctions import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, os


# Création de la classe permettant l'exploitation de la fenetre.
class anacontux(QtWidgets.QMainWindow):
    def __init__(self):
        super(anacontux, self).__init__()

        # Création de la fenetre.
        self.ui = Ui_mw_anaconda()
        self.ui.setupUi(self)

        # Séléction du 1 er onglet par défaut.
        self.ui.tab_anacontux.setCurrentIndex(0)

        # Centrage de la fenetre sur l'écran.
        self.centrer_fenetre()

        # Ajout d'une icone à la fenetre.
        self.setWindowIcon(QtGui.QIcon("Tuxicon.ico"))

        # Déclaration et initialisation de variables
        ChoixDistrib = -1
        ChiffrePasswd = False
        HeureGmt = False

        # Evenement case cochée ou décochée affiche ou masque le mot de passe.
        self.ui.cb_affichePasswd.stateChanged.connect(self.affichepasse)

        # Evenement case cochée ou décochée chiffrement du mot de passe.
        self.ui.cb_chiffrePasswd.stateChanged.connect(self.chiffrement)

        # Evenement case cochée ou décochée choix de l(heure GMT).
        self.ui.cb_gmt.stateChanged.connect(self.ChoixGmt)

        # Evenements comparaison des mots de passe
        self.ui.edt_password.textChanged[str].connect(self.changePasswd)
        self.ui.edt_verifPassword.textChanged[str].connect(self.changeVerifPasswd)

        # Evenement choix de la distribution
        self.ui.rb_centos7.toggled.connect(self.ChoixCentos7)
        self.ui.rb_c7netinstall.toggled.connect(self.ChoixCentos7Netinstall)
        self.ui.rb_centos8.toggled.connect(self.ChoixCentos8)
        self.ui.rb_c8netinstall.toggled.connect(self.ChoixCentos8Netinstall)
        self.ui.rb_fedora.toggled.connect(self.ChoixFedora)
        self.ui.cbx_fuseaux.clear()
        self.ui.cbx_fuseaux.addItem("Sélectionnez une distribution.")

        # Chargement de la liste des claviers
        self.ChargeListesClavier()

        # Activation désactivation de la saisie des URL en pré installation
        self.ui.rb_PreAutre.toggled.connect(self.PreUrlDepot_click)

        # Activation désactivation de la saisie des URL en pré installation
        self.ui.rb_PostAutre.toggled.connect(self.PostUrlDepot_click)

        # Installer rpm fusion en pré installation
        self.ui.cb_PreRpmFusion.stateChanged.connect(self.PreRpmFusion_click)

        # Installer rpm fusion en post installation
        self.ui.cb_PostRpmFusion.stateChanged.connect(self.PostRpmFusion_click)

        # Installer EPEL en post installation
        self.ui.cb_PostEpel.stateChanged.connect(self.PostEpel_click)

        # Installer EPEL en pre installation PreEpel_click
        self.ui.cb_PreEpel.stateChanged.connect(self.PreEpel_click)

        # Activation désactivation de la zone de saisie des commande pour la pré-installation
        self.ui.rb_PreAucun.toggled.connect(self.PreAucun_click)

        # Activation désactivation de la zone de saisie des commande pour la post-installation
        self.ui.rb_PostAucun.toggled.connect(self.PostAucun_click)

    # Init fenetre
    def centrer_fenetre(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        enterPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
# ************************ Config base *****************************************
    def affichepasse(self, state):
        if state == Qt.Checked:
            self.ui.edt_verifPassword.setEnabled(False)
            self.ui.edt_verifPassword.setText('')
            self.ui.edt_password.setEchoMode(QLineEdit.Normal)
            self.ui.edt_verifPassword.setStyleSheet("background-color: white;")
        else:
            self.ui.edt_verifPassword.setEnabled(True)
            self.ui.edt_password.setEchoMode(QLineEdit.Password)
            self.ui.edt_verifPassword.setStyleSheet("background-color: red;")

    def chiffrement(self, state):
        ChiffrePasswd = bool(state)

    def ChoixGmt(self, state):
        HeureGmt = bool(state)

    def changePasswd(self, text):
        if text != self.ui.edt_verifPassword.text():
            self.ui.edt_verifPassword.setStyleSheet("background-color: red;")
        elif text == self.ui.edt_verifPassword.text():
            self.ui.edt_verifPassword.setStyleSheet("background-color: green;")

    def changeVerifPasswd(self, text):
        if text != self.ui.edt_password.text():
            self.ui.edt_verifPassword.setStyleSheet("background-color: red;")
        elif text == self.ui.edt_password.text():
            self.ui.edt_verifPassword.setStyleSheet("background-color: green;")

    def ChoixCentos7(self):
        ChoixDistrib = 0
        if self.ui.rb_centos7.isChecked():
            try:
                self.ui.cbx_fuseaux.clear()
                with open('timezones/centos7.txt', 'r') as fuseau:
                    while True:
                        # Lecture du fichier ligne par ligne
                        lignes = fuseau.readline()

                        # Si la ligne est vide alors on a atteind la fin du fichier
                        if not lignes:
                            break
                        self.ui.cbx_fuseaux.addItem(lignes.strip())
                fuseau.close()
            except FileNotFoundError:
                AfficheMessages("Liste de fuseaux horaires introuvable.", "Impossible de charger la liste des fuseaux horaires pour centos 7.",QMessageBox.Critical ,QMessageBox.Ok)
                self.ui.bg_distribution.setExclusive(False)
                self.ui.rb_centos7.setChecked(False)
                self.ui.bg_distribution.setExclusive(True)
                self.ui.cbx_fuseaux.clear()
                self.ui.cbx_fuseaux.addItem("Erreur de chargement")
                self.ui.cbx_fuseaux.addItem("de la liste des")
                self.ui.cbx_fuseaux.addItem("fuseaux horaires")

    def ChoixCentos7Netinstall(self):
        ChoixDistrib = 1
        self.ui.edt_UrlDepot.setEnabled(self.ui.rb_c7netinstall.isChecked())
        self.ui.edt_UrlDepot.clear()
        if self.ui.rb_c7netinstall.isChecked():
            try:
                self.ui.cbx_fuseaux.clear()
                with open('timezones/centos7.txt', 'r') as fuseau:
                    while True:
                        # Lecture du fichier ligne par ligne
                        lignes = fuseau.readline()

                        # Si la ligne est vide alors on a atteind la fin du fichier
                        if not lignes:
                            break
                        self.ui.cbx_fuseaux.addItem(lignes.strip())
                fuseau.close()
            except FileNotFoundError:
                AfficheMessages("Liste de fuseaux horaires introuvable.", "Impossible de charger la liste des fuseaux horaires pour centos 7.",QMessageBox.Critical ,QMessageBox.Ok)
                self.ui.bg_distribution.setExclusive(False)
                self.ui.rb_c7netinstall.setChecked(False)
                self.ui.bg_distribution.setExclusive(True)
                self.ui.cbx_fuseaux.clear()
                self.ui.cbx_fuseaux.addItem("Erreur de chargement")
                self.ui.cbx_fuseaux.addItem("de la liste des")
                self.ui.cbx_fuseaux.addItem("fuseaux horaires")

    def ChoixCentos8(self):
        ChoixDistrib = 2
        self.ui.edt_UrlDepot.setEnabled(False)
        if self.ui.rb_centos8.isChecked():
            try:
                self.ui.cbx_fuseaux.clear()
                with open('timezones/centos8.txt', 'r') as fuseau:
                    while True:
                        # Lecture du fichier ligne par ligne
                        lignes = fuseau.readline()

                        # Si la ligne est vide alors on a atteind la fin du fichier
                        if not lignes:
                            break
                        self.ui.cbx_fuseaux.addItem(lignes.strip())
                fuseau.close()
            except FileNotFoundError:
                AfficheMessages("Liste de fuseaux horaires introuvable.", "Impossible de charger la liste des fuseaux horaires pour centos 8.",QMessageBox.Critical ,QMessageBox.Ok)
                self.ui.bg_distribution.setExclusive(False)
                self.ui.rb_centos8.setChecked(False)
                self.ui.bg_distribution.setExclusive(True)
                self.ui.cbx_fuseaux.clear()
                self.ui.cbx_fuseaux.addItem("Erreur de chargement")
                self.ui.cbx_fuseaux.addItem("de la liste des")
                self.ui.cbx_fuseaux.addItem("fuseaux horaires")

    def ChoixCentos8Netinstall(self):
        ChoixDistrib = 3
        self.ui.edt_UrlDepot.setEnabled(self.ui.rb_c8netinstall.isChecked())
        self.ui.edt_UrlDepot.clear()
        if self.ui.rb_c8netinstall.isChecked():
            try:
                self.ui.cbx_fuseaux.clear()
                with open('timezones/centos8.txt', 'r') as fuseau:
                    while True:
                        # Lecture du fichier ligne par ligne
                        lignes = fuseau.readline()

                        # Si la ligne est vide alors on a atteind la fin du fichier
                        if not lignes:
                            break
                        self.ui.cbx_fuseaux.addItem(lignes.strip())
                fuseau.close()
            except FileNotFoundError:
                AfficheMessages("Liste de fuseaux horaires introuvable.", "Impossible de charger la liste des fuseaux horaires pour centos 8.",QMessageBox.Critical ,QMessageBox.Ok)
                self.ui.bg_distribution.setExclusive(False)
                self.ui.rb_c8netinstall.setChecked(False)
                self.ui.bg_distribution.setExclusive(True)
                self.ui.cbx_fuseaux.clear()
                self.ui.cbx_fuseaux.addItem("Erreur de chargement")
                self.ui.cbx_fuseaux.addItem("de la liste des")
                self.ui.cbx_fuseaux.addItem("fuseaux horaires")

    def ChoixFedora(self):
        ChoixDistrib = 4
        if self.ui.rb_fedora.isChecked():
            # self.ui.edt_UrlDepot.setEnabled(False)
            # self.ui.edt_UrlDepot.clear()
            try:
                self.ui.cbx_fuseaux.clear()
                with open('timezones/Fedora3x.txt', 'r') as fuseau:
                    while True:
                        # Lecture du fichier ligne par ligne
                        lignes = fuseau.readline()

                        # Si la ligne est vide alors on a atteind la fin du fichier
                        if not lignes:
                            break
                        self.ui.cbx_fuseaux.addItem(lignes.strip())
                fuseau.close()
            except FileNotFoundError:
                AfficheMessages("Liste de fuseaux horaires introuvable.", "Impossible de charger la liste des fuseaux horaires pour Fedora.",QMessageBox.Critical ,QMessageBox.Ok)
                self.ui.bg_distribution.setExclusive(False)
                self.ui.rb_fedora.setChecked(False)
                self.ui.bg_distribution.setExclusive(True)
                self.ui.cbx_fuseaux.clear()
                self.ui.cbx_fuseaux.addItem("Erreur de chargement")
                self.ui.cbx_fuseaux.addItem("de la liste des")
                self.ui.cbx_fuseaux.addItem("fuseaux horaires")

    def ChargeListesClavier(self):
        try:
            self.ui.cbx_langueos.clear()
            with open('datas/oslanguec7.txt', 'r') as languageos:
                while True:
                    ligne = languageos.readline()
                    position = ligne.find(":")
                    if position != -1:
                        self.ui.cbx_langueos.addItem(ligne[0:position].strip())

                    if not ligne:
                        break

            languageos.close()
        except FileNotFoundError:
            AfficheMessages("Liste de langue introuvable.", "Impossible de charger la liste des langues.",QMessageBox.Critical ,QMessageBox.Ok)
            self.ui.bg_distribution.setExclusive(False)
            self.ui.rb_fedora.setChecked(False)
            self.ui.bg_distribution.setExclusive(True)
            self.ui.cbx_langueos.clear()
            self.ui.cbx_langueos.addItem("Erreur de chargement")
            self.ui.cbx_langueos.addItem("de la liste des")
            self.ui.cbx_langueos.addItem("langues.")

# ************************ Pré installation ************************************
    # Activation désactivation de la zone de saisie d'URL
    def PreUrlDepot_click(self):
        self.ui.edt_PreInstall.setEnabled(self.ui.rb_PreAutre.isChecked())
        self.ui.edt_PreInstall.clear()

    # Activation désactivation du choix des dépot rpm fusion et de la checkbox post install
    def PreRpmFusion_click(self):
        self.ui.cb_PostRpmFusion.setEnabled(not self.ui.cb_PreRpmFusion.isChecked())
        self.ui.gb_PreRpmFusion.setEnabled(self.ui.cb_PreRpmFusion.isChecked())
        if not self.ui.cb_PreRpmFusion.isChecked():
            self.ui.bg_PreRpmFusion.setExclusive(False)
            self.ui.rb_PreRpmFree.setChecked(False)
            self.ui.rb_PreRpmNonFree.setChecked(False)
            self.ui.rb_PreDeux.setChecked(False)
            self.ui.bg_PreRpmFusion.setExclusive(True)

    # Activation désactivation du choix EPEL et de la checkbox EPEL post install
    def PreEpel_click(self):
        self.ui.cb_PostEpel.setEnabled(not self.ui.cb_PreEpel.isChecked())

    # Activation désactivation de la zone de saisie des commande pour la préinstallation
    def PreAucun_click(self):
        self.ui.ptedt_PreListeCommandes.setEnabled(not self.ui.rb_PreAucun.isChecked())
        self.ui.ptedt_PreListeCommandes.clear()
        # self.ui.ptedt_PostListeCommandes.setEnabled(True)

# ************************ Post installation ***********************************
    # Activation désactivation de la zone de saisie d'URL
    def PostUrlDepot_click(self):
        self.ui.edt_postinstall.setEnabled(self.ui.rb_PostAutre.isChecked())
        self.ui.edt_postinstall.clear()
        self.ui.tab_anacontux.setEnabled(self.ui.rb_PreAucun.isChecked())

    # Activation désactivation du choix des dépot rpm fusion et de la checkbox pré install
    def PostRpmFusion_click(self):
        self.ui.cb_PreRpmFusion.setEnabled(not self.ui.cb_PostRpmFusion.isChecked())
        self.ui.gb_PostRpmFusion.setEnabled(self.ui.cb_PostRpmFusion.isChecked())
        if not self.ui.cb_PostRpmFusion.isChecked():
            self.ui.bg_PostRpmFusion.setExclusive(False)
            self.ui.rb_PostRpmFree.setChecked(False)
            self.ui.rb_PostRpmNonFree.setChecked(False)
            self.ui.rb_PostDeux.setChecked(False)
            self.ui.bg_PostRpmFusion.setExclusive(True)

    # Activation désactivation du choix EPEL et de la checkbox EPEL pré install
    def PostEpel_click(self):
        self.ui.cb_PreEpel.setEnabled(not self.ui.cb_PostEpel.isChecked())

    # Activation désactivation de la zone de saisie des commande pour la préinstallation
    def PostAucun_click(self):
        self.ui.ptedt_PostListeCommandes.setEnabled(not self.ui.rb_PostAucun.isChecked())
        self.ui.ptedt_PostListeCommandes.clear()


# ************************ Programe principal***********************************
if __name__ == "__main__":
    ''' Application principale '''
    app = QtWidgets.QApplication(sys.argv)
    w = anacontux()
    w.show()
    sys.exit(app.exec_())

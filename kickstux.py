# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anaconda.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mw_anaconda(object):
    def setupUi(self, mw_anaconda):
        mw_anaconda.setObjectName("mw_anaconda")
        mw_anaconda.resize(1050, 509)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Tuxicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mw_anaconda.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mw_anaconda)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_anacontux = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_anacontux.setGeometry(QtCore.QRect(0, 0, 1051, 491))
        self.tab_anacontux.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_anacontux.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab_anacontux.setObjectName("tab_anacontux")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gb_configBase = QtWidgets.QGroupBox(self.tab_2)
        self.gb_configBase.setGeometry(QtCore.QRect(0, 210, 971, 251))
        self.gb_configBase.setObjectName("gb_configBase")
        self.lbl_langueos = QtWidgets.QLabel(self.gb_configBase)
        self.lbl_langueos.setGeometry(QtCore.QRect(5, 32, 141, 17))
        self.lbl_langueos.setObjectName("lbl_langueos")
        self.lbl_clavier = QtWidgets.QLabel(self.gb_configBase)
        self.lbl_clavier.setGeometry(QtCore.QRect(5, 72, 62, 17))
        self.lbl_clavier.setObjectName("lbl_clavier")
        self.lbl_fuseaux = QtWidgets.QLabel(self.gb_configBase)
        self.lbl_fuseaux.setGeometry(QtCore.QRect(5, 112, 111, 17))
        self.lbl_fuseaux.setObjectName("lbl_fuseaux")
        self.cb_gmt = QtWidgets.QCheckBox(self.gb_configBase)
        self.cb_gmt.setGeometry(QtCore.QRect(540, 110, 91, 23))
        self.cb_gmt.setToolTip("")
        self.cb_gmt.setObjectName("cb_gmt")
        self.cbx_langueos = QtWidgets.QComboBox(self.gb_configBase)
        self.cbx_langueos.setGeometry(QtCore.QRect(150, 30, 380, 25))
        self.cbx_langueos.setObjectName("cbx_langueos")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_langueos.addItem("")
        self.cbx_clavier = QtWidgets.QComboBox(self.gb_configBase)
        self.cbx_clavier.setGeometry(QtCore.QRect(150, 70, 380, 25))
        self.cbx_clavier.setObjectName("cbx_clavier")
        self.cbx_fuseaux = QtWidgets.QComboBox(self.gb_configBase)
        self.cbx_fuseaux.setGeometry(QtCore.QRect(150, 110, 380, 25))
        self.cbx_fuseaux.setObjectName("cbx_fuseaux")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.cbx_fuseaux.addItem("")
        self.gbx_PasswdRoot = QtWidgets.QGroupBox(self.gb_configBase)
        self.gbx_PasswdRoot.setGeometry(QtCore.QRect(10, 140, 371, 111))
        self.gbx_PasswdRoot.setObjectName("gbx_PasswdRoot")
        self.label = QtWidgets.QLabel(self.gbx_PasswdRoot)
        self.label.setGeometry(QtCore.QRect(5, 32, 100, 17))
        self.label.setObjectName("label")
        self.lbl_verifPassword = QtWidgets.QLabel(self.gbx_PasswdRoot)
        self.lbl_verifPassword.setGeometry(QtCore.QRect(5, 72, 100, 17))
        self.lbl_verifPassword.setObjectName("lbl_verifPassword")
        self.edt_verifPassword = QtWidgets.QLineEdit(self.gbx_PasswdRoot)
        self.edt_verifPassword.setGeometry(QtCore.QRect(110, 70, 250, 25))
        self.edt_verifPassword.setToolTip("")
        self.edt_verifPassword.setMaxLength(20)
        self.edt_verifPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edt_verifPassword.setDragEnabled(False)
        self.edt_verifPassword.setClearButtonEnabled(True)
        self.edt_verifPassword.setObjectName("edt_verifPassword")
        self.edt_password = QtWidgets.QLineEdit(self.gbx_PasswdRoot)
        self.edt_password.setGeometry(QtCore.QRect(110, 30, 250, 23))
        self.edt_password.setToolTip("")
        self.edt_password.setMaxLength(20)
        self.edt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edt_password.setClearButtonEnabled(True)
        self.edt_password.setObjectName("edt_password")
        self.cb_chiffrePasswd = QtWidgets.QCheckBox(self.gb_configBase)
        self.cb_chiffrePasswd.setGeometry(QtCore.QRect(400, 170, 191, 23))
        self.cb_chiffrePasswd.setToolTip("")
        self.cb_chiffrePasswd.setObjectName("cb_chiffrePasswd")
        self.cb_affichePasswd = QtWidgets.QCheckBox(self.gb_configBase)
        self.cb_affichePasswd.setGeometry(QtCore.QRect(400, 210, 191, 21))
        self.cb_affichePasswd.setToolTip("")
        self.cb_affichePasswd.setObjectName("cb_affichePasswd")
        self.gb_configAvance = QtWidgets.QGroupBox(self.tab_2)
        self.gb_configAvance.setGeometry(QtCore.QRect(0, 0, 971, 211))
        self.gb_configAvance.setObjectName("gb_configAvance")
        self.gb_distribution = QtWidgets.QGroupBox(self.gb_configAvance)
        self.gb_distribution.setGeometry(QtCore.QRect(10, 30, 171, 171))
        self.gb_distribution.setObjectName("gb_distribution")
        self.rb_centos7 = QtWidgets.QRadioButton(self.gb_distribution)
        self.rb_centos7.setGeometry(QtCore.QRect(5, 20, 106, 23))
        self.rb_centos7.setObjectName("rb_centos7")
        self.bg_distribution = QtWidgets.QButtonGroup(mw_anaconda)
        self.bg_distribution.setObjectName("bg_distribution")
        self.bg_distribution.addButton(self.rb_centos7)
        self.rb_centos8 = QtWidgets.QRadioButton(self.gb_distribution)
        self.rb_centos8.setGeometry(QtCore.QRect(5, 80, 106, 23))
        self.rb_centos8.setObjectName("rb_centos8")
        self.bg_distribution.addButton(self.rb_centos8)
        self.rb_fedora = QtWidgets.QRadioButton(self.gb_distribution)
        self.rb_fedora.setGeometry(QtCore.QRect(5, 140, 151, 23))
        self.rb_fedora.setObjectName("rb_fedora")
        self.bg_distribution.addButton(self.rb_fedora)
        self.rb_c7netinstall = QtWidgets.QRadioButton(self.gb_distribution)
        self.rb_c7netinstall.setGeometry(QtCore.QRect(5, 50, 161, 23))
        self.rb_c7netinstall.setObjectName("rb_c7netinstall")
        self.bg_distribution.addButton(self.rb_c7netinstall)
        self.rb_c8netinstall = QtWidgets.QRadioButton(self.gb_distribution)
        self.rb_c8netinstall.setGeometry(QtCore.QRect(5, 110, 161, 23))
        self.rb_c8netinstall.setObjectName("rb_c8netinstall")
        self.bg_distribution.addButton(self.rb_c8netinstall)
        self.edt_UrlDepot = QtWidgets.QLineEdit(self.gb_configAvance)
        self.edt_UrlDepot.setEnabled(False)
        self.edt_UrlDepot.setGeometry(QtCore.QRect(190, 100, 741, 23))
        self.edt_UrlDepot.setObjectName("edt_UrlDepot")
        self.tab_anacontux.addTab(self.tab_2, "")
        self.tab_installation = QtWidgets.QWidget()
        self.tab_installation.setObjectName("tab_installation")
        self.tab_anacontux.addTab(self.tab_installation, "")
        self.tab_boot = QtWidgets.QWidget()
        self.tab_boot.setObjectName("tab_boot")
        self.tab_anacontux.addTab(self.tab_boot, "")
        self.tab_partitions = QtWidgets.QWidget()
        self.tab_partitions.setObjectName("tab_partitions")
        self.tab_anacontux.addTab(self.tab_partitions, "")
        self.tab_reseau = QtWidgets.QWidget()
        self.tab_reseau.setObjectName("tab_reseau")
        self.tab_anacontux.addTab(self.tab_reseau, "")
        self.tab_authentification = QtWidgets.QWidget()
        self.tab_authentification.setObjectName("tab_authentification")
        self.tab_anacontux.addTab(self.tab_authentification, "")
        self.tab_PareFeu = QtWidgets.QWidget()
        self.tab_PareFeu.setObjectName("tab_PareFeu")
        self.tab_anacontux.addTab(self.tab_PareFeu, "")
        self.tab_affichage = QtWidgets.QWidget()
        self.tab_affichage.setObjectName("tab_affichage")
        self.tab_anacontux.addTab(self.tab_affichage, "")
        self.tab_packages = QtWidgets.QWidget()
        self.tab_packages.setObjectName("tab_packages")
        self.tab_anacontux.addTab(self.tab_packages, "")
        self.tab_PreInstallation = QtWidgets.QWidget()
        self.tab_PreInstallation.setObjectName("tab_PreInstallation")
        self.gb_InterpreteurPreInstall = QtWidgets.QGroupBox(self.tab_PreInstallation)
        self.gb_InterpreteurPreInstall.setGeometry(QtCore.QRect(0, 0, 231, 71))
        self.gb_InterpreteurPreInstall.setObjectName("gb_InterpreteurPreInstall")
        self.rb_PreAucun = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PreAucun.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.rb_PreAucun.setChecked(True)
        self.rb_PreAucun.setObjectName("rb_PreAucun")
        self.rb_PreBash = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PreBash.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.rb_PreBash.setObjectName("rb_PreBash")
        self.rb_PrePython2 = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PrePython2.setGeometry(QtCore.QRect(80, 30, 81, 21))
        self.rb_PrePython2.setObjectName("rb_PrePython2")
        self.rb_PrePython3 = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PrePython3.setGeometry(QtCore.QRect(80, 50, 81, 21))
        self.rb_PrePython3.setObjectName("rb_PrePython3")
        self.rb_PrePerl = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PrePerl.setGeometry(QtCore.QRect(170, 30, 51, 21))
        self.rb_PrePerl.setObjectName("rb_PrePerl")
        self.rb_PreAutre = QtWidgets.QRadioButton(self.gb_InterpreteurPreInstall)
        self.rb_PreAutre.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.rb_PreAutre.setObjectName("rb_PreAutre")
        self.lbl_PreInsertion = QtWidgets.QLabel(self.tab_PreInstallation)
        self.lbl_PreInsertion.setGeometry(QtCore.QRect(5, 80, 461, 16))
        self.lbl_PreInsertion.setObjectName("lbl_PreInsertion")
        self.ptedt_PreListeCommandes = QtWidgets.QPlainTextEdit(self.tab_PreInstallation)
        self.ptedt_PreListeCommandes.setEnabled(False)
        self.ptedt_PreListeCommandes.setGeometry(QtCore.QRect(0, 100, 1051, 361))
        self.ptedt_PreListeCommandes.setObjectName("ptedt_PreListeCommandes")
        self.edt_PreInstall = QtWidgets.QLineEdit(self.tab_PreInstallation)
        self.edt_PreInstall.setEnabled(False)
        self.edt_PreInstall.setGeometry(QtCore.QRect(240, 40, 201, 23))
        self.edt_PreInstall.setObjectName("edt_PreInstall")
        self.gb_PreRpmFusion = QtWidgets.QGroupBox(self.tab_PreInstallation)
        self.gb_PreRpmFusion.setEnabled(False)
        self.gb_PreRpmFusion.setGeometry(QtCore.QRect(790, 10, 251, 61))
        self.gb_PreRpmFusion.setObjectName("gb_PreRpmFusion")
        self.rb_PreRpmFree = QtWidgets.QRadioButton(self.gb_PreRpmFusion)
        self.rb_PreRpmFree.setGeometry(QtCore.QRect(5, 20, 91, 21))
        self.rb_PreRpmFree.setObjectName("rb_PreRpmFree")
        self.bg_PreRpmFusion = QtWidgets.QButtonGroup(mw_anaconda)
        self.bg_PreRpmFusion.setObjectName("bg_PreRpmFusion")
        self.bg_PreRpmFusion.addButton(self.rb_PreRpmFree)
        self.rb_PreRpmNonFree = QtWidgets.QRadioButton(self.gb_PreRpmFusion)
        self.rb_PreRpmNonFree.setGeometry(QtCore.QRect(5, 40, 121, 21))
        self.rb_PreRpmNonFree.setObjectName("rb_PreRpmNonFree")
        self.bg_PreRpmFusion.addButton(self.rb_PreRpmNonFree)
        self.rb_PreDeux = QtWidgets.QRadioButton(self.gb_PreRpmFusion)
        self.rb_PreDeux.setGeometry(QtCore.QRect(160, 20, 81, 21))
        self.rb_PreDeux.setObjectName("rb_PreDeux")
        self.bg_PreRpmFusion.addButton(self.rb_PreDeux)
        self.cb_PreEpel = QtWidgets.QCheckBox(self.tab_PreInstallation)
        self.cb_PreEpel.setGeometry(QtCore.QRect(520, 10, 171, 21))
        self.cb_PreEpel.setObjectName("cb_PreEpel")
        self.cb_PreRpmFusion = QtWidgets.QCheckBox(self.tab_PreInstallation)
        self.cb_PreRpmFusion.setGeometry(QtCore.QRect(520, 40, 241, 21))
        self.cb_PreRpmFusion.setObjectName("cb_PreRpmFusion")
        self.tab_anacontux.addTab(self.tab_PreInstallation, "")
        self.tab_PostInstallation = QtWidgets.QWidget()
        self.tab_PostInstallation.setObjectName("tab_PostInstallation")
        self.gb_InterpreteurPostInstall = QtWidgets.QGroupBox(self.tab_PostInstallation)
        self.gb_InterpreteurPostInstall.setGeometry(QtCore.QRect(0, 0, 231, 71))
        self.gb_InterpreteurPostInstall.setObjectName("gb_InterpreteurPostInstall")
        self.rb_PostAucun = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostAucun.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.rb_PostAucun.setChecked(True)
        self.rb_PostAucun.setObjectName("rb_PostAucun")
        self.rb_PostBash = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostBash.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.rb_PostBash.setObjectName("rb_PostBash")
        self.rb_PostPython2 = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostPython2.setGeometry(QtCore.QRect(80, 30, 81, 21))
        self.rb_PostPython2.setObjectName("rb_PostPython2")
        self.rb_PostPython3 = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostPython3.setGeometry(QtCore.QRect(80, 50, 81, 21))
        self.rb_PostPython3.setObjectName("rb_PostPython3")
        self.rb_PostPerl = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostPerl.setGeometry(QtCore.QRect(170, 30, 51, 21))
        self.rb_PostPerl.setObjectName("rb_PostPerl")
        self.rb_PostAutre = QtWidgets.QRadioButton(self.gb_InterpreteurPostInstall)
        self.rb_PostAutre.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.rb_PostAutre.setObjectName("rb_PostAutre")
        self.edt_postinstall = QtWidgets.QLineEdit(self.tab_PostInstallation)
        self.edt_postinstall.setEnabled(False)
        self.edt_postinstall.setGeometry(QtCore.QRect(240, 40, 201, 23))
        self.edt_postinstall.setObjectName("edt_postinstall")
        self.lbl_PostInsertion = QtWidgets.QLabel(self.tab_PostInstallation)
        self.lbl_PostInsertion.setGeometry(QtCore.QRect(5, 80, 501, 16))
        self.lbl_PostInsertion.setObjectName("lbl_PostInsertion")
        self.ptedt_PostListeCommandes = QtWidgets.QPlainTextEdit(self.tab_PostInstallation)
        self.ptedt_PostListeCommandes.setEnabled(False)
        self.ptedt_PostListeCommandes.setGeometry(QtCore.QRect(0, 100, 1051, 361))
        self.ptedt_PostListeCommandes.setObjectName("ptedt_PostListeCommandes")
        self.cb_PostEpel = QtWidgets.QCheckBox(self.tab_PostInstallation)
        self.cb_PostEpel.setGeometry(QtCore.QRect(520, 10, 171, 21))
        self.cb_PostEpel.setObjectName("cb_PostEpel")
        self.cb_PostRpmFusion = QtWidgets.QCheckBox(self.tab_PostInstallation)
        self.cb_PostRpmFusion.setGeometry(QtCore.QRect(520, 40, 241, 21))
        self.cb_PostRpmFusion.setObjectName("cb_PostRpmFusion")
        self.gb_PostRpmFusion = QtWidgets.QGroupBox(self.tab_PostInstallation)
        self.gb_PostRpmFusion.setEnabled(False)
        self.gb_PostRpmFusion.setGeometry(QtCore.QRect(790, 10, 251, 61))
        self.gb_PostRpmFusion.setObjectName("gb_PostRpmFusion")
        self.rb_PostRpmFree = QtWidgets.QRadioButton(self.gb_PostRpmFusion)
        self.rb_PostRpmFree.setGeometry(QtCore.QRect(5, 20, 91, 21))
        self.rb_PostRpmFree.setObjectName("rb_PostRpmFree")
        self.bg_PostRpmFusion = QtWidgets.QButtonGroup(mw_anaconda)
        self.bg_PostRpmFusion.setObjectName("bg_PostRpmFusion")
        self.bg_PostRpmFusion.addButton(self.rb_PostRpmFree)
        self.rb_PostRpmNonFree = QtWidgets.QRadioButton(self.gb_PostRpmFusion)
        self.rb_PostRpmNonFree.setGeometry(QtCore.QRect(5, 40, 121, 21))
        self.rb_PostRpmNonFree.setObjectName("rb_PostRpmNonFree")
        self.bg_PostRpmFusion.addButton(self.rb_PostRpmNonFree)
        self.rb_PostDeux = QtWidgets.QRadioButton(self.gb_PostRpmFusion)
        self.rb_PostDeux.setGeometry(QtCore.QRect(160, 20, 81, 21))
        self.rb_PostDeux.setObjectName("rb_PostDeux")
        self.bg_PostRpmFusion.addButton(self.rb_PostDeux)
        self.tab_anacontux.addTab(self.tab_PostInstallation, "")
        mw_anaconda.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mw_anaconda)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1050, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFichiers = QtWidgets.QMenu(self.menuBar)
        self.menuFichiers.setObjectName("menuFichiers")
        self.menuA_propos = QtWidgets.QMenu(self.menuBar)
        self.menuA_propos.setObjectName("menuA_propos")
        mw_anaconda.setMenuBar(self.menuBar)
        self.actionOuvrir_un_fichier = QtWidgets.QAction(mw_anaconda)
        self.actionOuvrir_un_fichier.setObjectName("actionOuvrir_un_fichier")
        self.actionNouveau_fichier = QtWidgets.QAction(mw_anaconda)
        self.actionNouveau_fichier.setObjectName("actionNouveau_fichier")
        self.actionSauvegarder = QtWidgets.QAction(mw_anaconda)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionQuiter = QtWidgets.QAction(mw_anaconda)
        self.actionQuiter.setObjectName("actionQuiter")
        self.actionSauvegarder_sous = QtWidgets.QAction(mw_anaconda)
        self.actionSauvegarder_sous.setObjectName("actionSauvegarder_sous")
        self.actionA_propos = QtWidgets.QAction(mw_anaconda)
        self.actionA_propos.setObjectName("actionA_propos")
        self.menuFichiers.addAction(self.actionNouveau_fichier)
        self.menuFichiers.addAction(self.actionOuvrir_un_fichier)
        self.menuFichiers.addAction(self.actionSauvegarder)
        self.menuFichiers.addAction(self.actionSauvegarder_sous)
        self.menuFichiers.addSeparator()
        self.menuFichiers.addAction(self.actionQuiter)
        self.menuA_propos.addAction(self.actionA_propos)
        self.menuBar.addAction(self.menuFichiers.menuAction())
        self.menuBar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(mw_anaconda)
        self.tab_anacontux.setCurrentIndex(10)
        QtCore.QMetaObject.connectSlotsByName(mw_anaconda)

    def retranslateUi(self, mw_anaconda):
        _translate = QtCore.QCoreApplication.translate
        mw_anaconda.setWindowTitle(_translate("mw_anaconda", "Générateur de fichiers d\'auto réponse Red Hat v 1.0.0"))
        self.gb_configBase.setTitle(_translate("mw_anaconda", "Configuration avancée"))
        self.lbl_langueos.setText(_translate("mw_anaconda", "Langue du système :"))
        self.lbl_clavier.setText(_translate("mw_anaconda", "Clavier :"))
        self.lbl_fuseaux.setText(_translate("mw_anaconda", "Fuseau horaire :"))
        self.cb_gmt.setText(_translate("mw_anaconda", "Heure GMT"))
        self.cbx_langueos.setToolTip(_translate("mw_anaconda", "<html><head/><body><p>Choix de la langue du système</p></body></html>"))
        self.cbx_langueos.setItemText(0, _translate("mw_anaconda", "Anglais (UK)"))
        self.cbx_langueos.setItemText(1, _translate("mw_anaconda", "Anglais (US)"))
        self.cbx_langueos.setItemText(2, _translate("mw_anaconda", "Anglais (international)"))
        self.cbx_langueos.setItemText(3, _translate("mw_anaconda", "Allemand (Allemagne)"))
        self.cbx_langueos.setItemText(4, _translate("mw_anaconda", "Espagnol (Espagne)"))
        self.cbx_langueos.setItemText(5, _translate("mw_anaconda", "Francais (France)"))
        self.cbx_langueos.setItemText(6, _translate("mw_anaconda", "Francais (Belgique)"))
        self.cbx_langueos.setItemText(7, _translate("mw_anaconda", "Italien (Italie)"))
        self.cbx_langueos.setItemText(8, _translate("mw_anaconda", "Portugais (Portugal)"))
        self.cbx_langueos.setItemText(9, _translate("mw_anaconda", "Portugais (Brésilien)"))
        self.cbx_clavier.setToolTip(_translate("mw_anaconda", "<html><head/><body><p>Choix du type de clavier</p></body></html>"))
        self.cbx_fuseaux.setToolTip(_translate("mw_anaconda", "<html><head/><body><p>Choix du fuseau horaire ou est installée la machine.</p></body></html>"))
        self.cbx_fuseaux.setItemText(0, _translate("mw_anaconda", "Africa/Abidjan"))
        self.cbx_fuseaux.setItemText(1, _translate("mw_anaconda", "Africa/Accra"))
        self.cbx_fuseaux.setItemText(2, _translate("mw_anaconda", "America/Adak"))
        self.cbx_fuseaux.setItemText(3, _translate("mw_anaconda", "America/Anchorage"))
        self.cbx_fuseaux.setItemText(4, _translate("mw_anaconda", "Antarctica/Casey"))
        self.cbx_fuseaux.setItemText(5, _translate("mw_anaconda", "Antarctica/Davis"))
        self.cbx_fuseaux.setItemText(6, _translate("mw_anaconda", "Asia/Almaty"))
        self.cbx_fuseaux.setItemText(7, _translate("mw_anaconda", "Asia/Amman"))
        self.cbx_fuseaux.setItemText(8, _translate("mw_anaconda", "Atlantic/Azores"))
        self.cbx_fuseaux.setItemText(9, _translate("mw_anaconda", "Atlantic/Bermuda"))
        self.cbx_fuseaux.setItemText(10, _translate("mw_anaconda", "Australia/Adelaide"))
        self.cbx_fuseaux.setItemText(11, _translate("mw_anaconda", "Australia/Brisbane"))
        self.cbx_fuseaux.setItemText(12, _translate("mw_anaconda", "Europe/Berlin"))
        self.cbx_fuseaux.setItemText(13, _translate("mw_anaconda", "Europe/Brussels"))
        self.cbx_fuseaux.setItemText(14, _translate("mw_anaconda", "Europe/Monaco"))
        self.cbx_fuseaux.setItemText(15, _translate("mw_anaconda", "Europe/Paris"))
        self.cbx_fuseaux.setItemText(16, _translate("mw_anaconda", "Indian/Chagos"))
        self.cbx_fuseaux.setItemText(17, _translate("mw_anaconda", "Indian/Christmas"))
        self.cbx_fuseaux.setItemText(18, _translate("mw_anaconda", "Pacific/Apia"))
        self.cbx_fuseaux.setItemText(19, _translate("mw_anaconda", "Pacific/Auckland"))
        self.cbx_fuseaux.setItemText(20, _translate("mw_anaconda", "UTC"))
        self.gbx_PasswdRoot.setTitle(_translate("mw_anaconda", "Mot de passe root"))
        self.label.setText(_translate("mw_anaconda", "Mot de passe : "))
        self.lbl_verifPassword.setText(_translate("mw_anaconda", "Vérification : "))
        self.cb_chiffrePasswd.setText(_translate("mw_anaconda", "Chiffrer le mot de passe."))
        self.cb_affichePasswd.setText(_translate("mw_anaconda", "Afficher le mot de passe."))
        self.gb_configAvance.setTitle(_translate("mw_anaconda", "Configuration de base"))
        self.gb_distribution.setTitle(_translate("mw_anaconda", "Choix de la distribution :"))
        self.rb_centos7.setText(_translate("mw_anaconda", "Centos 7.X"))
        self.rb_centos8.setText(_translate("mw_anaconda", "Centos 8.X"))
        self.rb_fedora.setText(_translate("mw_anaconda", "Fedora 3X server"))
        self.rb_c7netinstall.setText(_translate("mw_anaconda", "Centos 7.x netinstall"))
        self.rb_c8netinstall.setText(_translate("mw_anaconda", "Centos 8.x netinstall"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_2), _translate("mw_anaconda", "Config base"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_installation), _translate("mw_anaconda", "Installation"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_boot), _translate("mw_anaconda", "Boot"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_partitions), _translate("mw_anaconda", "Partitions"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_reseau), _translate("mw_anaconda", "Reseau"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_authentification), _translate("mw_anaconda", "Authentification"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_PareFeu), _translate("mw_anaconda", "Pare-feu"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_affichage), _translate("mw_anaconda", "Affichage"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_packages), _translate("mw_anaconda", "Packages"))
        self.gb_InterpreteurPreInstall.setTitle(_translate("mw_anaconda", "Choisir un interpréteur"))
        self.rb_PreAucun.setText(_translate("mw_anaconda", "Aucun"))
        self.rb_PreBash.setText(_translate("mw_anaconda", "Bash"))
        self.rb_PrePython2.setText(_translate("mw_anaconda", "Python 2"))
        self.rb_PrePython3.setText(_translate("mw_anaconda", "Python 3"))
        self.rb_PrePerl.setText(_translate("mw_anaconda", "Perl"))
        self.rb_PreAutre.setText(_translate("mw_anaconda", "Autre"))
        self.lbl_PreInsertion.setText(_translate("mw_anaconda", "Inserez ici la liste vos commandes de pré installation."))
        self.gb_PreRpmFusion.setTitle(_translate("mw_anaconda", "Dépots RPM Fusion"))
        self.rb_PreRpmFree.setText(_translate("mw_anaconda", "Dépot free"))
        self.rb_PreRpmNonFree.setText(_translate("mw_anaconda", "Dépot non free"))
        self.rb_PreDeux.setText(_translate("mw_anaconda", "Les deux"))
        self.cb_PreEpel.setText(_translate("mw_anaconda", "Installer le dépot EPEL."))
        self.cb_PreRpmFusion.setText(_translate("mw_anaconda", "Installer le(s) dépot(s) RPM fusion"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_PreInstallation), _translate("mw_anaconda", "Pré-installation"))
        self.gb_InterpreteurPostInstall.setTitle(_translate("mw_anaconda", "Choisir un interpréteur"))
        self.rb_PostAucun.setText(_translate("mw_anaconda", "Aucun"))
        self.rb_PostBash.setText(_translate("mw_anaconda", "Bash"))
        self.rb_PostPython2.setText(_translate("mw_anaconda", "Python 2"))
        self.rb_PostPython3.setText(_translate("mw_anaconda", "Python 3"))
        self.rb_PostPerl.setText(_translate("mw_anaconda", "Perl"))
        self.rb_PostAutre.setText(_translate("mw_anaconda", "Autre"))
        self.lbl_PostInsertion.setText(_translate("mw_anaconda", "Inserez ici la liste vos commandes de post installation."))
        self.cb_PostEpel.setText(_translate("mw_anaconda", "Installer le dépot EPEL."))
        self.cb_PostRpmFusion.setText(_translate("mw_anaconda", "Installer le(s) dépot(s) RPM fusion"))
        self.gb_PostRpmFusion.setTitle(_translate("mw_anaconda", "Dépots RPM Fusion"))
        self.rb_PostRpmFree.setText(_translate("mw_anaconda", "Dépot free"))
        self.rb_PostRpmNonFree.setText(_translate("mw_anaconda", "Dépot non free"))
        self.rb_PostDeux.setText(_translate("mw_anaconda", "Les deux"))
        self.tab_anacontux.setTabText(self.tab_anacontux.indexOf(self.tab_PostInstallation), _translate("mw_anaconda", "Post-installation"))
        self.menuFichiers.setTitle(_translate("mw_anaconda", "Fichiers"))
        self.menuA_propos.setTitle(_translate("mw_anaconda", "Aide"))
        self.actionOuvrir_un_fichier.setText(_translate("mw_anaconda", "Ouvrir un fichier"))
        self.actionOuvrir_un_fichier.setShortcut(_translate("mw_anaconda", "Ctrl+O"))
        self.actionNouveau_fichier.setText(_translate("mw_anaconda", "Nouveau fichier"))
        self.actionNouveau_fichier.setShortcut(_translate("mw_anaconda", "Ctrl+N"))
        self.actionSauvegarder.setText(_translate("mw_anaconda", "Sauvegarder"))
        self.actionSauvegarder.setShortcut(_translate("mw_anaconda", "Ctrl+S"))
        self.actionQuiter.setText(_translate("mw_anaconda", "Quiter"))
        self.actionQuiter.setShortcut(_translate("mw_anaconda", "Ctrl+Q"))
        self.actionSauvegarder_sous.setText(_translate("mw_anaconda", "Sauvegarder sous"))
        self.actionSauvegarder_sous.setShortcut(_translate("mw_anaconda", "Ctrl+Shift+S"))
        self.actionA_propos.setText(_translate("mw_anaconda", "A propos"))
        self.actionA_propos.setShortcut(_translate("mw_anaconda", "F1"))

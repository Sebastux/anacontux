from PyQt5.QtWidgets import QMessageBox


def AfficheMessages(titre, texte, icone, boutons):
    msgBox = QMessageBox()
    msgBox.setIcon(icone)
    msgBox.setText(texte)
    msgBox.setWindowTitle(titre)
    msgBox.setStandardButtons(boutons)
    msgBox.exec()

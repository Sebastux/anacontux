from PyQt5.QtWidgets import QMessageBox


def AfficheMessages(titre, texte, icone, boutons):
    msgBox = QMessageBox()
    msgBox.setIcon(icone)
    msgBox.setText(texte)
    msgBox.setWindowTitle(titre)
    msgBox.setStandardButtons(boutons)
    msgBox.exec()

"""
Liste des icones :
QMessageBox.Information
QMessageBox.Question
QMessageBox.Warning
QMessageBox.Critical

Liste des boutons :
QMessageBox.Cancel
QMessageBox.Ok
QMessageBox.Help
QMessageBox.Open
QMessageBox.Save
QMessageBox.SaveAll
QMessageBox.Discard
QMessageBox.Close
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.NoButton
QMessageBox.RestoreDefaults
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore

Pour mettre plusieurs boutons, il suffit de les chainer et de les séparé par un pipe.
"""

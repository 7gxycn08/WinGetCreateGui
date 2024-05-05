# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget, QFileDialog, QMessageBox)
import sys
import yaml

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setFocus()
        Dialog.setFixedSize(503, 694)
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(503, 694)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Resources/app.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        self.exception_messege = None
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.installer_url_entry = QLineEdit(Dialog)
        self.installer_url_entry.setObjectName(u"installer_url_entry")
        self.installer_url_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.installer_url_entry, 19, 0, 1, 1)

        self.installer_url_label = QLabel(Dialog)
        self.installer_url_label.setObjectName(u"installer_url_label")

        self.gridLayout.addWidget(self.installer_url_label, 18, 0, 1, 1)

        self.installer_type_entry = QLineEdit(Dialog)
        self.installer_type_entry.setObjectName(u"installer_type_entry")
        self.installer_type_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.installer_type_entry, 17, 0, 1, 1)

        self.installer_sha_label = QLabel(Dialog)
        self.installer_sha_label.setObjectName(u"installer_sha_label")

        self.gridLayout.addWidget(self.installer_sha_label, 20, 0, 1, 1)

        self.package_name_entry = QLineEdit(Dialog)
        self.package_name_entry.setObjectName(u"package_name_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.package_name_entry.sizePolicy().hasHeightForWidth())
        self.package_name_entry.setSizePolicy(sizePolicy1)
        self.package_name_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.package_name_entry, 1, 0, 1, 1)

        self.license_entry = QLineEdit(Dialog)
        self.license_entry.setObjectName(u"license_entry")
        self.license_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.license_entry, 13, 0, 1, 1)

        self.publisher_id_entry = QLineEdit(Dialog)
        self.publisher_id_entry.setObjectName(u"publisher_id_entry")
        sizePolicy1.setHeightForWidth(self.publisher_id_entry.sizePolicy().hasHeightForWidth())
        self.publisher_id_entry.setSizePolicy(sizePolicy1)
        self.publisher_id_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.publisher_id_entry, 5, 0, 1, 1)

        self.package_version_entry = QLineEdit(Dialog)
        self.package_version_entry.setObjectName(u"package_version_entry")
        sizePolicy1.setHeightForWidth(self.package_version_entry.sizePolicy().hasHeightForWidth())
        self.package_version_entry.setSizePolicy(sizePolicy1)
        self.package_version_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.package_version_entry, 7, 0, 1, 1)

        self.publisher_id_label = QLabel(Dialog)
        self.publisher_id_label.setObjectName(u"publisher_id_label")
        self.publisher_id_label.setTextFormat(Qt.TextFormat.PlainText)
        self.publisher_id_label.setScaledContents(False)

        self.gridLayout.addWidget(self.publisher_id_label, 4, 0, 1, 1)

        self.locale_label = QLabel(Dialog)
        self.locale_label.setObjectName(u"locale_label")

        self.gridLayout.addWidget(self.locale_label, 10, 0, 1, 1)

        self.arch_list = QListWidget(Dialog)
        QListWidgetItem(self.arch_list)
        QListWidgetItem(self.arch_list)
        QListWidgetItem(self.arch_list)
        QListWidgetItem(self.arch_list)
        self.arch_list.setObjectName(u"arch_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.arch_list.sizePolicy().hasHeightForWidth())
        self.arch_list.setSizePolicy(sizePolicy2)
        self.arch_list.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.arch_list.setAutoFillBackground(False)
        self.arch_list.setFlow(QListView.Flow.TopToBottom)
        self.arch_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.arch_list.setViewMode(QListView.ViewMode.ListMode)
        self.arch_list.setWordWrap(False)
        self.arch_list.setSelectionRectVisible(False)
        self.arch_list.setSortingEnabled(False)

        self.gridLayout.addWidget(self.arch_list, 15, 0, 1, 1)

        self.locale_entry = QLineEdit(Dialog)
        self.locale_entry.setObjectName(u"locale_entry")
        self.locale_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.locale_entry, 11, 0, 1, 1)

        self.arch_label = QLabel(Dialog)
        self.arch_label.setObjectName(u"arch_label")

        self.gridLayout.addWidget(self.arch_label, 14, 0, 1, 1)

        self.license_label = QLabel(Dialog)
        self.license_label.setObjectName(u"license_label")

        self.gridLayout.addWidget(self.license_label, 12, 0, 1, 1)

        self.generate_button = QPushButton(Dialog)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.clicked.connect(self.generate_yaml)

        self.gridLayout.addWidget(self.generate_button, 22, 0, 1, 1)

        self.description_entry = QPlainTextEdit(Dialog)
        self.description_entry.setObjectName(u"description_entry")

        self.gridLayout.addWidget(self.description_entry, 9, 0, 1, 1)

        self.package_version_label = QLabel(Dialog)
        self.package_version_label.setObjectName(u"package_version_label")

        self.gridLayout.addWidget(self.package_version_label, 6, 0, 1, 1)

        self.package_name_label = QLabel(Dialog)
        self.package_name_label.setObjectName(u"package_name_label")
        self.package_name_label.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.package_name_label, 0, 0, 1, 1)

        self.publisher_entry = QLineEdit(Dialog)
        self.publisher_entry.setObjectName(u"publisher_entry")
        sizePolicy1.setHeightForWidth(self.publisher_entry.sizePolicy().hasHeightForWidth())
        self.publisher_entry.setSizePolicy(sizePolicy1)
        self.publisher_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.publisher_entry, 3, 0, 1, 1)

        self.installer_type_label = QLabel(Dialog)
        self.installer_type_label.setObjectName(u"installer_type_label")

        self.gridLayout.addWidget(self.installer_type_label, 16, 0, 1, 1)

        self.installer_sha_entry = QLineEdit(Dialog)
        self.installer_sha_entry.setObjectName(u"installer_sha_entry")
        self.installer_sha_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.installer_sha_entry, 21, 0, 1, 1)

        self.description_label = QLabel(Dialog)
        self.description_label.setObjectName(u"description_label")

        self.gridLayout.addWidget(self.description_label, 8, 0, 1, 1)

        self.publisher_label = QLabel(Dialog)
        self.publisher_label.setObjectName(u"publisher_label")

        self.gridLayout.addWidget(self.publisher_label, 2, 0, 1, 1)


        self.retranslateUi(Dialog)
        Dialog.setTabOrder(self.package_name_entry, self.publisher_entry)
        Dialog.setTabOrder(self.publisher_entry, self.publisher_id_entry)
        Dialog.setTabOrder(self.publisher_id_entry, self.package_version_entry)
        Dialog.setTabOrder(self.package_version_entry, self.description_entry)
        Dialog.setTabOrder(self.description_entry, self.locale_entry)
        Dialog.setTabOrder(self.locale_entry, self.license_entry)
        Dialog.setTabOrder(self.license_entry, self.arch_list)
        Dialog.setTabOrder(self.arch_list, self.installer_type_entry)
        Dialog.setTabOrder(self.installer_type_entry, self.installer_url_entry)
        Dialog.setTabOrder(self.installer_url_entry, self.installer_sha_entry)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"WinGetCreateGui v1.0",
                                                         None))
        self.installer_url_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                    u"# Path to download installation file.", None))
        self.installer_url_label.setText(QCoreApplication.translate("Dialog", u"Installer Url:",
                                                                    None))
        self.installer_type_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
        u"# Enumeration of supported installer types (exe, msi, msix, inno, wix, nullsoft, appx).",
                                                                                None))
        self.installer_sha_label.setText(QCoreApplication.translate("Dialog", u"Installer Sha256:",
                                                                    None))
#if QT_CONFIG(accessibility)
        self.package_name_entry.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.package_name_entry.setText("")
        self.package_name_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                              u"# The name of the application.",
                                                                              None))
        self.license_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                         u"# The license of the application.",
                                                                         None))
        self.publisher_id_entry.setText("")
        self.publisher_id_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                              u"# Publisher.package format.",
                                                                              None))
        self.package_version_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                                 u"# Version numbering format.",
                                                                                 None))
        self.publisher_id_label.setText(QCoreApplication.translate("Dialog",
                                                                   u"Package Identifier:", None))
        self.locale_label.setText(QCoreApplication.translate("Dialog",
                                                             u"Package Locale:", None))

        __sortingEnabled = self.arch_list.isSortingEnabled()
        self.arch_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.arch_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"x64", None));
        ___qlistwidgetitem1 = self.arch_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"x86", None));
        ___qlistwidgetitem2 = self.arch_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"arm", None));
        ___qlistwidgetitem3 = self.arch_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"arm64", None));
        self.arch_list.setSortingEnabled(__sortingEnabled)

        self.locale_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                        u"# BCP 47 format (e.g. en-US)",
                                                                        None))
        self.arch_label.setText(QCoreApplication.translate("Dialog", u"Architecture:", None))
        self.license_label.setText(QCoreApplication.translate("Dialog", u"License:", None))
        self.generate_button.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.description_entry.setPlainText("")
        self.description_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                        u"# The description of the application.",
                                                                             None))
        self.package_version_label.setText(QCoreApplication.translate("Dialog",
                                                                      u"Package Version:", None))
        self.package_name_label.setText(QCoreApplication.translate("Dialog", u"Package Name:",
                                                                   None))
        self.publisher_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                           u"# The name of the publisher.",
                                                                           None))
        self.installer_type_label.setText(QCoreApplication.translate("Dialog",
                                                                     u"Installer Type:", None))
        self.installer_sha_entry.setPlaceholderText(QCoreApplication.translate("Dialog",
                                                                u"# SHA256 calculated from installer.",
                                                                               None))
        self.description_label.setText(QCoreApplication.translate("Dialog",
                                                                  u"Short Description:", None))
        self.publisher_label.setText(QCoreApplication.translate("Dialog", u"Publisher:", None))
    # retranslateUi

    def exception_messege_box(self):
        message_box = QMessageBox()
        message_box.setWindowIcon(QIcon(r"Resources\app.png"))
        message_box.setIcon(QMessageBox.Icon.Critical)
        message_box.setWindowTitle("Error")
        message_box.setText(f"{self.exception_messege}")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()
    def generate_yaml(self):
        project_name = self.package_name_entry.text()
        publisher_name = self.publisher_entry.text()
        package_version = self.package_version_entry.text()
        description = self.description_entry.toPlainText()
        package_locale = self.locale_entry.text()
        license_name = self.license_entry.text()
        try:
            arch_type = self.arch_list.currentItem().text()
            if arch_type == None:
                arch_type = ""
        except AttributeError or UnboundLocalError:
            self.exception_messege = "Select Architecture Type."
            self.exception_messege_box()
            return

        installer_type = self.installer_type_entry.text()
        installer_url = self.installer_url_entry.text()
        installer_sha256 = self.installer_sha_entry.text()

        data = {
            'PackageIdentifier': f'{publisher_name}.{project_name}',
            'PackageVersion': f'{package_version}',
            'PackageLocale': f'{package_locale}',
            'Publisher': f'{publisher_name}',
            'PackageName': f'{project_name}',
            'License': f'{license_name}',
            'ShortDescription': f'{description}',
            'Installers': [
                {
                    'Architecture': f'{arch_type}',
                    'InstallerType': f'{installer_type}',
                    'InstallerUrl': f'{installer_url}',
                    'InstallerSha256': f'{installer_sha256}',
                }
            ],
            'ManifestType': 'singleton',
            'ManifestVersion': '1.6.0'
        }

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("YAML files (*.yaml)")

        default_name = f'{project_name}.{publisher_name}.yaml'
        file_dialog.selectFile(default_name)

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            with open(selected_file, 'w') as file:
                yaml.dump(data, file, sort_keys=False)

def main():
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


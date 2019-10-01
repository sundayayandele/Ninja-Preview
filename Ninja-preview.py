# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import QCoreApplication, QSettings
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from preview import Preview

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

qApp.setWindowIcon(QIcon("./UI/icons/logo.ico"))

engine = QQmlApplicationEngine()

preview = Preview()

engine.rootContext().setContextProperty('preview', preview)

engine.load('UI/main.qml')

engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, subprocess

#Определение домашней папки пользователя
HOMEFOLDER = os.getenv('HOME')

#Директория в домашней папке пользователя для хранения настроек и подключений
WORKFOLDER = HOMEFOLDER + '/.connector/'

#Установки по умолчанию для параметров программы (какие приложения использовать)
DEFAULT = dict(RDP = 1, VNC = 0, TAB = '0') 

#Версия приложения
VERSION = "1.3.24"
RELEASE = subprocess.check_output("rpm -q connector; exit 0", shell=True, universal_newlines=True).strip().split('-') [2]

#Исходные данные для ярлыка подключения
DESKTOP_INFO ="""#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=/usr/share/connector/data/emblem.png
"""

#Запускаемый файл приложения
EXEC = "/usr/bin/connector "

#Проверка и установка пути монтирования устройств
#control udisks2
udisks2 = subprocess.check_output("/usr/sbin/control udisks2; exit 0", shell=True, universal_newlines=True).strip()
if udisks2 == 'default':
    USBPATH = "/run/media/$USER"
if udisks2 == 'shared':
    USBPATH = "/media"

#Ведение логов
LOGFOLDER = WORKFOLDER + "logs/"
STD_TO_LOG = ' >> ' + LOGFOLDER + "all.log 2>&1 &"

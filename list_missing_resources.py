#!/usr/bin/env python
#
# Quick to detect missing files from Android project definition
#
# Author: info@rickvanderzwet.nl
# Licence: BSD
#

from lxml import etree
import pathlib

basedir = pathlib.Path('./Source/DigiD.Droid')

root = etree.XML(open(basedir / pathlib.Path('DigiD.Droid.csproj'),'rb').read())
for ar in root.iterfind('.//{http://schemas.microsoft.com/developer/msbuild/2003}AndroidResource'):
	filepath = ar.get('Include')
	file = pathlib.Path(basedir / pathlib.Path(filepath))
	print(file, file.exists(), file.suffix)


# Possible dummy replacements for missing XML files (just to get the application to build...):
# - https://gist.githubusercontent.com/teoinke/097f3231f8445c3e3b3b/raw/2c80456aa48e45d6503fa69c46f84025ecac1de7/shake.xml
# - https://raw.githubusercontent.com/bazelbuild/examples/main/android/ndk/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml
# - https://raw.githubusercontent.com/persian-calendar/persian-calendar/847255fb80c7d8f3f8fb4aed73d9b4b134c159a5/PersianCalendar/src/main/res/drawable/popup_background.xml



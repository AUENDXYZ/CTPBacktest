# --coding:utf-8--
import qdarkstyle
from qdarkstyle.light.palette import LightPalette


STYLESHEET = qdarkstyle.load_stylesheet(qt_api='pyside6')
STYLESHEET_LIGHT = qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette())
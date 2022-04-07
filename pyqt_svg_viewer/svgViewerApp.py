from PyQt5.QtWidgets import QApplication
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_style_setter import StyleSetter

from pyqt_svg_viewer.svgViewer import SvgViewer


class SvgViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = SvgViewer()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/svg.svg')
        self.__titleBarWindow.show()
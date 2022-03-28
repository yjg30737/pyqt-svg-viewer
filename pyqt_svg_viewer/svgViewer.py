from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqt_style_setter import StyleSetter

from pyqt_svg_viewer.svgViewerWidget import SvgViewerWidget


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__view = SvgViewerWidget()
        self.setCentralWidget(self.__view)

    def setSvgFile(self, filename: str):
        self.__view.setSvgFile(filename)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    svgViewer = SvgViewer()
    svgViewer.show()
    StyleSetter.setWindowStyle(svgViewer)
    sys.exit(app.exec_())




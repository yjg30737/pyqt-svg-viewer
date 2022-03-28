from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqt_style_setter import StyleSetter

from svgViewerWidget import SvgViewerWidget


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = SvgViewerWidget()
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    svgViewer = SvgViewer()
    svgViewer.show()
    StyleSetter.setWindowStyle(svgViewer)
    sys.exit(app.exec_())




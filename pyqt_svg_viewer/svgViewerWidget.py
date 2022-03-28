from PyQt5.QtSvg import QSvgWidget
from pyqt_viewer_widget import ViewerWidget


class SvgViewerWidget(ViewerWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = QSvgWidget()
        self.setView(mainWidget)

    def setSvgFile(self, filename: str):
        widget = self.getView()
        widget.load(filename)


from pyqt_viewer_widget import ViewerWidget

from pyqt_svg_viewer.SvgViewerView import SvgViewerView


class SvgViewerWidget(ViewerWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = SvgViewerView()
        self.setView(mainWidget)


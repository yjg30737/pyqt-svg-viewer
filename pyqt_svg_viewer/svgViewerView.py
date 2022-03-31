from PyQt5.QtSvg import QSvgWidget


class SvgViewerView(QSvgWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setFilename(self, filename: str):
        self.load(filename)
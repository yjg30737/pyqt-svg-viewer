from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QTextEdit, QLabel
from pyqt_svg_button import SvgButton

from simplePyQt5.topLeftRightWidget import TopLeftRightWidget


class SourceWidget(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__srcCodeTextEdit = QTextEdit()
        self.__srcCodeTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeBtn = SvgButton(self)
        closeBtn.clicked.connect(self.close)
        closeBtn.setToolTip('Close')
        closeBtn.setIcon('ico/close.svg')

        mainWidget = TopLeftRightWidget()
        mainWidget.setLeftWidgets([QLabel('Source')])
        mainWidget.setRightWidgets([closeBtn])
        mainWidget.addBottomWidget(self.__srcCodeTextEdit)
        lay = mainWidget.layout()
        lay.setContentsMargins(5, 5, 5, 5)

        self.setLayout(lay)

    def setSourceOfFile(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            self.__srcCodeTextEdit.setPlainText(contents)

    def close(self):
        self.closeSignal.emit()
        super().close()
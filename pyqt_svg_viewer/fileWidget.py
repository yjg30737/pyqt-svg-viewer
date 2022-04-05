from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QCheckBox, QLabel

from pyqt_checkbox_file_list_widget.checkBoxFileListWidget import CheckBoxFileListWidget
from pyqt_svg_icon_pushbutton import SvgIconPushButton
from simplePyQt5 import VerticalWidget, LeftRightWidget
from simplePyQt5.topLeftRightWidget import TopLeftRightWidget


class FileWidget(QWidget):
    showSignal = pyqtSignal(int)
    removeSignal = pyqtSignal(list)
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        closeBtn = SvgIconPushButton()
        closeBtn.setIcon('ico/close.svg')
        closeBtn.clicked.connect(self.close)

        closeBtn.setToolTip('Close')

        self.__allChkBox = QCheckBox('Check all')
        self.__onlyFileNameChkBox = QCheckBox('Show filename only')

        self.__removeBtn = SvgIconPushButton()
        self.__removeBtn.setIcon('ico/remove.svg')
        self.__removeBtn.setToolTip('Remove')
        self.__removeBtn.clicked.connect(self.__remove)

        self.__fileListWidget = CheckBoxFileListWidget()
        self.__fileListWidget.checkedSignal.connect(self.__btnToggled)
        self.__fileListWidget.itemDoubleClicked.connect(self.__showSignal)
        self.__fileListWidget.itemActivated.connect(self.__showSignal)

        topWidget = LeftRightWidget()
        topWidget.setLeftWidgets([QLabel('List of files')])
        topWidget.setRightWidgets([closeBtn])

        bottomWidget = TopLeftRightWidget()
        bottomWidget.setLeftWidgets([self.__allChkBox, self.__onlyFileNameChkBox])
        bottomWidget.setRightWidgets([self.__removeBtn])
        bottomWidget.addBottomWidget(self.__fileListWidget)

        self.__allChkBox.stateChanged.connect(self.__fileListWidget.toggleState)

        self.__onlyFileNameChkBox.stateChanged.connect(self.__fileListWidget.setFilenameOnly)

        mainWidget = VerticalWidget()
        mainWidget.addWidgets([topWidget, bottomWidget])
        lay = mainWidget.layout()
        lay.setContentsMargins(0, 0, 1, 0)
        self.setLayout(lay)

        self.__chkToggled()
        self.__btnToggled()

    def __chkToggled(self):
        f = self.__fileListWidget.count() > 0
        self.__allChkBox.setEnabled(f)
        self.__onlyFileNameChkBox.setEnabled(f)

    def __btnToggled(self):
        f = len(self.__fileListWidget.getCheckedRows()) > 0
        self.__removeBtn.setEnabled(f)

    def setCurrentItem(self, idx: int):
        self.__fileListWidget.setCurrentItem(self.__fileListWidget.item(idx))

    def setFilenames(self, filenames: list, idx=0):
        self.__fileListWidget.setFilenames(filenames, idx)
        self.__chkToggled()

    def __showSignal(self, item):
        r = self.__fileListWidget.row(item)
        self.showSignal.emit(r)

    def getItem(self, i):
        return self.__fileListWidget.item(i)

    def __remove(self):
        filenames_to_remove_from_list = self.__fileListWidget.getCheckedFilenames()
        self.__fileListWidget.removeCheckedRows()
        self.removeSignal.emit(filenames_to_remove_from_list)
        self.__allChkBox.setChecked(False)

        self.__chkToggled()
        self.__btnToggled()

    def close(self):
        self.closeSignal.emit()
        super().close()

from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidgetAction
from pyqt_svg_icon_pushbutton import SvgIconPushButton
from pyqt_description_tooltip import DescriptionToolTipGetter

from pyqt_svg_viewer.svgViewerWidget import SvgViewerWidget


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__view = SvgViewerWidget()
        self.setCentralWidget(self.__view)

        self.__setActions()
        self.__setToolBar()

    def setSvgFile(self, filename: str):
        self.__view.setSvgFile(filename)

    def __setActions(self):
        self.__loadFileAction = QWidgetAction(self)
        self.__loadFileBtn = SvgIconPushButton(self)
        self.__loadFileBtn.setIcon('ico/add_file.svg')
        self.__loadFileBtn.setShortcut('Ctrl+O')
        self.__loadFileBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Open Files',
                                                                          shortcut='Ctrl+O'))
        self.__loadFileBtn.clicked.connect(self.__loadFile)
        self.__loadFileAction.setDefaultWidget(self.__loadFileBtn)

        self.__loadDirAction = QWidgetAction(self)
        self.__loadDirBtn = SvgIconPushButton(self)
        self.__loadDirBtn.setIcon('ico/add_dir.svg')
        self.__loadDirBtn.setShortcut('Ctrl+Shift+O')
        self.__loadDirBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Open Directory',
                                                                         shortcut='Ctrl+Shift+O'))
        self.__loadDirBtn.clicked.connect(self.__loadDir)
        self.__loadDirAction.setDefaultWidget(self.__loadDirBtn)

        self.__showNavigationToolbarAction = QWidgetAction(self)
        self.__showNavigationToolbarBtn = SvgIconPushButton(self)
        self.__showNavigationToolbarBtn.setIcon('ico/navigation_bar.svg')
        self.__showNavigationToolbarBtn.setCheckable(True)
        self.__showNavigationToolbarBtn.setChecked(True)
        self.__showNavigationToolbarBtn.setShortcut('Ctrl+B')
        self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide Navigation Bar',
                                                                                       shortcut='Ctrl+B'))
        self.__showNavigationToolbarBtn.toggled.connect(self.__showNavigationToolbar)
        self.__showNavigationToolbarAction.setDefaultWidget(self.__showNavigationToolbarBtn)

        self.__fullScreenToggleAction = QWidgetAction(self)
        self.__fullScreenToggleBtn = SvgIconPushButton(self)
        self.__fullScreenToggleBtn.setIcon('ico/full_screen.svg')
        self.__fullScreenToggleBtn.setCheckable(True)
        self.__fullScreenToggleBtn.setShortcut('F11')
        self.__fullScreenToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show As Full Screen',
                                                                                  shortcut='F11'))
        self.__fullScreenToggleBtn.toggled.connect(self.__fullScreenToggle)
        self.__fullScreenToggleAction.setDefaultWidget(self.__fullScreenToggleBtn)

    def __setToolBar(self):
        toolbar = QToolBar()
        toolbar.addAction(self.__loadFileAction)
        toolbar.addAction(self.__loadDirAction)
        toolbar.addAction(self.__htmlFileListToggleAction)
        toolbar.addAction(self.__showNavigationToolbarAction)
        toolbar.addAction(self.__srcWidgetToggleAction)
        toolbar.addAction(self.__fullScreenToggleAction)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet('QToolBar { background-color: #888; }')




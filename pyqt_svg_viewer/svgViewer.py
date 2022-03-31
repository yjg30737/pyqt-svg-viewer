import os, posixpath

from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidgetAction, QFileDialog
from pyqt_svg_icon_pushbutton import SvgIconPushButton
from pyqt_description_tooltip import DescriptionToolTipGetter

from pyqt_svg_viewer.svgViewerWidget import SvgViewerWidget


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('SVG Viewer')
        self.__viewerWidget = SvgViewerWidget()
        self.__viewerWidget.setExtensionsExceptForImage(['.svg'])
        self.setCentralWidget(self.__viewerWidget)

        self.__setActions()
        self.__setToolBar()

    def setSvgFile(self, filename: str):
        self.__viewerWidget.setSvgFile(filename)

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
        toolbar.addAction(self.__showNavigationToolbarAction)
        toolbar.addAction(self.__fullScreenToggleAction)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet('QToolBar { background-color: #888; }')

    def __fullScreenToggle(self, f):
        if f:
            self.showFullScreen()
        else:
            self.showNormal()

    def __loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Files', '', "SVG Files (*.svg)")
        if filename[0]:
            filename = filename[0]
            dirname = os.path.dirname(filename)
            self.__setSvgFilesOfDirectory(dirname, filename)

    def __loadDir(self):
        dirname = QFileDialog.getExistingDirectory(self, 'Open Directory', '', QFileDialog.ShowDirsOnly)
        if dirname:
            self.__setSvgFilesOfDirectory(dirname)

    def __setSvgFilesOfDirectory(self, dirname, cur_filename=''):
        filenames = [os.path.join(dirname, filename).replace(os.path.sep, posixpath.sep) for filename in
                     os.listdir(dirname)
                     if os.path.splitext(filename)[-1] == '.svg']
        if filenames:
            if cur_filename:
                pass
            else:
                cur_filename = filenames[0]
            cur_file_idx = filenames.index(cur_filename)
            self.__viewerWidget.setFilenames(filenames, cur_filename=cur_filename)

    def __showNavigationToolbar(self, f):
        self.__showNavigationToolbarBtn.setChecked(f)
        self.__viewerWidget.setBottomWidgetVisible(f)
        if f:
            self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide navigation bar',
                                                                                           shortcut='Ctrl+B'))
        else:
            self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show navigation bar',
                                                                                           shortcut='Ctrl+B'))

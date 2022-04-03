import os, posixpath

from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidgetAction, QFileDialog, QSplitter, QGridLayout, QWidget
from pyqt_svg_icon_pushbutton import SvgIconPushButton
from pyqt_description_tooltip import DescriptionToolTipGetter

from pyqt_svg_viewer.fileWidget import FileWidget
from pyqt_svg_viewer.sourceWidget import SourceWidget
from pyqt_svg_viewer.svgViewerWidget import SvgViewerWidget


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('SVG Viewer')

        self.__viewerWidget = SvgViewerWidget()
        self.__viewerWidget.prevSignal.connect(self.__selectCurrentFileItemInList)
        self.__viewerWidget.nextSignal.connect(self.__selectCurrentFileItemInList)
        self.__viewerWidget.closeSignal.connect(self.__showNavigationToolbar)
        self.__viewerWidget.setExtensionsExceptForImage(['.svg'])

        self.__srcWidget = SourceWidget()
        self.__srcWidget.closeSignal.connect(self.__srcWidgetBtnToggled)

        self.__fileListWidget = FileWidget()
        self.__fileListWidget.showSignal.connect(self.__showFileToViewer)
        self.__fileListWidget.showSignal.connect(self.__showSource)
        self.__fileListWidget.removeSignal.connect(self.__removeSomeFilesFromViewer)
        self.__fileListWidget.closeSignal.connect(self.__fileListWidgetBtnToggled)

        splitter = QSplitter()
        splitter.addWidget(self.__fileListWidget)
        splitter.addWidget(self.__viewerWidget)
        splitter.addWidget(self.__srcWidget)
        splitter.setSizes([200, 400, 200])
        splitter.setChildrenCollapsible(False)

        lay = QGridLayout()
        lay.addWidget(splitter)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.__fileListWidget.hide()
        self.__srcWidget.hide()

        self.setCentralWidget(mainWidget)

        self.__setActions()
        self.__setToolBar()

    def __showFileToViewer(self, r):
        self.__viewerWidget.setCurrentIndex(r)

    def __showSource(self, r):
        item = self.__fileListWidget.getItem(r)
        if item:
            filename = item.text()
            self.__srcWidget.setSourceOfFile(filename)

    def __removeSomeFilesFromViewer(self, filenames: list):
        self.__viewerWidget.removeSomeFilesFromViewer(filenames)
        self.__selectCurrentFileItemInList()

    def __selectCurrentFileItemInList(self):
        idx = self.__viewerWidget.getCurrentIndex()
        self.__fileListWidget.setCurrentItem(idx)
        self.__showSource(idx)
        self.__viewerWidget.setFocus()

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

        self.__fileListToggleAction = QWidgetAction(self)
        self.__fileListToggleBtn = SvgIconPushButton(self)
        self.__fileListToggleBtn.setIcon('ico/list.svg')
        self.__fileListToggleBtn.setCheckable(True)
        self.__fileListToggleBtn.setShortcut('Ctrl+L')
        self.__fileListToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show File List',
                                                                                shortcut='Ctrl+L'))
        self.__fileListToggleBtn.toggled.connect(self.__fileListToggle)
        self.__fileListToggleAction.setDefaultWidget(self.__fileListToggleBtn)

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

        self.__srcWidgetToggleAction = QWidgetAction(self)
        self.__srcWidgetToggleBtn = SvgIconPushButton(self)
        self.__srcWidgetToggleBtn.setIcon('ico/source.svg')
        self.__srcWidgetToggleBtn.setCheckable(True)
        self.__srcWidgetToggleBtn.setShortcut('Ctrl+S')
        self.__srcWidgetToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show Source Browser',
                                                                                 shortcut='Ctrl+S'))
        self.__srcWidgetToggleBtn.toggled.connect(self.__srcWidgetToggle)
        self.__srcWidgetToggleAction.setDefaultWidget(self.__srcWidgetToggleBtn)

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
        toolbar.addAction(self.__fileListToggleAction)
        toolbar.addAction(self.__showNavigationToolbarAction)
        toolbar.addAction(self.__srcWidgetToggleAction)
        toolbar.addAction(self.__fullScreenToggleAction)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet('QToolBar { background-color: #888; }')

    def __srcWidgetToggle(self):
        if self.__srcWidget.isHidden():
            self.__srcWidget.show()
            self.__srcWidgetToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide source browser',
                                                                                     shortcut='Ctrl+S'))
        else:
            self.__srcWidget.hide()
            self.__srcWidgetToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show source browser',
                                                                                     shortcut='Ctrl+S'))

    def __fileListToggle(self, f):
        if f:
            self.__fileListWidget.show()
            self.__fileListToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide File List',
                                                                                    shortcut='Ctrl+L'))
        else:
            self.__fileListWidget.hide()
            self.__fileListToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show File List',
                                                                                    shortcut='Ctrl+L'))

    def __fullScreenToggle(self, f):
        if f:
            self.showFullScreen()
        else:
            self.showNormal()

    def __fileListWidgetBtnToggled(self):
        self.__fileListToggleBtn.setChecked(self.__fileListWidget.isHidden())

    def __srcWidgetBtnToggled(self):
        self.__srcWidgetToggleBtn.setChecked(self.__srcWidget.isHidden())

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

import os

from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidgetAction, QFileDialog, QSplitter, QGridLayout, QWidget
from pyqt_svg_button import SvgButton
from pyqt_description_tooltip import DescriptionToolTipGetter

from pyqt_svg_viewer.sourceWidget import SourceWidget

from pyqt_list_viewer_widget.listViewerWidget import ListViewerWidget
from pyqt_get_selected_filter import getSelectedFilter

from pyqt_svg_viewer.svgViewerView import SvgViewerView


class SvgViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__title = 'SVG Viewer'
        self.__extensions = ['.svg']

    def __initUi(self):
        self.setWindowTitle(self.__title)

        self.__srcWidget = SourceWidget()
        self.__srcWidget.closeSignal.connect(self.__srcWidgetBtnToggled)

        self.__listViewerWidget = ListViewerWidget()
        self.__listViewerWidget.closeListSignal.connect(self.__fileListWidgetBtnToggled)
        self.__listViewerWidget.closeViewerSignal.connect(self.__showNavigationToolbar)
        self.__listViewerWidget.setExtensions(self.__extensions)
        self.__listViewerWidget.setView(SvgViewerView())
        self.__listViewerWidget.setWindowTitleBasedOnCurrentFileEnabled(True, self.windowTitle())
        self.__listViewerWidget.showSignal.connect(self.__showSource)

        self.__fileListWidget = self.__listViewerWidget.getListWidget()

        splitter = QSplitter()
        splitter.addWidget(self.__listViewerWidget)
        splitter.addWidget(self.__srcWidget)
        splitter.setSizes([400, 200])
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

    def __showFileToViewer(self, filename: str):
        self.__viewerWidget.setCurrentFilename(filename)

    def __showSource(self, filename: str):
        self.__srcWidget.setSourceOfFile(filename)

    def __removeSomeFilesFromViewer(self, filenames: list):
        self.__viewerWidget.removeSomeFilesFromViewer(filenames)
        self.__selectCurrentFileItemInList()

    def __selectCurrentFileItemInList(self):
        idx = self.__viewerWidget.getCurrentIndex()
        self.__fileListWidget.setCurrentItem(idx)
        self.__showSource(self.__fileListWidget.getFilenameFromRow(idx))
        self.__viewerWidget.setFocus()

    def __setActions(self):
        self.__loadFileAction = QWidgetAction(self)
        self.__loadFileBtn = SvgButton(self)
        self.__loadFileBtn.setIcon('ico/add_file.svg')
        self.__loadFileBtn.setShortcut('Ctrl+O')
        self.__loadFileBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Open Files',
                                                                          shortcut='Ctrl+O'))
        self.__loadFileBtn.clicked.connect(self.__loadFile)
        self.__loadFileAction.setDefaultWidget(self.__loadFileBtn)

        self.__loadDirAction = QWidgetAction(self)
        self.__loadDirBtn = SvgButton(self)
        self.__loadDirBtn.setIcon('ico/add_dir.svg')
        self.__loadDirBtn.setShortcut('Ctrl+Shift+O')
        self.__loadDirBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Open Directory',
                                                                         shortcut='Ctrl+Shift+O'))
        self.__loadDirBtn.clicked.connect(self.__loadDir)
        self.__loadDirAction.setDefaultWidget(self.__loadDirBtn)

        self.__fileListToggleAction = QWidgetAction(self)
        self.__fileListToggleBtn = SvgButton(self)
        self.__fileListToggleBtn.setIcon('ico/list.svg')
        self.__fileListToggleBtn.setCheckable(True)
        self.__fileListToggleBtn.setShortcut('Ctrl+L')
        self.__fileListToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show File List',
                                                                                shortcut='Ctrl+L'))
        self.__fileListToggleBtn.toggled.connect(self.__fileListToggle)
        self.__fileListToggleAction.setDefaultWidget(self.__fileListToggleBtn)

        self.__showNavigationToolbarAction = QWidgetAction(self)
        self.__showNavigationToolbarBtn = SvgButton(self)
        self.__showNavigationToolbarBtn.setIcon('ico/navigation_bar.svg')
        self.__showNavigationToolbarBtn.setCheckable(True)
        self.__showNavigationToolbarBtn.setChecked(True)
        self.__showNavigationToolbarBtn.setShortcut('Ctrl+B')
        self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide Navigation Bar',
                                                                                       shortcut='Ctrl+B'))
        self.__showNavigationToolbarBtn.toggled.connect(self.__showNavigationToolbar)
        self.__showNavigationToolbarAction.setDefaultWidget(self.__showNavigationToolbarBtn)

        self.__srcWidgetToggleAction = QWidgetAction(self)
        self.__srcWidgetToggleBtn = SvgButton(self)
        self.__srcWidgetToggleBtn.setIcon('ico/source.svg')
        self.__srcWidgetToggleBtn.setCheckable(True)
        self.__srcWidgetToggleBtn.setShortcut('Ctrl+S')
        self.__srcWidgetToggleBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show Source Browser',
                                                                                 shortcut='Ctrl+S'))
        self.__srcWidgetToggleBtn.toggled.connect(self.__srcWidgetToggle)
        self.__srcWidgetToggleAction.setDefaultWidget(self.__srcWidgetToggleBtn)

        self.__fullScreenToggleAction = QWidgetAction(self)
        self.__fullScreenToggleBtn = SvgButton(self)
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
        filename = QFileDialog.getOpenFileName(self, 'Open File', '',
                                               f'SVG File {getSelectedFilter(self.__extensions)}')
        if filename[0]:
            filename = filename[0]
            self.__listViewerWidget.addFilenames([filename])
            self.__showSource(filename)

    def __loadDir(self):
        dirname = QFileDialog.getExistingDirectory(self, 'Open Directory', '', QFileDialog.ShowDirsOnly)
        if dirname:
            self.__listViewerWidget.addDirectory(dirname)
            filename = [os.path.join(dirname, filename) for filename in os.listdir(dirname) if os.path.splitext(filename)[-1] in self.__extensions][0]
            self.__showSource(filename)

    def __showNavigationToolbar(self, f):
        self.__showNavigationToolbarBtn.setChecked(f)
        self.__listViewerWidget.setBottomWidgetVisible(f)
        if f:
            self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Hide navigation bar',
                                                                                           shortcut='Ctrl+B'))
        else:
            self.__showNavigationToolbarBtn.setToolTip(DescriptionToolTipGetter.getToolTip(title='Show navigation bar',
                                                                                           shortcut='Ctrl+B'))

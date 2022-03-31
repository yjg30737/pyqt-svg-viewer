# pyqt-svg-viewer
PyQt SVG viewer

## Requirements
* PyQt5 >= 5.15.6 - for `QSvgWidget`

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-svg-viewer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-viewer-widget.git">pyqt-viewer-widget</a>
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a>
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-setter.git">pyqt-custom-titlebar-setter</a>
* <a href="https://github.com/yjg30737/pyqt-description-tooltip.git">pyqt-description-tooltip</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_svg_viewer import SvgViewer


if __name__ == "__main__":
    import sys

    app = SvgViewerApp(sys.argv)
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/160336283-617857ac-9ccf-4dd5-87db-48600729c115.png)




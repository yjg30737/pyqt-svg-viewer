# pyqt-svg-viewer
PyQt SVG viewer

## Requirements
* PyQt5 >= 5.15.6 - for `QSvgWidget`

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-svg-viewer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a>
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-setter.git">pyqt-custom-titlebar-setter</a>
* <a href="https://github.com/yjg30737/pyqt-description-tooltip.git">pyqt-description-tooltip</a>
* <a href="https://github.com/yjg30737/pyqt-list-viewer-widget.git">pyqt-list-viewer-widget</a>
* <a href="https://github.com/yjg30737/pyqt-get-selected-filter.git">pyqt-get-selected-filter</a>

## Example
Code Sample
```python
from pyqt_svg_viewer import SvgViewerApp

if __name__ == "__main__":
    import sys

    app = SvgViewerApp(sys.argv)
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/172029084-ad0fec80-f403-48df-81ce-ce5120b85ca3.png)




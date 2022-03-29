from setuptools import setup, find_packages

setup(
    name='pyqt-svg-viewer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_svg_viewer.ico': ['svg.svg']},
    description='PyQt SVG viewer',
    url='https://github.com/yjg30737/pyqt-svg-viewer.git',
    install_requires=[
        'PyQt5>=5.15.6',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main'
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main'

    ]
)
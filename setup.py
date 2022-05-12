from setuptools import setup, find_packages

setup(
    name='pyqt-svg-viewer',
    version='0.2.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_svg_viewer.ico': ['add_dir.svg', 'add_file.svg', 'close.svg', 'full_screen.svg',
                                          'list.svg', 'navigation_bar.svg',
                                          'source.svg', 'svg.svg']},
    description='PyQt SVG viewer',
    url='https://github.com/yjg30737/pyqt-svg-viewer.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter>=0.0.1',
        'pyqt-custom-titlebar-setter>=0.0.1',
        'pyqt-description-tooltip @ git+https://git@github.com/yjg30737/pyqt-description-tooltip.git@main',
        'pyqt-list-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-list-viewer-widget.git@main',
        'pyqt-get-selected-filter @ git+https://git@github.com/yjg30737/pyqt-get-selected-filter.git@main'
    ]
)
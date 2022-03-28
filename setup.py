from setuptools import setup, find_packages

setup(
    name='pyqt-svg-viewer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt SVG viewer',
    url='https://github.com/yjg30737/pyqt-svg-viewer.git',
    install_requires=[
        'PyQt5>=5.15.6'
    ]
)
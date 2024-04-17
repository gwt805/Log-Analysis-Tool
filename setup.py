from setuptools import setup
from src import __version__

setup(
    name = "log_analysis_tool",
    author = "gwt",
    author_email = "1973735972@qq.com",
    version = __version__,
    description = "log analysis tool",
    packages = ['src', 'qrc'],
    include_package_data = True,
    install_requires = ['pyqt5', 'easydict', 'openpyxl'],
    data_files = ["qrc/logo.png"],
    python_requires = ">=3.6",
    keywords=["Log", "screen", "application", "PyQt5", "Python 3"],
    entry_points={
        "console_scripts": [
            "log_analysis_tool=src.app:main"
        ]
    }
)

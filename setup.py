from setuptools import setup
from log_analysis_tool import __version__

setup(
    name = "log_analysis_tool",
    author = "gwt",
    author_email = "1973735972@qq.com",
    version = __version__,
    description = "log analysis tool",
    packages = ['log_analysis_tool'],
    include_package_data = True,
    install_requires = ['pyqt5', 'easydict', 'openpyxl'],
    python_requires = ">=3.6",
    keywords=["Log", "screen", "application", "PyQt5", "Python 3"],
    entry_points={
        "console_scripts": [
            "log_analysis_tool=log_analysis_tool.app:main"
        ]
    }
)

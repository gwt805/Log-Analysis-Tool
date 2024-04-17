# 巡检清洁 console 日志分析工具
<div align='center'>
    <img src="./demo/demo.jpg">
</div>

# Used
```
> pip install twine
> python setup.py sdist bdist_wheel
> twine upload dist/log_analysis_tool-your_version-py3-none-any.whl # 会提示输入你的 PyPi Token
> pip install -U log-analysis-tool # 注意这里不要设置镜像，本地永久镜像也不能要
> log_analysis_tool # 这样就会界面就会弹出来了

or

> python log_analysis_tool/app.py
```
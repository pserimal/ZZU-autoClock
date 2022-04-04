# 关于配置 win10 任务计划的教程https://www.cnblogs.com/lishidefengchen/p/4381565.html
# 可以不填写 powershell 完整路径，直接填写 powershell 也可

# 记得更改自己存放脚本的路径
python -u "完整路径/autoClock.py";
# 退出 powershell，exit只能终止脚本运行
Stop-Process -Name powershell

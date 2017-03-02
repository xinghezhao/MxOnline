请下载success分之，之后运行pip install -r requirement.txt
# MxOnline
Mxonline(在线教育学习网站)
本项目技术语言 Python2.7，所用框架django1.9 xadmin0.6.1。

本项目是做的在线教育系统，基于Django，后台用的是xadmin。能够实现，登陆、注册、找回密码。添加教育机构，教育机构中的讲师，
讲师的课程等，支持全局搜索，能够快速搜索出，讲师、教育机构或者是相关课程。能够对课程、讲师、或教育机构进行排序等。
有个人中心管理能够实现个人头像的更换，修改密码，更换邮箱。

能够在后台对课程，讲师等一系列进行更新。

pip install django-simple-captcha==0.4.6 用于验证码

pip install django-pure-pagination 用户分页

pip install pillow 图像处理

https://github.com/zhangfisher/DjangoUeditor  富文本编辑器    将github整个源码包下载回家，在命令行运行：
    python setup.py install  推荐源码安装，pip安装会提示找不到模板。（大坑）
    
个人强烈推荐使用Xadmin,功能样式，都比Admin强大。

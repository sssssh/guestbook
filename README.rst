===================
留言板应用
===================


目的
=====


练习开发通过Web浏览器提交留言的Web应用程序


工具版本
====================


:Python:     2.7.10
:pip:        9.0.1
:virtualenv: 15.1.0


安装与启动方法
=======================


从版本库获取代码，然后在该目录下搭建virtualenv环境::

  $ git clone https://github.com/sssssh/guestbook.git
  $ cd guestbook
  $ virtualenv ENV
  $ source ENV/bin/activate
  (ENV)$ pip install .
  (ENV)$ guestbook


开发流程
=========

用于开发的安装
------------------


1. 检测
2. 按以下流程安装::

     (ENV)$ pip install -e .

变更依赖库时
---------------------

1. 更新``setup.py``的``install_requires``
2. 按以下流程更新环境::

     (ENV)$ virtualenv --clear ENV
     (ENV)$ pip install -e ./guestbook (local path)

3. 将setup.py和requirements.txt提交到版本库


延伸
---------------------
为什么用pip install -e进行安装
时间一久，就算是自己开发的项目，我们也会忘记如何搭建运行环境。
所以为了将来不忘 记，我们最好在文档的开头就记下运行程序之前所
需的全部流程。另外，尽量能让自己在看文 档时立刻回想起当时用了
什么流程。因此，流程要尽量短，而且要用开发者们普遍采用的结构。::

  不容易出现键入错误、流程颠倒等人为失误
  减少整个项目中需要记忆的东西
  需要向其他开发者或使用者传递的信息更少，减少文档量
  测试和部署更容易自动化

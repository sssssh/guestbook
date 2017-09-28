from setuptools import setup, find_packages


setup(
    name='guestbook',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)


# name
'''
一般情况下，包名都与项目名称一致。但是，用于发布的程序包需要有一个独特的名称，以防止与其他程序包名撞车。
'''

# version
'''
代表版本号的字符串
'''

# packages
'''
指定所有捆绑的Python程序包。
如果一个项目包含多级目录，那么：
packages=[
    'guestbook', 'guestbook.server', 'guestbook.server.dir',
    'guestbook.storage', ...
],
'''

# include_package_data
'''
在packages指定的Python包(目录)中，除“.py”之外的文件都称为程序包资源。
这个设置用来指定是否安装Python包中所含的程序包资源。
这里我们要安装templates和static这两个程序包资源，所以将它们指定为True。
'''

# install_requires
'''
列表指定依赖包。与requirements.txt不同，这里一般不指定版本。
'''

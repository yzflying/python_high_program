"""
定义一个class，需要显示得继承object，在python3中默认继承了object

第4章：
4.2命名风格
常亮表示：使用大写字母，加下划线连接
变量表示：小写字母，前面加下划线
函数方法名称表示：使用小写字母，加下划线连接
4.3通用风格
避免使用模块名、通用名
4.4参数
函数入参进行assert，判断入参是否符合标准
避免使用没有名称意义的入参，例如魔法参数*args、**kwargs
*args接受不定量的入参，例如3,2，形成一个元组(3,2)；**kwargs接受不定量的入参,例如a=3,b=2，形成一个字典{a:3,b:2}
4.5类的名称
4.6模块、包的名称
使用小写字母，不带下划线
4.7风格检查工具包Pylint

第5章：
5.1创建一个包
5.1.1打包推荐工具
使用setuptools来定义项目并创建'源代码发行版'
使用wheel来创建'构建发行版'
使用twine来向PyPI上传包的发行版
5.1.2项目配置
1.setup.py
根目录脚本，定义了模块中描述的所有元数据，并合并为标准的setup()函数调用
from setuptools import setup
setup(
name = 'mypackage',
)
该脚本提供了一些命令，可用‘python setup.py --help-commands’命令来列出
2.setup.cfg
包含setup.py脚本命令的默认选项，例如下面示例，提供了global命令的默认参数：
[global]
quiet=1
3.MANIFEST.in
构建发行版时，需要指明哪些文件需要保存在存档中，MANIFEST.in定义了一个规则，例如
include README.txt
4.最重要的元数据
5.trove分类器
进行应用程序分类。所有分类器都形成一个树状结构，每个分类器是字符串形式，使用'::'分隔命名空间。
分类器列表作为setup()函数的classifiers参数，例如：
classifiers=[
'development status :: 4-beta',
'programing language :: python :: 3.7',
]
6.常见模式
版本字符串
在__init__.py文件中包含版本属性，例如：
VERSION = (0, 1, 1)
__version__ = '.'.join([str(x) for x in VERSION])
README文件
管理依赖
可以在setup()函数中列出依赖包，例如：
install_requires = ['falcon','requests']
也可以使用requirement.txt文件来列出
5.1.3自定义setup命令
新的命令可以用入口点entry point来注册，入口点是类或者函数的命名链接。任何应用都可以扫描所有已注册的包，并将链接作插件使用
要想链接新的命令，可以在setup()中调用entry_point元数据，例如：
entry_points = "
[distutils.commands]
mycommand = my.command.module.Class
"
5.1.4在开发期间使用包
安装与卸载

5.2命名空间包
如果应用组件的开发、打包、版本化是独立的，但仍然希望从同一个命名空间进行访问，命名空间包有助于理解包的所在组织
tree acme/如下（包含俩子包sql、templating）
acme/
	acme
		__init__.py
		sql
			__init__.py
		templating
			__init__.py
	setup.py
这种方法几乎不能单独开发子包，利用命名空间包改进如下：
tree acme.sql/
acme.sql/
	acme
		sql
			__init__.py
	setup.py
5.3上传一个包
5.3.1
python setup.py <disk_commands> upload
disk_commands是创建要上传的发行版的命令列表
.pypirc文件
配置文件，保存有关包仓库信息
5.3.2源代码包与构建包
源代码发行版是最简单的，不依赖于平台的；如果包中引入了其他语言，则需要用户环境有合适的编译器，否则适合构建发行版
1.sdist
它创建一颗分发树，其中复制了一个包运行需要的全部内容；然后这棵树归档到存档文件(通常是tar文件)，这个存档便是源码副本
使用命令如下：
python setup.py sdist
2.bdist与wheels
bdist通过如下命令创建构建包
python setup.py bdist

5.4独立可执行文件
创建一个可执行文件，嵌入python解释器和项目，使得不需要python解释器依赖
常用工具举例PyInstaller命令如下(生成项目文件夹包含dll、exe等文件)：
PyInstaller <项目文件名称.py>
5.4.3可执行文件包中的python代码安全性
不会让代码安全，可以通过反编译渠道还原代码
反编译步骤：
1.从独立可执行文件中提取项目字节码的二进制表示
2.将二进制表示映射到python字节码
3.将字节码转换成AST
4.从AST直接重新创建源代码
避免被反编译的措施：
1.运行时删除所有可用的代码元数据
2.修改CPython解释器的字节码，使得上述第2、3步骤不容易
3.用复杂的方式修改CPython的源代码

第6章：部署代码
将代码部署到远程主机上并运行
6.1十二要素应用
6.2用fabric进行自动化部署
fabric用于自动化远程执行，它是python库，也是一个命令行工具
使用方法：
1.安装fabric并在项目根目录创建fabfile.py文件
2.fabfile.py文件内容
import os
from fabric.api import *
from fabric.contrib.files import exists
# 定义一些函数
def get_version():
	pass
def prepare_release():
	pass
@task
def uptime():
	pass
@task
def deploy():
	pass
3.使用fab --list命令列出可用子命令
4.部署
fab -R production deploy

6.4常见约定与实践
6.4.3 进程管理工具supervisor、circus
使用circus进程管理工具，启动并管理应用进程方法：


第11章：优化
11.3分析瓶颈
11.3.1分析CPU使用情况
1.宏观分析：当程序运行时，对整个程序进行分析，并生成统计数据，例如profile、cprofile模块
命令：python -m cprofile myfile.py
结果包含每个函数(function)、线程(lineno)的被调用次数(ncalls)，每次耗时(percall)，总耗时(cumtime)等信息
2.微观分析
当找到慢速函数时，需要对部分代码进行速度测试
import timeit
t = timeit.Timer("funcction")
t.timeit(number = test_num)
timeit模块在不同机器上运行时间可能有所不同，需要利用PYstones测量固定序列代码的代码基准速度，并计算比率
from test import pystone
pystone.pystones()        # 返回当前机器每秒中执行pystones的数量，例如（1,40000）
将代码耗时换算为pystones的数量，可以在不同机器上进行比较

11.3.2分析内存使用情况
应用程序中有太多对象被创建，或者不打算保留的对象一直存活，导致内存消耗
消耗内存的情况：
1.不受控制的缓存
2.未正确结束的线程
3.使用__del__方法并涉及循环引用的对象，在旧版本中垃圾回收器不会打破循环
内存泄漏：不被引用的对象占用一定的内存块
objgraph工具：可以用于创建各对象之间引用关系的图表
常用方法如下：
objgraph.show_most_common_types()   #打印各种数据类型的统计数目
objgraph.count('list')         #打印list数据类型的对象数目
objgraph.show_refs()
objgraph.show_backrefs()       #各对象相互引用关系图
当对象相互循环引用，且没有外部引用时，python垃圾回收器会进行回收；当对象定义了__del__方法时，需要3.4以后版本才可以终结类似对象

11.3.3分析网络情况
使用ntop等工具观察网络流量

第12章：优化2
12.1 降低复杂度
12.2 架构体系权衡
启用启发式算法或近似算法
将一些工作推迟到延迟任务队列处理
使用概率性数据结构
12.5缓存
当应用程序中的函数或方法计算成本较高时，可以考虑缓存：保存计算结果；；；需要经常和快速访问的对象可以考虑使用缓存
前提：该函数时确定的，给定相同的参数有相同的返回值；函数的返回值会继续有用
实现方式：
1.确定性缓存
缓存函数返回值，可以将数据放入进程内存，即记忆化
例如计算斐波那契数列的时候可以创建一个dict，保存相应输入的返回值，更通用的做法如下：
@functools.lru_cache(None)   #functools模块提供了装饰器lru_cache(maxsize, typed)，用于在内存中缓存确定性函数的结果
def fib(n):
	if n<2:
		return 1
	else:
		return fib(n-2)+fib(n-1)

2.非确定性缓存
当暂时使用预存的结果，而不确定它们的状态是否与其他系统组件一致时，可使用非确定性缓存
3.缓存服务
进程在多台机器上运行时，避免将缓存数据在多台机器复制，可以使用redis或memcached将缓存共享
from pymemcached.client.base import Client
client = Client((localhost,port))    #启动memcached客户端
client.set('key', 'value', expire='time')   #保存缓存数据
client.get('key')       #获取缓存数据
client.delete('key')    #删除缓存数据
"""

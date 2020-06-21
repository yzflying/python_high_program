"""
ps:编写的py文件名不要与模块同名
《python高级编程》第一章:python现状
1. python3于2008.12发布
2. python3与python2的差异：
    a.语法变化
    print不再是语句，而是一个函数
    捕获异常的语法由except exc，var改为except exc as var
    比较运算符<>改为!=
    整数除法表达式可以返回浮点数
    ...
    b.标准库的变化
    c.数据类型和集合的变化
    字符串前加u，表Unicode，例如u'string',python3中无需加u
3. 虚拟隔离环境
    3.1 环境隔离：解决同时开发多个项目，但项目之间的依赖不一致的问题
                  项目不再受限系统版本
                  不会破坏其他项目依赖
    3.2 运行时隔离python的方法
            利用工具，例如venv，修改PATH和PYTHONPATH的环境变量，保存在项目依赖的自定义位置
    3.3 系统级环境隔离：开发环境能完全匹配生产环境的版本与服务，例如VMware
    3.4 容器：系统级隔离的替代方法，容器与主机共享操作系统OS，开销小，只包含系统依赖
            dockerfile：容器描述文件，包含基础镜像、工程代码文件夹、工作目录WORKDIR、安装支持（RUN pip install -r requirements.txt）、CMD命令行等
            requirement：描述了项目依赖
4. 生产力工具pip、venv、shell

5. Awesome-Python，python包查询索引




"""


# 捕获异常的语法
# 首选执行try语句，报错后try其余部分不执行；从上到下依次匹配except语句的错误类型，匹配上则其余except不匹配；最后执行finally语句
# 常见异常：NameError、TypeError、IOError、ImportError等
try:
    num = int(input("输入一个整数："))
    result = 8 / num  # 将用户输入的整数除于8
    print(result)
except ZeroDivisionError as e:  # 当你输入0的时候，程序报错的最后一行代码就是ZeroDivisionError: division by zero，报错类型是ZeroDivisionError，e是异常说明division by zero
    print('不要输入0 ！')
    print(e)
except ValueError as e:  # 当你输入英文的时候，程序报错的最后一行代码就是ValueError: invalid literal for int() with base 10:'s'
    print('请输入数字，不要输入英文！')
    print(e)
except Exception as ex:  # 能捕获所有异常Exception
    print(ex)
finally:
    print('end')


# assert断言语句
# 直接assert语句判断条件，抛出AssertionError错误；if条件判断，抛出AssertionError错误
a = -1
assert a > 0, "a超出范围"            # 方法1：将抛出一个异常，报错类型与异常说明为AssertionError: a超出范围
if not a > 0:
    raise AssertionError('a > 0')    # 方法2：判断if语句，将抛出一个AssertionError类型的异常
assert a < 0                 # 断言正常，程序正常往后执行
print('end')


# 用户自定义异常
# 1.用户自定义异常类型
class TooLongExceptin(Exception):
    def __init__(self, lenth, minlenth):
        super().__init__()    # 对象初始化，可不调用
        self.lenth = lenth
        self.minlenth = minlenth

    def __str__(self):        # 异常说明
        return "姓名长度是" + str(self.lenth) + "，超过长度" + str(self.minlenth)


# 2.手动抛出用户自定义类型异常
def name_Test():
    name = input("enter your name:")
    if len(name) > 4:
        raise TooLongExceptin(len(name), 4)  # 抛出异常,入参与TooLongExceptin类中的init一致
    else:
        print(name)


# 3.执行函数
name_Test()


# #dockerfile文件示例
# #基于的基础镜像
# FROM python:3.7
# #代码添加到code文件夹
# ADD ./EF_NFCS /code
# # 设置code文件夹是工作目录
# WORKDIR /code
# # 安装支持
# RUN pip install -r requirements.txt
# CMD ["python", "/code/package/manage.py"]

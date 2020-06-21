"""
1. python内置类型
    1.1 字符串str与字节bytes
        1.1.1   str为字符串，不可变序列，能够保存文本数据类型，Unicode文本；例如 'u'foo，通常，'u'可以省略
                bytes为字节序列，只能用字节（8位），表达范围为0-255的数；例如 'b'foo，即 102 111 111（字母f的阿斯玛值为102）

        1.1.2   字符串与字节序列的转化：
                编码：将字符串转为字节序列，str.encode(encoding)
                解码：将字节序列转为字符串，bytes.decode(encoding)

        1.1.3   str是不可变的，故str可以作为字典的key，set的元素；
                每次对str进行修改，需要创建一个全新的字符串实例

        1.1.4   字符串的拼接：推荐使用 ''.join(substrs)方法

    1.2 集合类型(列表list、元组tuple、字典dict、集合set)
        1.2.1   list和tuple
                都表示对象序列，list是动态的，tuple不可修改
                list.insert与list.delete的复杂度为O(n)，list.append与list.pop的复杂度为O(1)
                列表推导，推荐使用列表生成式
                枚举enumerate，自动为列表配置索引：
                打包zip，对两个大小相等的迭代对象均匀遍历
"""
for i, ele in enumerate(['one', 'two', 'three']):
    print(i, ele)

ls = [item for item in zip(['1', '2', '3'], ['one', 'two', 'three'])]
"""
        1.2.2   dict
                将一组唯一的key映射到对应位置
                推荐使用字典生成式，例如 {num: num**2 for num in range(10)}
                字典的3个属性 keys()、values()、items()
        
        1.2.3   set
                set是一种可变的，无序的集合，元素是唯一的
                frozenset是不可变的集合
                推荐集合推导，如{num for num in range(10)}
        
2. 高级语法
    2.1 迭代器
        迭代器iter有两个方法
        iter：返回迭代器本身
        next：返回迭代器下一个元素
        当遍历完可迭代序列时，会引发异常

    2.2 生成器(特殊的迭代器)
        迭代器为生成器提供了基础，基于yield语句，生成器可以暂停函数并返回一个中间结果，该函数会保存执行上下文，必要时恢复
        
    2.3 装饰器
        被装饰函数名作为参数传递给装饰函数


    2.4 上下文管理器




"""
i = iter('abc')    # 利用iter函数和可迭代序列'abc'来创建一个迭代器i
print(next(i))     # next方法返回迭代器i的下一个元素
print(next(i))


def fibonacci():   # 定义一个函数fibonacci(带yield，即生成器，每次next返回b的当前值)
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


fib = fibonacci()  # 定义一个生成器fib
for i in range(10):
    print(next(fib))  # 返回生成器的下一个元素


# 装饰器常见模式一：函数形式（装饰器函数mydecorator的写法）
def mydecorator(function):
    def wrapped(*args, **kwargs):
        # 此处在调用被装饰函数前，处理一些事情
        result = function(*args, **kwargs)
        # 此处在调用被装饰函数后，处理一些事情
        return result
    return wrapped


# 装饰器常见模式二：类形式
class DecoratorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # 此处在调用被装饰函数前，处理一些事情
        result = self.function(*args, **kwargs)
        # 此处在调用被装饰函数后，处理一些事情
        return result







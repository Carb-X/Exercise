"""类的内省和装饰器。

定义一个类Mlog，对于继承自Mlog的子类，每当其调用属性方法时，打印如下内容：
类名、被调用的属性方法和参数值列表
开始运行时间
结束运行时间
函数运行的结果


示例：
class Any(Mlog):

    def track(*args, **kwars):
        pass

a = Any()
a.track(1,2,3, b="xx")

输出:

[Mlog] Any.track(1,2,3, b="xx")
[start] {start_timestamp}
[end] {end_timestamp}
[result] {result}
"""


import datetime



class Mlog(object):
    pass


def method_dec(original_function, cls_name, method_name):
    """This decorator is used to write logs for a class method when it is called."""

    def new_function(*args, **kw):
        print('[Mlog] {}.{}({}, {})'.format(cls_name, method_name, args, kw))
        print('[start] {}'.format(datetime.datetime.now()))
        result = original_function(*args, **kw)
        print('[end] {}'.format(datetime.datetime.now()))
        print('[result] {}'.format(result))      
        return result                                             
    return new_function


def mlog_subclass_dec(Cls):
    """Class decorator for classes derived from Mlog.

    When an instance method of a subclass (the method 
    is not defined in Mlog) is invoked, print:
    class name, method name and arguments list;
    start and end time of the function call;
    result of this invocation.
    """

    if (Mlog not in Cls.__bases__):  # do nothing if Cls is not derived from Mlog
        return Cls

    class NewCls(object):

        def __init__(self, *args, **kw):
            self.oInstance = Cls(*args, **kw)

        def __getattribute__(self, attr_name):
             
            try:
                attr = super().__getattribute__(attr_name)
            except AttributeError:
                pass
            else:
                return attr
            
            attr = self.oInstance.__getattribute__(attr_name)
            if type(attr) == type(self.__init__):
                return method_dec(attr, Cls.__name__, attr.__name__)
            else:
                return attr
    return NewCls



@mlog_subclass_dec
class Any(Mlog):

    def a(self, x, y):
        return x + y

# Test 1:
#
# The logs are as follows:
# [Mlog] Any.a((1, 2), {})
# [start] 2019-03-06 20:33:43.395617
# [end] 2019-03-06 20:33:43.395617
# [result] 3
any = Any()
any.a(1, 2)  



@mlog_subclass_dec
class Some(object):

    def s(self, x):
        return x

# Test 2:
#
# No logs are printed because Some is not derived from Mlog.
some = Some()
some.s(1)



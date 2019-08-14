# -*- coding: utf-8 -*-
from ch2.my_module import *


# 单下划线开头
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


test = Test()
assert 11 == test.foo
assert 23 == test._bar

assert 23 == external_func()
try:
    _internal_func()
except NameError as e:
    print(e)
    error1 = e
assert error1


# 单下划线结尾
def make_object(name, class_):
    pass


# 双下划线开头
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


t = Test()
print(f"dir(t):{dir(t)}")


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'


t2 = ExtendedTest()
assert 'overridden' == t2.foo
assert 'overridden' == t2._bar
# 下面的代码会报错:AttributeError: 'ExtendedTest' object has no attribute '__baz'
try:
    t2.__baz
except AttributeError as e:
    print(e)
    error2 = e
assert error2
print(f"dir(t2):{dir(t2)}")
assert 23 == t2._Test__baz
assert 'overridden' == t2._ExtendedTest__baz


class ManglingTest:
    def __init__(self) -> None:
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled


mt = ManglingTest()
assert 'hello' == mt.get_mangled()


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


mm = MangledMethod()
assert 42 == mm.call_it()
# AttributeError: 'MangledMethod' object has no attribute '__method'
try:
    mm.__method()
except AttributeError as e:
    print(e)
    error3 = e
assert error3

_MangledGlobal__mangled = 11


class MangledGlobal:
    def test(self):
        return __mangled


assert 11 == MangledGlobal().test()


# 双下滑线开头和结尾
class PrefixPostfixTest:
    def __init__(self) -> None:
        self.__bam__ = 42


assert 42 == PrefixPostfixTest().__bam__

# 单下划线
for _ in range(3):
    print('Hello,World')

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
assert 'red' == color
assert 3812.4 == mileage

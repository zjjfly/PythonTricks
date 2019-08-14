# -*- coding: utf-8 -*-
from string import Template

errno = 50159747054
name = 'Bob'
target = 'Hey Bob, there is a 0xbadc0ffee error!'

# old style
s = 'Hello,%s' % name
assert 'Hello,Bob' == s

n = '%x' % errno
assert 'badc0ffee' == n

s1 = 'Hey %s, there is a 0x%x error!' % (name, errno)
assert target == s1

s2 = 'Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno}
assert target == s2

# new style
s = 'Hello,{}'.format(name)
assert 'Hello,Bob' == s

s1 = 'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)
assert target == s1

# formatted string literal
s = f'Hello,{name}'
assert 'Hello,Bob' == s
a = 5
b = 10
s = f'Five plus ten is {a + b} and not {2 * (a + b)}.'
assert 'Five plus ten is 15 and not 30.' == s

s1 = f"Hey {name}, there is a {errno:#x} error!"
assert target == s1

# template string
t = Template('Hello,$name')
s = t.substitute(name=name)
assert 'Hello,Bob' == s

templ_string = 'Hey $name, there is a $error error!'
s1 = Template(templ_string).substitute(name=name, error=hex(errno))
assert target == s1

SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass


err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
s = user_input.format(error=err)
assert 'this-is-a-secret' == s

user_input = '${error.__init__.__globals__[SECRET]}'
try:
    Template(user_input).substitute(error=err)
except ValueError as e:
    err = e
assert err

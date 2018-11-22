# # 1 来自C语言的%方式

print('%s %s'%('Hello','world'))

# %s是一个占位符，它仅代表一段字符串，并不是拼接的实际内容。实际的拼接内容在一个单独的%号后面，放在一个元组里。类似的占位符还有：%d（代表一个整数）、%f（代表一个浮点数）、%x（代表一个16进制数）


# # 2 format()拼接方式

s1='Hello {}! My name is {}.'.format('World','PyCat')
print(s1)

s2='Hello {0}! My name is {1}'.format('World','PyCat')
s3='Hello {name1}! My name is {name2}.'.format(name1='World',name2='PyCat')
print(s2)
print(s3)

# 使用花括号{}做占位符，在format方法中再转入实际的拼接值。对号入座版主要有两种，一种传入序列号(s2)一种则使用key-value的方式(s3)。


# # 3 () 类似元组方式

s_tuple=('Hello',' ','world')
s_like_tuple=('Hello' ' ' 'world')

print(s_tuple)
print(s_like_tuple)

# s_like_tuple并不是一个元组，因为元素间没有逗号分隔符，这些元素间可以用空格间隔，也可以不要空格。使用type()查看，发现它就是一个str类型。

# 多元素时，不支持有变量
# str_1 = 'Hello'
# str_2 = (str_1 'world')
# >>> SyntaxError: invalid syntax
# str_3 = (str_1 str_1)
# >>> SyntaxError: invalid syntax
# # 但是下面写法不会报错
# str_4 = (str_1)


# # 4 面向对象模板拼接
from string import Template
s=Template('${s1} ${s2}!')
print(s.safe_substitute(s1='Hello',s2='world'))


# # 5 +号方式

str_1='Hello world!'
str_2='My name is PyCat.'
print(str_1 + str_2)

# 字符串是不可变类型，新的字符串会独占一块新的内存，而原来的字符串保持不变。拼接前有两段字符串，拼接后实际有三段字符串。


# # 6 join()拼接方式

str_list=['Hello', 'world']
str_join1=' '.join(str_list)
str_join2='-'.join(str_list)
print(str_join1)
print(str_join2)

# str对象自带的join()方法，接受一个序列参数，可以实现拼接。拼接时，元素若不是字符串，需要先转换一下。这种方法比较适用于连接序列对象中（例如列表）的元素，并设置统一的间隔符。


# # 7 f-string方式

name='world'
myname='PyCat'
words=f'Hello {name}. My name is {myname}.'
print(words)

# 在字符串前加 f 标识，字符串中间则用花括号{}包裹其它字符串变量。


## 总结一下，我们前面说的“字符串拼接”，其实是从结果上理解。若从实现原理上划分的话，我们可以将这些方法划分出三种类型：

# 格式化类：%、format()、template
# 拼接类：+、()、join()
# 插值类：f-string

# 当要处理字符串列表等序列结构时，采用join()方式；拼接长度不超过20时，选用+号操作符方式；长度超过20的情况，高版本选用f-string，低版本时看情况使用format()或join()方式。

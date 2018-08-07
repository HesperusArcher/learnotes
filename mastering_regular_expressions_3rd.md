
```shell
egrep -i(ignore capital or not) 'searched string' file.name
```


[0-9A-Za-z] == [A-Za-z0-9] == [a-z0-9A-Z]


{min,max} instead "*" had limited length


metasequences
\<cat\> match the letter "cat"


|   | least | most |
| ? |     0 |    1 |
| * |     0 |  inf |
| + |     1 |  inf |


```perl
$reply =~ m/^[0-9]+$/

# `=~` means match

# `==` between numbers
# `eq` between strings
```

\b: 单词分隔符
\t: tab
\s: whitespace character
\S: not whitespace
\d: [0-9]
\w: word


```shell
perl -p -i -e 's/sysread/read/g' file.name
```

-e: 程序接在命令后面
-p: 对每一行查找和替换
-i: 将替换结果写回到文件


TODO: 环视(Lookaround)
| 表达式                                                 | 说明       |
|--------------------------------------------------------|------------|
| (?<=Expression) 逆序肯定环视，表示所在位置左侧能够匹配 | Expression |
| (?<!Expression) 逆序否定环视，表示所在位置左侧不能匹配 | Expression |
| (?=Expression) 顺序肯定环视，表示所在位置右侧能够匹配  | Expression |
| (?!Expression) 顺序否定环视，表示所在位置右侧不能匹配  | Expression |


grep: Global Regular Expression Print

POSIX: Portable Operating System Interface


程序设计语言 3 种处理正则的方式：
+ integrated: Perl
+ procedural
+ object-oriented
后两种 Java, .NET, Tcl, Python, PHP, Emacs lisp, Ruby


```perl
s/reg/exp/[gix]
# g:全局替换
# i:不区分大小写
# x:宽松排列模式
```

```elisp
\\<\\[a-z]+\\)\\([\n \t]\\|<[^>]+>\\)+\\1\\>
# 查找重复单词
```

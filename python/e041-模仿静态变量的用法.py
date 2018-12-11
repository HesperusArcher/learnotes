def varfunc():
    var = 0
    print(var)
    var += 1


if __name__ == '__main__':
    for i in range(3):
        varfunc()  # -> 0 0 0


# 类的属性
class Static:
    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)  # -> 5
a = Static()
for i in range(3):
    a.varfunc()  # -> 6 7 8

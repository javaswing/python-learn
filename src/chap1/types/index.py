"""
1. 变量的定义与赋值
"""

name = 'javaswing'  # str
month = 12  # int
salary = 1000.12  # float
is_perfect_attendance = True  # bool
team = None  # NoneType

"""
首先Python是一个强类型语言，并不像js那样是一种弱类型语言。可以使用type关键字来返回当前字段的类型
"""
print(type(team))

"""
2. 变量的命名规则
- 变量必须以字母或者下划线（_）开头。
- 命名多个单词之间需要使用下划线（_）进行连接，且只能包含数字、字母、下划线（_）
- 不能使用语言本身包含的关键字。比如：str等
"""
# 在JavaScript中一般使用 userName
user_name = "张晓天"


# 类的命名采用和JavaScript一样的方式命令
# class UserPermission:


# 函数名在JavaScript中使用的是getById的形式
def get_by_id():
    pass


# 常量都是以全大写方式，JavaScript中使用 DEFAULT_SEX

DEFAULT_SEX = 0

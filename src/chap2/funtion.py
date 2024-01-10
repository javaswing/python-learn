"""
函数的定义和调用
"""


def greet(name, age):
    print(f"你好！我是{name}，今年{age}岁")


# 正常方式传入参数
greet('javaswing', 12)

# key=value形式传入参数
greet(age=87, name='李白')

"""
匿名函数也称为“lambda”函数
"""

nums = [1, 2, 3, 5]
# 使用lambda关键字实现函数。相当于JavaScript中的() => 箭头函数形式
# 需要注意的是Python中lambda函数没有函数体，直接使用表达式的返回值自动返回
squared_numbers = list(map(lambda number: number ** 2, nums))
print(squared_numbers)

# 多个参数
print((lambda n, m: n * m)(2, 3))  # 6

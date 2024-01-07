"""
if 语句
"""

num1 = 100

if num1 > 0:
    print('正数')
elif num1 < 0:
    print('负数')
else:
    print('零')

name = None

# 不建议使用这种方式，不知道为什么。pycharm提示
if name == None:
    # if name is None:
    print('is None')
elif name != None:
    # elif name is not None:
    print('is not None')

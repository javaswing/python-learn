# 该方法是直接导入一整体模块
import calculator
# 也可以使用这种方法进行导入，和jsa中的 import { xx } from
from calculator import subtract, multiply
# 也可以使用as起别名
from calculator import divide as did
# 也可以对整个模块起别名
import calculator as cac

import name_convert

"""
需要注意的是：模块的名称不包含“-”否则不能被其它模块引用，例如：name-covert。如果把name_convert修改成“name-convert”，IDE没有办法把这个文件识别成模块的
"""

result = calculator.add(1, 2)
print(result)

print(subtract(3, 2))

print(multiply(3, 3))

print(did(3, 1))

print(cac.add(2, 2))



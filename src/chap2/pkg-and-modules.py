# 当不指定模块名称时，默认导入__init__.py中导出的模块
import pkg.subpackage as psm
# 指定从子模块的导入
from pkg.subpackage.module3 import subpackage_module3_fun
"""
模块和包
"""

"""
模块这个概念，在js中也有对应的概念。在py中每一个py文件都是一个模块

注意：在Python中所有的模块导出的变量、函数、模块都是自动导出的。可以被其它模块任意引用。Python并没有提供保护私有成员的方法。全靠约定
以“_”或者 “__”开头对成员进行命名部分，是不希望其它模块引用时进行导入的。开发时需要遵循这个约定
"""


print(subpackage_module3_fun("javaswing"))

print(psm.subpackage_module4_fun(34))

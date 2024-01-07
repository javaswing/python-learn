"""
列表和元组

Python中的列表，相当于JavaScript中的数组。用于存储多个连续的值
元组可以简单理解为常量的数组，一旦创建不能进行修改
"""

# 声明
# name_list = list()

name_list = ["🙀"]

name_tuple = ()

# 添加
name_list.append("🤡")


print(name_list)  # ['🙀', '🤡']

# 访问
print(name_list[0])

# 长度
print(len(name_list))  # 2

# 切片
print(name_list[0:1])  # ['🙀']

# 连接
print(name_list + ["🙄"])  # ['🙀', '🤡', '🙄']

# 复制
name_list_copy = name_list.copy()
print(name_list_copy)

# 反转
name_list.reverse()
print(name_list)  # ['🤡', '🙀']

# 删除
del name_list[0]
print(name_list)  # ['🙀']

# 最大值
name_list.append("🤤")
print(max(name_list))  # 🤤

# 最小值
print(min(name_list))  # 🙀

# 求和 仅支持int类型列表
# print(sum(name_list))

# 转换为元组
print(tuple(name_list))  # ('🙀', '🤤')

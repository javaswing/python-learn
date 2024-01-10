"""
字典

字典通常用于使用特定的存储和检索数据。Python中的字典与JavaScript中的对象基本等价
"""

# 声明
dict_map = {"name": "javaSwing", "age": 12}

# 也可以使用以下方式
dict_map2 = dict(name="3232", age=132)

print(dict_map2)  # {'name': '3232', 'age': 132}
print(dict_map)  # {'name': 'javaSwing', 'age': 12}

# 访问
print(dict_map["name"])  # javaSwing

# 访问带默认值
print(dict_map.get("name", "default"))

# 更新值
dict_map["name"] = "张晓天"
print(dict_map)   # {'name': '张晓天', 'age': 12}

# 合并更新
dict_map.update({"name": 'porn hub', "school": '学校名'})
print(dict_map)  # {'name': 'porn hub', 'age': 12, 'school': '学校名'}

# 删除键
del dict_map["name"]
print(dict_map)  # {'age': 12, 'school': '学校名'}

# 检查键是否存在
print("age" in dict_map)  # True

# 获取所有键
print(dict_map.keys())  # ['age', 'school']

# 获取所有值
print(dict_map.values())   # [12, '学校名']

# 获取键值对的数目
print(len(dict_map))   # 2



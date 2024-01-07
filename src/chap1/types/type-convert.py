"""
类型转换
"""

gb = "512MB"

# 使用字符串切片
int_gb = int(gb[:-2])  # 512

# int convert
print(int(gb[:-2]))

# float
print(float(gb[:-2]))  # 512.0

print(bool(gb))  # True

# list convert
print(list(gb))  # ['5', '1', '2', 'M', 'B']

# dict convert
print(dict({'name': 'xxx'}))  # {'name': 'xxx'}


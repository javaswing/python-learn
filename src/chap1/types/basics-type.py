"""
Python中的数据类型
"""

"""
基本数据类型

1. 整数类型：int
2. 浮点类型：float
3. 字符串类型：str (使用单引号或者双引号括起来的字符串)
4. 布尔值：bool 使用 True或者False
5. 空值：None
"""

name = "张晓天"

name2 = "javaswing"

print(len(name))  # 3

print(name + name2)  # 张晓天javaswing

# str[star:end] 字符串截取方法
print(name[0:1])  # 张

# 查找方法
print(name.index("晓"))  # 1

# 替换
print(name.replace("张", "林"))  # 林晓天

# 分割
print(name.split(" "))

# 大小写转换
print(name2.upper())

print(name2.lower())

# 反转
print(name[::-1])  # 天晓张

# 统计次数
print(name2.count("a"))  # 2

# 以x字符串开始
print(name.startswith("张"))  # True

print(name.endswith("晓"))  # False

# 除去两端空格
print(" xx00 ".strip())  # xx00

# 第一个单词首字母大写
print("porn hub".capitalize())  # Porn hub

# 每个单词首字母大写
print("porn hub".title())  # Porn Hub

"""
列表推导和字典推导
Python中，列表推导和字典推导提供了一种简洁的创建列表和字典

列表推导和字典推导是Python特有，JavaScript没有与之等价的语法与特性
"""

# 列表推导
squared_numbers = [x**2 for x in range(1, 11)]
print(squared_numbers)

filtered_numbers = [num for num in squared_numbers if num % 2 == 0]
print(filtered_numbers)

squared_dic = {x: x ** 2 for x in range(1, 11)}
filtered_dic = {key: value for key, value in squared_dic.items() if value < 5}
print(filtered_dic)

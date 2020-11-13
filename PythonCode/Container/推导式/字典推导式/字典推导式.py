"""字典推导和列表推导的使用方法是类似的，只不中括号该改成大括号。直接举例说明："""

# 例子一：大小写key合并
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
  k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
  for k in mcase.keys()
  if k.lower() in ['a', 'b']
}
print(mcase_frequency)
# Output: {'a': 17, 'b': 34}

# 例子二：快速更换key和value
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)
# Output: {10: 'a', 34: 'b'}
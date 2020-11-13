# 它们跟列表推导式也是类似的。 唯一的区别在于它使用大括号{}。
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: set([1, 4])
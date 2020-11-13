# coding:utf-8
from graphviz import Digraph

dot = Digraph(comment='The Round Table')

# 添加圆点 A, A的标签是 King Arthur
dot.node('A', 'king')
dot.view()  # 后面这句就注释了，也可以使用这个命令查看效果

# 添加圆点 B, B的标签是 Sir Bedevere the Wise
dot.node('B', 'Sir Bedevere the Wise')
# dot.view()

# 添加圆点 L, L的标签是 Sir Lancelot the Brave
dot.node('L', 'Sir Lancelot the Brave')
# dot.view()

# 创建一堆边，即连接AB的边，连接AL的边。
dot.edges(['AB', 'AL'])
# dot.view()

# 在创建两圆点之间创建一条边
dot.edge('B', 'L', constraint='false')
# dot.view()

# 获取DOT source源码的字符串形式
print(dot.source)

# 保存source到文件，并提供Graphviz引擎
dot.render('test-output/round-table.gv', view=True)
# x
# 30
#
# 1
# # coding:utf-8
# 2
# from graphviz import Digraph
#
# 3
# 4
# dot = Digraph(comment='The Round Table')
# 5
# 6
# # 添加圆点 A, A的标签是 King Arthur
# 7
# dot.node('A', 'king')
# 8
# dot.view()  # 后面这句就注释了，也可以使用这个命令查看效果
# 9
# 10
# # 添加圆点 B, B的标签是 Sir Bedevere the Wise
# 11
# dot.node('B', 'Sir Bedevere the Wise')
# 12
# # dot.view()
# 13
# 14
# # 添加圆点 L, L的标签是 Sir Lancelot the Brave
# 15
# dot.node('L', 'Sir Lancelot the Brave')
# 16
# # dot.view()
# 17
# 18
# # 创建一堆边，即连接AB的边，连接AL的边。
# 19
# dot.edges(['AB', 'AL'])
# 20
# # dot.view()
# 21
# 22
# # 在创建两圆点之间创建一条边
# 23
# dot.edge('B', 'L', constraint='false')
# 24
# # dot.view()
# 25
# 26
# # 获取DOT source源码的字符串形式
# 27
# print(dot.source)
# 28
# 29
# # 保存source到文件，并提供Graphviz引擎
# 30
# dot.render('test-output/round-table.gv', view=True)
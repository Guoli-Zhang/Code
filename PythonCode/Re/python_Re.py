# -*_ coding:utf-8 -*-
import re

# 1. 将以下网址提取出域名：
# 提取出域名
s1 = """http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
https://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415"""

p = r"(http.?://.+?/).+"
print(re.sub(p, lambda x: x.group(1), s1))

# 2. 去除以下html文件中的标签，只显示文本信息。
# 去除标签
s2 = "<div>\
<p>岗位职责：</p>\
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>\
<p><br></p>\
<p>必备要求：</p>\
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>\
<p>&nbsp;<br></p>\
<p>技术要求：</p>\
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>\
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>\
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>\
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>\
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>\
<p>&nbsp;<br></p>\
<p>加分项：</p>\
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>\
</div>"
t = "(</?\w+>|&nbsp;)"
p = r"(<[^>]*>|&nbsp;)"
print(re.sub(p, " ", s2))
# print(re.sub(r"(<[^>]*>|&nbsp;)", " ", s2))
# 3. 提取出如下字符串中的单词：hello world ha ha
# 提取出单词
s3 = "hello world ha ha"
print(re.split(r" +", s3))  # 用split方法分割空格
print(re.findall(r"\b\w+\b", s3))

# 4. IP
if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
            "192.168.103.1"):
    print("IP vaild")
else:
    print("IP invaild")

# 精确提取IP
string_ip = "is this 289.22.22.22 ip ?"
result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip)
if result:
    print(result)
else:
    print("re cannot find ip")

# 5. \\
s = "c:\\a\\b\\d"
print(re.match("c:\\\\a", s).group())
print(re.match(r"c:\\a", s).group())

# 6. match、search、findall、finditer
data = 'bat bit btt a ta tib atb but hat hit hut'
print(re.findall(r"\b[bh][aiu]t\b", data))

s4 = "23432WerWre2342WerWreW "
p = r"(\d*)([a-zA-Z]*)"

# match(从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。)
m = re.match(p, s4)
print(f"{m.group()}\n{m.group(0)}\n{m.group(1)}\n{m.group(2)}\n{m.groups()}")

# findall(返回string中所有与pattern相匹配的全部字串，返回形式为数组。)
print(re.findall(p, s4))

s5 = "11113446777"
print(re.findall(r"(\d)\1*", s5))

# search
m = re.search(r"(\d)\*", s5)  # print(m.group())报错：AttributeError: 'NoneType' object has no attribute 'group'
n = re.search(r"(\d)\1*", s5)
print(f"{n.group()}\n{n.group(0)}\n{n.group(1)}\n{n.groups()}")

# finditer
o = re.finditer(r"(\d)\1*", s5)
print(f"{o.__next__().group()}\n{o.__next__().group()}\n{o.__next__().group()}\n{o.__next__().group()}\n{o.__next__().group()}")

# p = r"(\d)\1+([a-zA-Z]+)"
s6 = '1111werwrw3333rertert4444'
p = r'(\d)\1+([a-zA-Z]*)'
print(re.findall(p, s6))
print(re.search(p, s6).group())
print(re.search(p, s6).group(1))
print(re.search(p, s6).group(2))
print(re.search(p, s6).groups())
o = re.finditer(p, s6)
print(f"{o.__next__().group()}\n{o.__next__().group()}\n{o.__next__().group()}")

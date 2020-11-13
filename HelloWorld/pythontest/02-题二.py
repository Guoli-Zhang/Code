# 完成模拟商品管理的功能
#
# 要求1: 创建名为“heima”的数据库，在该数据库中创建包含名为“goods”的表；
#
# 要求2: goods表包含id、name、price三个字段，其中id为主键，name和price字段分别存储用户名和单价(decimal(7, 2))，name不允许为空不允许重复；
#
# 要求3: 代码运行起来后, 控制台显示主页面如下：
#
#
#
# 要求4: 输入1进入添加模块，依次提示用户输入商品名称、单价，若全部输入正确，将该商品名和单价信息存入数据库，提示“添加成功”并返回主页面；若数据库中已存在该商品名，提示“该商品已存在, 请重新添加!”；
#
# 要求5: 输入2进入查询模块，提示用户依次输入价格范围(输入两次单价, 先小后大)，若输入正确并查询到结果，显示此间隔范围内的商品信息；若输入错误，提示“输入有误, 请重新输入!”
#
# 答案提交方式：创建数据库和表的sql语句以注释的形式写在所有代码之前，只提交一份代码文件。
# (30分)反馈该题

# create table goods(id int unsigned primary key auto_increment not null, name varchar(20)
# not null, price decimal(7, 2) not null);

import pymysql

conn = pymysql.connect(host="localhost", user="root", port=3306, pasworrd="mysql", database="heima", charset="utf8")

cursor = conn.cursor()

sql = "select * from goods;"

num = cursor.execute(sql)

result = cursor.fetchall()

cursor.close()

conn.close()

goods = list(result)


def start():
    while True:
        print("-" * 10 + "管理系统" + "-" * 10)
        print("1:添加商品")
        print("2.查询商品")
        print("请输入功能对应的序号：")


def add():
    name = input("请输入商品名称：")
    price = input("请输入商品单价：")
    conn = pymysql.connect(host="localhost", user="root", port=3306, pasworrd="mysql", database="heima",
                           charset="utf8")

    cursor = conn.cursor()

    sql = "insert into goods values(1,'%name', '%price');" % name, price

    num = cursor.execute(sql)
    print(num)

    result = cursor.fetchall()
    print(result)

    cursor.close()

    conn.close()

    return


def select():
    price1 = input("请输入商品价格最低价：")
    price2 = input("请输入商品价格最高价：")
    if price2 >= price1:
        print("输入成功！")
        conn = pymysql.connect(host="localhost", user="root", port=3306, pasworrd="mysql", database="heima",
                               charset="utf8")

        cursor = conn.cursor()

        sql = "select * from goods where price between %price1 and %price2;" % price1, price2

        num = cursor.execute(sql)
        print(num)

        result = cursor.fetchall()
        print(result)

        cursor.close()

        conn.close()
    else:
        print("输入有误，请重新输入")


def fun():
    start()
    num = input("请选择功能：")
    if num == "1":
        print("您选择的功能是：添加商品")
        add()
    if num == "2":
        print("你选择的功能是：查询商品")
        select()
    else:
        print("请按提示输入！")
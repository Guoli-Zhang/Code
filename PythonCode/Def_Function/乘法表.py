import openpyxl
# 工作簿
workbook = openpyxl.Workbook()
# 工作表
worksheet = workbook.active
# 创建九九乘法表
nine_list = []
for i in range(1, 10):
    # 临时表，储存每一行
    temp_list = []
    for j in range(1, i + 1):
        # 打印九九乘法表
        print("{} x {} = {}".format(j, i, i * j), end='\t')
        temp_list.append("{} x {} = {}".format(j, i, i * j))
    nine_list.append(temp_list)
    print()
# 将九九乘法表批量写入到Excel中
for i in nine_list:
    worksheet.append(i)
# 保存Excel
workbook.save("九九乘法表.xlsx")

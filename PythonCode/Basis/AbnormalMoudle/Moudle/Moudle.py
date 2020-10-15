
# sys模块
import sys
print(f"{sys.stdout.write}")

# 今天是今年第几天
import datetime


def dayofyear():
    year = int(input())
    month = int(input())
    day = int(input())
    date1 = datetime.date(year=year, month=month, day=day)
    date2 = datetime.date(year=year, month=1, day=1)
    return (date1 - date2).days + 1

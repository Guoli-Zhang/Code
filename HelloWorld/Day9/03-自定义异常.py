class PhoneError(Exception):  # 自定义异常类    必须要继承Exception类
    pass


def check_phone(part1):
    if len(part1) != 11:
        Phone = PhoneError("手机号码不满11位")  # 创建异常对象
        raise Phone  # 抛出异常对象
    else:
        print("欢迎使用！")


check_phone("135252546466")
class MobileConverter:
    """匹配手机号码的路由转换器"""
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        """用于路由匹配"""
        return int(value)

    def to_url(self, value):
        """用于反向解析时传值的"""
        return str(value)


class CustomConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        """"""
        return int(value)

    def to_url(self, value):
        """"""
        return str(value)

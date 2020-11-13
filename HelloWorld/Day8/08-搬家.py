# 属性：类型、占地面积
# 输出：具体的家具及其占地面积

# 房子：
# 属性：地址、占地面积、剩余面积


# class Furniture:
#     def __init__(self, part1, part2):
#         self.types = part1
#         self.area = part2
#
#     def __str__(self):
#         return f"家具：{self.types}, 面积：{self.area}平方"
#
#
# class House:
#     def __init__(self, part1, part2, part3):
#         self.address = part1
#         self.area = part2
#         self.free = part3
#         self.furniture = []
#
#     def add_furn(self, furn):
#         if self.free >= furn.area:
#             print(f"{furn.types}添加成功！")
#             self.free -= furn.area
#             self.furniture.append(furn.types)
#         else:
#             print(f"{furn.types}添加失败！")
#
#     def __str__(self):
#         if len(self.furniture) == 0:
#             return f"房址：{self.address}, 占地面积{self.area}剩余面积：{self.free}, 无家具搬入！"
#         else:
#             return f"房址：{self.address},占地面积：{self.area}, 剩余面积：{self.free}, 搬入的家具有:" \
#                 f"{'、'.join(self.furniture)}"
#
#
# bed = Furniture("席梦思", 4)
# sofa = Furniture("真皮沙发", 2.5)
# washing_machine = Furniture("海尔", 2)
# swimming = Furniture("泳池", 160)
# sz = House("深圳湾1号", 200, 160)
# sz.add_furn(bed)
# sz.add_furn(sofa)
# sz.add_furn(washing_machine)
# sz.add_furn(swimming)
# print(sz)
# print()
# print("_*_" * 30)
# print()
# shanghai = House("海港7号", 180, 140)
# print(shanghai)


class Furniture:
    def __init__(self, types, area):
        self.types = types
        self.area = area

    def __str__(self):
        return f"{self.types}占地{self.area}平方。"


class House:
    def __init__(self, address, area, surplus):
        self.address = address
        self.area = area
        self.surplus = surplus
        self.furniture = []

    def add_furniture(self, furn):
        if self.surplus >= furn.area:
            print(f"{furn.types}添加成功！")
            self.surplus -= furn.area
            self.furniture.append(furn.types)
        else:
            print(f"{furn.types}添加失败！")

    def __str__(self):
        if len(self.furniture) == 0:
            return f"{self.address}占地{self.area}平方，剩余{self.surplus}平方可使用, 无家具添置。 "
        else:
            return f"{self.address}占地{self.area}平方，剩余{self.surplus}平方可使用，{'、'.join(self.furniture)}" \
                f"等家具成功添加！"







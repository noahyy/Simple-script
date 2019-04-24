import random

class number_phone():#
    def proparea(self):  # 选择区号
        arrow = ['139', '138', '137', '136', '135', '134', '178', '170', '188', '187',
             '183', '182', '159', '158', '157','152', '150','147', '1390', '186',
             '185', '156', '155', '130', '131', '132', '189', '180', '170', '153', '133']
        return random.choice(arrow)

    def y(self,num, list):  # 用列表装生成电话号码
        for i in range(0, num):
            proparea_1 = self.proparea()
            list.append(self.z(proparea_1))

    def z(self,proparea):  # 生成电话号码
        while 1:
            num = random.randint(0, 9)
            proparea = proparea + str(num)
            if len(proparea) == 11:
                return proparea

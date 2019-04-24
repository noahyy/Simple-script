from 简单脚本 import import_1
from 简单脚本.导入意向学员.intended_curriculum.curriculum_num import curriculum_num_1


class create_curriculum_1():
    def curriculum_1(self,num,Excel):
        list = []
        curriculum_num_1().num_curriculum(list,num)
        i = 5
        import_1.Excel().writeExcel(list, Excel, i)

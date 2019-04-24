from 简单脚本 import import_1
from 简单脚本.导入意向学员.interest_degree.degree import degree_num


class create_degree_1():
    def degree_1(self,num,Excel):
        list = []
        degree_num().num_degree(list,num)
        i = 6
        import_1.Excel().writeExcel(list, Excel, i)

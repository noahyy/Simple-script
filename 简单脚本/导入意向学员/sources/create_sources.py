from 简单脚本.导入意向学员.sources.sources_num import sources_num_1
from 简单脚本 import import_1


class create_sources_1():
    def sources_1(self,num,Excel):
        list = []
        sources_num_1().num_sources(list,num)
        i = 3
        import_1.Excel().writeExcel(list, Excel, i)


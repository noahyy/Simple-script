from 简单脚本.导入意向学员.phone.create_phone import create_phone_1
from 简单脚本.导入意向学员.name.create_name import create_name_1
from 简单脚本.导入意向学员.sex.create_sex import create_sex_1
from 简单脚本.导入意向学员.sources.create_sources import create_sources_1
from 简单脚本.导入意向学员.interest_degree.create_degree import create_degree_1
from 简单脚本.导入意向学员.intended_curriculum.create_curriculum import create_curriculum_1




class input_1():
    def inputdata(self,number,Excel):
        num = int(number)
        create_phone_1().x(num,Excel)
        create_name_1().x(num,Excel)
        create_sex_1().x(num,Excel)
        create_sources_1().sources_1(num,Excel)
        create_degree_1().degree_1(num,Excel)
        create_curriculum_1().curriculum_1(num,Excel)

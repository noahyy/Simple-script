from 简单脚本.导入意向学员.input_data import input_1

class number_of_people():
    def number(self):
        num = 2000
        # num = input('请输入意向学员人数：')
        Excel = 'C://Users//杨贤宇//Desktop//1.xlsx'
        input_1().inputdata(num,Excel)
number_of_people().number()

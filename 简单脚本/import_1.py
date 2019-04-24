import xlrd
from xlutils.copy import copy
# xlutils版本位1.7.2

class Excel():
    def writeExcel(self,list, Excel,i):         # 输入到Excel表格可以保存,
        rb = xlrd.open_workbook(Excel)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for x, v in enumerate(list, 3):     #2代表从Excel表格第三行开始输入
            y = i
            ws.write(x, y, v)
        wb.save(Excel)
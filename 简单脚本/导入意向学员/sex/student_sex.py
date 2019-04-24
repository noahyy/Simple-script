import random
class student_sex_1():
    def sex_1(self):
        a= ['男生','女生','待确认']
        return random.choice(a)
    def st_sex(self,list,num):
        for i in range(num):
            list.append(self.sex_1())
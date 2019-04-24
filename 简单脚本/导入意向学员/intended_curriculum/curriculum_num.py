import random


class curriculum_num_1():
    def curriculum_choice(self):
        a = ['语文','数学','英语','物理','化学']
        return random.choice(a)
    def num_curriculum(self,list,num):
        for i in range(num):
            list.append(self.curriculum_choice())
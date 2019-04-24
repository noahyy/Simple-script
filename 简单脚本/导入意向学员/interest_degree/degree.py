import random


class degree_num():
    def degree_choice(self):
        a = ['意向强烈','初步意向','没有意向']
        return random.choice(a)
    def num_degree(self,list,num):
        for i in range(num):
            list.append(self.degree_choice())

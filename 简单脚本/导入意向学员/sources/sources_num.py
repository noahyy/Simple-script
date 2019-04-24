import random
class sources_num_1():
    def sources_choice(self):
        a = ['广告','地推','老带新','上门']
        return random.choice(a)
    def num_sources(self,list,num):
        for i in range(num):
            list.append(self.sources_choice())

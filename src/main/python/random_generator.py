import random

class RandomGenerator:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.items = []

    def set_range(self, start, end):
        self.start = start
        self.end = self.end
        for i in range(start,end):
            self.items.append(i)

    def get_random_number(self):
        value = random.randomInt(len(self.items))
        value1 = random.choice(self.items)
        self.items.remove(value[0])
        return value[0]

    def improved(self):
        data = [1,2,3,4,5,6]
        size = len(data)
        while size:
            index = random.randrange(size)
            elem = data[index]
            data[index] = data[size-1]
            size = size - 1
            print (elem)

rg = RandomGenerator()
rg.set_range(0,10)
#for i in range (1,10):
#    print (rg.get_random_number())
rg.improved()
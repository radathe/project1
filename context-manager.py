#import time



#class RunningCodeJudge:
    #def __init__(self):
         #self.start = None
         
    #def __enter__(self):
        #print('...start')
        #self.start = time.time()
        
    #def __exit__(self, exc_type, exc_val, exc_tb):
        #t = time.time()
        #print(f'Время выполнения кода {t - self.start} сек')
        #print('...exit')
        #if exc_type is not None:
            #return True
        

#with RunningCodeJudge():
    #my_list = [x for x in range(1, 100_000)]
    #my_list -= 's'
import random


class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit
        
    def __iter__(self):
        self.limit = self.__reload
        return self
        
    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -=1
        return random.randint(0, 100)
    

rand_iter = RandomIter(5)
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))
print(next(rand_iter))


iter(rand_iter)
print(next(rand_iter))
print(next(rand_iter))

for rand_int in rand_iter:
    print(rand_int)
    





import random
class RandomIter:
  
    def __next__(self):
        return random.randint(0, 100)
    
rand_iter = RandomIter()
print(next(rand_iter))
print(next(rand_iter))

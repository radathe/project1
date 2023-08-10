#class A:
    #def public(self):
        #self._private()
        #self.__protect()
        #print(1)
    #def _private(self):
        #print(2)
    #def __protect(self):
        #print(3)
    
    
#a = A()
#a.public()
#a._private()
#a.__protect()
#a._A__protect()




#декоратор

#def deco(name_func):
    #def wrapper(a, b):
        #return name_func(a, b) - 1
    #return wrapper

#@deco
#def func(a, b):
    #return a + b + 1

#print(func(1, 6))



#from datetime import datetime


#def timit(func):
    #def wrapper(val):
        #start = datetime.now()
        #res = func(val)
        #end = datetime.now()
        #print(end - start)
        #return res
    #return wrapper
        
    
#@timit
#def get_list(val):
    #lst = []
    #for i in range(val):
        #if i % 2 == 0:
            #lst.append(i)
    #return lst


#@timit
#def get_list2(val):
    #return[i for i in range(val) if i % 2 == 0]


#get_list(20_000_000)


#get_list2(20_000_000)

#class Singleton():
    #def __new__(cls, *args, **kwargs):
        #if not hasattr(cls, 'instance'):
            #cls.instance = super(Singleton, cls).__new__(cls)
        #return cls.instance

#a = Singleton()
#b = Singleton()
#print(a, id(a))
#print(b, id(b))



#print = 5
#print('5')

a = print
a(5)
print(5)
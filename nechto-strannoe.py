#my_list = (x for i in range (1, 1000000))
#print(my_list)
#print(next(my_list))

#генератор - круглые скобки а не кввадратные
#генератор - ленивая функция, которая вычисляет значение по необходимости

#def lazyfunc():
    #for item in range(1,11): #2 #7
        #print('До', item) #3
        #yield item #отдаём item - замарозка
        #print('После', item) #6
    
#for i in lazyfunc(): #1 #5
    #print(i) #4
    
    
import contextlib


#@contextlib.contextmanager
#def reverse_str(you_str):
    #print('Вход к контекстный менеджер')
    #yield you_str[::-1] #переворачиваю строку
    ##продолж после выхода из with
    #print('выход из контекст менедж')

#with reverse_str('Hello world') as r:
    #print(r)

#@contextlib.contextmanager
#def exc_handler(exc):
    #try:
        #yield True
    #except exc:
        #print('ощибощка вышла')

#with exc_handler(IndexError):
    #my_list = [1,2]
    #print(my_list[3])
    
    
    

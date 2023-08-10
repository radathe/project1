
    
while True:
    try: 
        print ('\nУкажите интересующуюю вас операцию')
        print ('+ - сложение')
        print ('- - вычитание')
        print ('* - умножение')
        print ('/ - деление')
        operation = input()
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if operation == '+':
            print (a+b)
        elif operation == '-':
            print (a-b)
        elif operation == '*':
            print (a*b)
        elif operation == '/':
            print (a/b)
        else:
            print ('\nОперация неизвестна, повторите ввод')
            
    except ValueError:
        print ('Неизвестные значения')
        

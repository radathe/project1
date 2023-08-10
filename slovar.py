

#name = 'Даниил'
#salary = 200000

#print (f'у {name} зарплата в месяц = {salary}')

# Реализация в виде словаря

#employee = {
    #'name' : 'Даниил',
    #'salary' : 200000
#}

#print(f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')


# Реализация в виде словаря, много сотрудников

#employee_list = [
    #{
        #'name' : 'Даниил',
        #'salary' : 200000
    #},
    
    #{
        #'name' : 'Олег',
        #'salary' : 150000
    #},
    #{
        #'name' : 'Пётр',
        #'salary' : 60000
    #}
    
    

#]

#for employee in employee_list:
    #print (f'У {employee["name"]} зарплата в месяц = {employee["salary"]}')
    
# Нанимаем сотрудника

#print('\nНАЙМ СОТРУДНИКА')
#name = input ('Введите имя сотрудника')
#salary = input ('Введите ЗП сотрудника')

#new_employee = {
    #'name' : name,
    #'salary' : salary

#}

#name = input('Введите имя увольняемого сотрудника: ')
#for employee in employee_list:
    #if employee[name] == name:
        #employee_list.remove(employee)
        
        

# ООП

class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee
    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary}{f", в отпуске" if self.on_vacation else ", не в отпуске"}'

    

employee_list = [Employee('Даниил', 200000, False, True), Employee('Олег', 150000, True, True), Employee('Петя', 600000, False, True), Employee('Анна', 200000, False, True), Employee('Тимофей', 350000, True, False)]



for employee in employee_list:
    print(employee.get_info())
    if not employee.is_good_employee:
        employee_list.remove(employee)
        
print("\n")

for employee in employee_list:
    print(employee.get_info())
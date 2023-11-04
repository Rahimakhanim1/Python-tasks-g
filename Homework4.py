#task 1
# import os
# n = int(input("Enter 1 or 2: "))
# if n == 1 and os.path.exists("demo.txt"):
#         os.remove('demo.txt')
# else:
#     data = input("Enter file data: ")
#     f = open("demo.txt","a")
#     fr = open("demo.txt").read()
#     if(len(fr)==0):
#        f.write(data)
#     elif data not in list(fr.split()):
#         f.write(","+data)
#     f.close()
#     fr.close()




#task 2
# demoTxt = open("demo.txt").read()
# print(0,len(demoTxt)-1)



# task 3
# class Employee:
#     def __init__(self,emp_name,emp_id,emp_salary,emp_department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department
#     def calculate_emp_salary(self,hours_worked):
#         if hours_worked>50:
#             overtime = hours_worked - 50
#             overtimeAmount = (overtime*(self.emp_salary/50))
#             self.emp_salary+=overtimeAmount
#     def print_employee_details(self):
#         print(self.emp_name,self.emp_id,self.emp_salary,self.emp_department)
#     def assign_department(self,newDepartment):
#         self.emp_department = newDepartment



# firstEmp = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
# secondEmp = Employee("JONES", "E7499", 45000, "RESEARCH")
# thirdEmp = Employee("MARTIN", "E7900", 50000, "SALES")
# fourthEmp = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# # task1 
# def vurma(a,b):
#     return a*b

# def bolme(a,b):
#     if b==0:
#         raise ZeroDivisionError('Sifira bolme olmaz')
#     return a/b

# def toplama(a,b):
#     return a+b

# def cixma(a,b):
#     return a-b



# while True:
#     try:
#         firstNumber = float(input("Ilk ədədi daxil edin: "))
#         secondNumber = float(input("Ikinci ədədi daxil edin:"))
#         operator = input("Operatoru daxil edin:")

#         if operator == "+":
#             print(toplama(firstNumber,secondNumber))
#         elif operator == "-":
#             print(cixma(firstNumber,secondNumber))
#         elif operator == "*":
#             print(vurma(firstNumber,secondNumber))
#         elif operator == "/":
#             print(bolme(firstNumber,secondNumber))
#         else:
#             print("Duzgun melumat qeyd etmediniz")


       
    
#     except ValueError as e:
#         print("Xahis edirik yalniz reqem daxil edin:")
#     except ZeroDivisionError as e:
#         print(e)


   

# task 2

# say = 1
# while say<10:
#     say2 = 1
#     while say2<11:
#         print(say,"*",say2,"=",say*say2)
#         say2+=1
#     print()
#     say+=1







# while type(firstNumber)==int:
#     print("Ədəd tip daxil edin:")
#     firstNumber = input("Ilk ədədi daxil edin: ")
# print("bitdi")
# secondNumber = input("Ikinci ədədi daxil edin: ")
# while type(secondNumber)==int:
#     print("Ədəd tip daxil edin:")
#     secondNumber = input("Ilk ədədi daxil edin: ")
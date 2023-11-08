#task 1
# n = int(input())
# count = 0
# for i in range(n+1):
#     count += i
# while n>0:
#     count+=n
#     n-=1
# print(count)

# task 2
# n = int(input())
# count = 0 
# while n>0:
#     count+=1
#     n//=10

# print(count)


# task 3
# n,m = map(int,input().split())
# def primitiveNumber(number):
#     count = 0
#     for i in range(2,number):
#         if number%i == 0:
#             count+=1
#     if count==0:
#         return True
#     else:
#         return False

# for i in range(n,m+1):
#     if(i<0) or i ==0 or i == 1:
#         pass
#     elif(primitiveNumber(i)):
#         print(i)
   


# task 4
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# task 5
# n = int(input())
# number = 0
# print(str(n)[::-1])
# while n>0:
#     number *=10
#     number+= n%10
    
#     n//=10
# print(number)

# ters = ""
# while n>0:
#     ters += str(n%10)
#     n//=10

# print(ters)


# task 6

# s = input()
# l = len(s)

# def counter(sentence):
#     l = len(sentence)
#     numbers = 0
#     letters = 0
#     for i in range(l):
#         if sentence[i].isdigit():
#             numbers+=1
#         elif sentence[i].isalpha():
#             letters+=1
#     return [numbers,letters]
# answer = counter(s)
# print("Herfler:",answer[1]," Ededler",answer[0]," Simvollar",l-(answer[0]+answer[1]))


# task 7
# import datetime
# n = datetime.datetime(2019,11,15)
# print(n.strftime("%d"),n.strftime("%B"),n.strftime("%Y"))


# task 8

# import time
# from datetime import datetime
# from datetime import timedelta
# x = datetime.now() + timedelta(days=8,hours=12,minutes =20)
# print(x)

# Get the current date and time
# now = datetime.now()

# # Add a timedelta of 3 days to the current date and time
# future_date = now + timedelta(days=3)

# # Subtract a timedelta of 1 hour from the current date and time
# past_date = now - timedelta(hours=1)

# # Compare two timedelta objects
# if delta < delta2:
#     print("delta is less than delta2")

# import datetime
# from datetime import datetime
# n = datetime.datetime(2023,7,7, 15,23,52 )
# n  = datetime.datetime.now()
# print(n)
# delta = n+ timedelta(days=8)
# print(delta)
# print(int(n.strftime("%d")),n.strftime("%B"),n.strftime("%Y"),int(n.strftime("%H")),n.strftime("%M"),n.strftime("%S"))



# task 9
# def sum(*args):
#     summ = 0
#     for i in args:
#         summ += i



# print(sum(3,7,9,15))


# task 10 - 11

# class Course:
#     def __init__(self,course,teacher,price,duration):
#         self.course = course
#         self.teacher = teacher
#         self.price = price
#         self.duration = duration

#     def show(self):
#         print(f"Best {self.price} for this {self.course}")


# elements = Course("ga","nasib",340,6)

# print(f"This {elements.course} is taught by {elements.teacher}, duration is {elements.duration} and price is {elements.price} ")



#task 12-13

# class Course:
#     def __init__(self,*args):
#         self.course = args[0]
#         self.teachers = args[1]

#     def printer(self):
#         print(self.course,self.teachers)

# e = Course("Mathematics Mrs." ,"Johnson")
# e.printer()




# class Course:
#     def __init__(self,**kwargs):
#         self.course = kwargs.get("course_name")
#         self.teacher = kwargs.get("teacher_name")

#     def printer(self):
#         print(self.course,self.teacher)
# course_info = {
#     'course_name': 'Mathematics',
#     'teacher_name': 'Mrs. Johnson'
# }
# e = Course(**course_info)
# e.printer()


# print(0 and 1 and 0)
# print(1 and 0)

# print(1 or 0)
# print(0  or 1)

# print(6 or 3)
# print(19 or 5 or 4)
# print(2 or 0 or 4)

# print(6 and 1 and 12 and 23)


# print(bool(0 and 5),0 and 5)
# print(bool(10 and 5), 10 and 5)
# print(bool(5 and 0), 5 and 0)
# print(bool(5 and 1), 5 and 1)
# print(bool(0 or 0), 0 or 0)
# print(bool(1 or 4),1 or 4)
# print(bool(4 or 1),4 or 1)
# print(bool(4 and 1),4 and 1)
# print(bool(4 or 0),4 or 0)

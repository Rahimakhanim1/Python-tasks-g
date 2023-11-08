# import datetime
# from datetime import timedelta
# n = input("Dogum gununuzu daxil edin: ")
# days = n.strftime("%A")    


birthday = input("Please enter your birthday (YYYY-MM-DD): ")

year, month, day = map(int, birthday.split('-'))

import datetime
current_date = datetime.date.today()

birthdate = datetime.date(year, month, day)
print(birthdate)
age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
print(f'siz heyatda {age*365*24*60*60} saniye, {age*365*24*60} deqiqe, {age*365*24} saat,{age*365} gun, {age*12} aydir ki yasayirsiz')

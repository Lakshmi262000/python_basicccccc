# a = 100
# b = 1.5
# c = a + b
# print(type(c))

# a = 100
# a = float(a)
# print(type(a))
# print(a)

# num = 5 + 2.0
# print(type(num))    
# print(num)

# int(5.7) 
# print(int(5.7))

# float("3.14")
# print(float("3.14"))

# str(42)
# print(str(42))
# print(type(str(42)))

# lis = [1, 5, 4, 2, 4, 3, 4, 5, 5]
# v_list =[]
# for i in lis:
#     if i not in v_list:
#         v_list.append(i)
# print(v_list)


# from typing import Union


# def calc_on_numbers(a: Union[int, float], b: int) -> int:
#     print(f"{a} + {b} = {a + b}")
#     print(f"{a} - {b} = {a - b}")
#     print(f"{a} * {b} = {a * b}")

#     if b != 0:
#         print(f"{a} / {b} = {a / b}")
#     else:
#         print("Division by zero is not allowed.")


#     return a + b


# calc_on_numbers(10, 5)
# calc_on_numbers(20.6, 4)


# print("hi \"python\"")

# print("hi \'python\'")

# print('hi "python"')

# print("message1\n\n\nmessage2")

# print("message1\tmessage2")
# print()
# print("message2")




# print("Your learning path: \n\t-Python Basics\n\t-Python Engineering\n\t-AI")

# 
# print("""Your learning path:
# # \t-Python Basics
# # \t-Python Engineering
# # \t-AI""")



# print("""Your learning path:
# \n\t-Python Basics
# \n\t-Python Engineering
# \n\t-AI""")



# print("my name is lakshmi")
# print("lakshmi is learning python")
# print("lakshmi wants to become a python developer")




# name = "lakshmi"
# print("my name is name")
# print("name is learning python")
# print("name wants to become a python developer")





# name = "lakshmi"
# # print("my name is ",name)
# # print(name," is learning python")
#  print(name," wants to become a python developer")



# name = "saleem"
# print("my name is ",name)
# print(name," is learning python")
# print(name," wants to become a python developer")



# name = "saleem"
# language = "python"
# print("my name is ",name)
# print(name," is learning",language)
# print(name," wants to become a",language,"developer")


# name = "lucky"
# language = "SQL"
# print("my name is ",name)
# print(name," is learning",language)
# print(name," wants to become a",language,"developer")





# input("Enter your name: ")


# name =input("Enter your name: ")
# print("my name is ",name)




# name =input("Enter your name: ")
# country = "pakistan"
# print("my name is ", name , "and i am from" , country)



# name =input("Enter your name: ")
# country = "ukraine"
# print("my name is ", name , "and i am from" , country)




# x = "a"
# print(x)

# y = input("enter value: ")
# print(y)   



# 'hello' .upper()



from unicodedata import name


text = "hi"
number = 5

# print(text)
# print(number)

# print(type(text))
# print(type(number))


# print(len(text))
# print(len(number))

# print(len(text))
# print(len(str(number)))


# print(text.upper())
# print(number.bit_length())


age = 25
height = 5.0
name = "isha"
student = True
phn_number = None


# print(type(age))
# print(type(height)) 
# print(type(name))
# print(type(student))
# print(type(phn_number))

# print("age is",age)
# print("height is",height)
# print("name is",name)
# print("student is",student)
# print("phone number is",phn_number)


# print(len(str(age))) 
# print(len(str(height))) 
# print(len(name))
# print(len(str(student)))
# print(len(str(phn_number)))  



# age = 25
# print (type(age))
# print("your age is:" + str(age))

# age_1= age + 10
# print (age_1)
# print(type(age_1))


# password = "1234fg"
# print(len(password))





# password = "1234fggfvjhjlfg7"
# if len(password) < 8:
#     print("password is too short")

# print(len(password))




#math.....

# text = """
# Python is easy to learn.
# Python is powerful.
# # Many people love python.
# """
# # print(text.count("Python"))
# # print(text.count("python"))



##########     transformations     #########

# price = "1890,985"
# print(price.replace(",", "."))


# phone_number = "123-456-7890"
# print(phone_number.replace("-", "/"))
# print(phone_number.replace("-", ""))



# price = "$ 1,940.99"
# print(price.replace("$", "").replace(",", ""))

# fanta  =  "+49 (176) 123-4567"
# print(fanta.replace("+", "",).replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print(full_name)  


# name = "lucky"
# age = 25
# is_student = False
# print("My name is " + name + ", I am " + str(age) + " years old, and it is " + str(is_student) + " that I am a student.")
# print(f"My name is {name}, I am {age} years old, and it is {is_student} that I am a student.")


# print(f"2 + 3 = {2 +3}")
# print(f"5 * 4 = {5*4}")
# print(f"10 / 2 = {10 / 2}")


# print(f"{{This is me}}")


# stamp = "2026-05-25 12:30"
# print(stamp.split(" "))
# print(stamp.split("-"))

# csv_file = "1234,Max,USA,1970-10-05,M"
# print(csv_file.split(","))


# print("haha"*3)

# s = "cat"
# # print (s[1])
# print (s[-3])

# print("="*30)

# text = "lachimik"
# # print(text[2])
# # print(text[-4])
# print(text[2:])
# print(text[2:6])
# print(text[2: :2])
# print(text[-8: :3])

######################### INDEXES AND SLICING##############################
# date = "2026-09-23"
# print(date[0:4])
# print(date[5:7])
# print(date[8: ])
# print(date[-5:-1])

# text = "   love you bacche"
# print(text)
# print(text.lstrip())
# print(len(text))
# print(len(text.strip()))
# print(len(text) - len(text.strip()))
# print(len(text) == len(text.strip()))
# nr_of_spaces = len(text) - len(text.strip())
# is_clean = len(text) == len(text.strip())
# print ("nr of spaces : ", nr_of_spaces)
# print ("Is my data clean?" , is_clean)

# text = "####abc####"
# print(text.strip("#"))


# text = "python PROGRAMMING"
# print(text.lower())
# print(text.upper())

# search = "Email"
# data = "email"
# print(search == data)

# search = "Email".lower()
# data = "email".lower()
# print(search == data)

# search = "     Email"
# data = "email    "
# print(search == data)

# search = "     Email".lower().strip()
# data = "email    ".lower().strip()
# print(search == data)

# text = "968-Maria, ( D@t@ Engineer );; 27y   "




######################### SEARCH ###########################

# phone = "+49-176-123456"
# print(phone.startswith("+49"))
# print(phone.startswith("+47"))

# email = "lucky26.k@gmail.com"
# print(email.endswith ("gmail.com"))
# print(email.endswith ("outlook.com"))


# file = "data_backup.csv"
# print(file.endswith(".csv"))
# print("@" in email)

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"
print(phone1[4:])
print(phone2[3:]) 
print(phone3[5:])
print(phone1.find("-"))



























































































































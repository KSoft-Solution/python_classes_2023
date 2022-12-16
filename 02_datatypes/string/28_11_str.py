# # var = 12
# # print(var) # 12

# # var1 = 23
# # var2 = 34

# # var1,var2 = 23,34
# # print(var1,var2)

# # print('ashok sahu')

# name = 12345 #type(string)
# print('variable value: ',name)
# print('variable type: ',type(name))
# print('variable id: ',id(name))

# name = 1234 #type(string)
# print('variable value: ',name)
# print('variable type: ',type(name))
# print('variable id: ',id(name))
# job  = 'software services'

# print(name,job) # ashok sahu software services
# print('name : ',name,',job : ',job)
# print(f'name : {name} , job : {job}')
# print({'name':name,'job':job})

# # formated string(f string)



# data types in python

# str = 'i am a string'
# print(str)
# print(type(str)) # <class 'str'>

# int()
# str()
# float()
# complex()
# list()
# dict()
# set()
# tuple()
# bool()

# str2 = str(12)
# print(str2)
# print(type(str2))

# num = 1
# print(num) # 1
# print(type(num)) #int

# num = bool(1)
# print(num) # True
# print(type(num)) #bool

# num = bool(True)
# print(num) # True
# print(type(num)) #bool

# num = bool(0)
# print(num) # False
# print(type(num)) #bool

# num = bool(False)
# print(num) # False
# print(type(num)) #bool

# num = bool('')
# print(num) # False
# print(type(num)) #bool

# num = bool([])
# print(num) # False
# print(type(num)) #bool

# num = bool(None)
# print(num) # False
# print(type(num)) #bool

# num = bool('ashok')
# print(num) # True
# print(type(num)) #bool


num1 = 12
print(num1) # 12
print(type(num1)) #int

num1 = int(12)
print(num1) # 12
print(type(num1)) #int

num1 = int('12')
print(num1) # 12
print(type(num1)) #int

num1 = int('12a') #ValueError: invalid literal for int() with base 10: '12a'
print(num1) # 12
print(type(num1)) #int 
import string

str1 = "Hello.python"
str2 = "."

print(type(str1))
print(str1.find('-'))

if (str1.find('-')+1):
    print(111)
else:
    print(222)

print(str1.index(str2))  # 结果5
print(str1[:str1.index(str2)])  # 获取 "."之前的字符(不包含点)  结果 Hello
print(str1[str1.index(str2):])  # 获取 "."之前的字符(包含点) 结果.python

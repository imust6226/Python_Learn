#coding = utf-8


"""pi_digits.txt文件的末端有空行"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(" read()到达文件末尾时返回一个空的字符串")
    print(contents)

    print("\n使用rstrip()函数可以删除末尾的空字符串")
    print(contents.rstrip())


"""
    可以将文件名传递给open()方法，也可以传递文件的路径
    1、绝对路径：
        1.1、Linux的绝对路径：/tmp/pi_digits.txt
        1.2、Window的绝对路径: C:\\Users\tmp\pi_digits.txt
    2、相对路径
        2.1、Linux的相对路径：text_file/pi_digits.txt
        2.2、Window的相对路径： text_file\\pi_digits.txt
"""

"""
file_path = 'C:\\Users\\Admin\\Desktop\\pcc-master\\tmp\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip() + '\n')

"""
print("\n逐行读取文件内容\n")

"""逐行读取时，由于每行有换行符，所以每行都会出现一个空白行"""

file_path = 'pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()



pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print("\n使用strip()函数，可以删除每行左边的空格\n")
pi_string_new = ''
for line in lines:
    pi_string_new += line.strip()

print(pi_string_new)
print(len(pi_string_new))

print("\n运行百万位的pi文件，只要内存足够大，没有限制\n")
file = "file_million_digits.txt"

with open(file) as file_object:
    lines = file_object.readlines()

pi_string1 = ''
for line in lines:
    pi_string1 += line.strip()

print(pi_string1[:52] + "...")

birthday = input("Enter your birthday,in this form mmddyy")
if birthday in pi_string1:
    print("Your birthday appears in the first million digit of pi")
else:
    print("Your birthday does'n appears in the first million digit of pi")


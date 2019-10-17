#coding = utf-8

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)

name = 'ada lovelace'
print(name.title())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name.title())

print("\tPython\tJava\tJavascript\tC++\tPerl\tRun")
print("Languages:\n\tPython\n\tJava\n\tC++\n\tPerl")

#删除空白 方法： rstrip() lstrip() strip
favourite_language = '  python  '

#右侧空格 删除
pirnt(favourite_language.rstrip())
#左侧空格 删除
pirnt(favourite_language.lstrip())
#两侧空格 删除
pirnt(favourite_language.rstrip())



# 使用双引号和单引号
msg = "One of Python's strengths is its diverse community."

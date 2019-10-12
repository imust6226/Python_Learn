#coding = utf-8

import re


"""
处理字符串首尾的空格，可以使用strip()，去掉首尾的空格
split()仅支持处理单个分割符；而re.split()支持多种分割符号处理
re.split()，正则表达式使用小括号和中括号的唯一区别是；中括号不
会把分割的符号计入分割后形成的列表中；但是小括号会把分割的符号
计入分割后列表中。
正则表达式: 分割符为分号、逗号、空格、句号以及分隔符前后有若干空格都需要匹配
小括号或者中括号内的分隔符是或的关系，外面则是且的关系
line = "asdf fjkd ; aded,fjek,asfd,foo"
result = re.split(r'[;,\s。]\s*', line)
result = ['asdf', 'fjkd', 'aded', 'fjek', 'asfd', 'foo']
result = re.split(r'(;,\s。)\s*', line)
result = ['asdf', ' ', 'fjkd', ';', 'aded', ',', 'fjek', ',', 'asfd', ',', 'foo']       
result = re.split(r'\s*(?:;|,|\s)\s*', line)
result = ['asdf', 'fjkd', 'aded', 'fjek', 'asfd', 'foo']
"""


class ReSplit():


    def __init__(self):
        # line1 这个字符串有前面有空格
        self.linea = "asdf fjkd ; aded,fjek,asfd,foo"
        # line2 这个字符串在标点符号后面有空格
        self.lineb = "asdf fjkd ; aded,fjek,asfd, foo"
        # line3 这个字符串在标点符号前面和后面都有空格
        self.linec = " asdf fjkd ; aded,fjek,asfd, foo"
        
    def null_capture_group1(self, line):
        """正则表达式不使用 捕获组 的模式，即使用中括号[]"""
        result = re.split(r'\s*[;,\s。]\s*', line)
        return result
    
    def null_capture_group2(self, line):
        """正则表达式不使用 捕获组 的模式，即使用中括号[]"""
        result = re.split(r'[;,\s。]\s*', line)
        return result
        

    def capture_group1(self, line):
        """正则表达式使用 捕获组 的模式，及使用小括号()"""
        result = re.split(r'\s*(;|,|\s)\s*', line)
        return result

    def capture_group2(self, line):
        """正则表达式使用 捕获组 的模式进行分组，使用 ?: 开头的正则，"""
        result = re.split(r'(?:;|,|\s)\s*', line)
        return result


re_split = ReSplit()
return_lista = re_split.null_capture_group2(re_split.linea)
print(return_lista)
return_listb = re_split.null_capture_group2(re_split.lineb)
print(return_listb)
return_listc = re_split.null_capture_group2(re_split.linec)
print(return_listc)

return_lista = re_split.capture_group1(re_split.linea)
print(return_lista)

return_lista = re_split.capture_group2(re_split.linea)
print(return_lista)


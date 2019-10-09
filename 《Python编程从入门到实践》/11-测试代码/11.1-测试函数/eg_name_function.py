#coding = utf-8


"""
    两个函数：
    第一个函数：没有中间名字
    第二个函数：可以处理中间名字
"""
def get_formatted_name1(first, last):
    """"
        生成一个整洁的名字，首字母大写
    """
    full_name = first + ' ' + last
    return full_name.title()

def get_formatted_name2(first, last, middle):
    """
        生成一个整洁的名字，首字母大写
    """
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
    
    
def get_formatted_name3(first, last, middle=''):
    """
        能够正确处理中间名字；
        判断中间名字是否为True，通常不为空，则True
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()
        

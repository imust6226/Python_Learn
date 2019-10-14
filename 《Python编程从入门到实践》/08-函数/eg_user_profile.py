#coding = utf-8

"""使用任意数量的关键字实参调用函数"""

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first'] = first
    profile['last'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile1 = build_profile('albert', 'einstein', location = 'princeton',
                             fielf = 'physics')
print (user_profile1)


others = {'sex':'female', 'age':28, 'hobby':'Love to Sing!'}

#任意数量的关键字实参需要指定变量名哟，最好有意义，能够读明白是指的什么意思，这个样子不行。
user_profile2 = build_profile('lcuy', 'mark', user_info = others)
print(user_profile2)


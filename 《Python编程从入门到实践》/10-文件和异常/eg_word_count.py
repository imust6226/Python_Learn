#coding = utf-8

filename = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'siddhartha.txt', 'Python.txt']

def count_words(filename):
    """计算一个文件大概有多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    
    
    
    except FileNotFoundError:
        print("Sorry,The File " + filename + " Not Yet Found。")

    # 这个异常可以什么都不用做，直接 pass掉了
    except Exception:
        pass
    
    else:
        words = contents.split()
        num_words = len(words)
        print("The File " + filename + " has about " + str(num_words) + " words")
        

def caluate(filename):
    for file in filename:
        count_words(file)


caluate(filename)

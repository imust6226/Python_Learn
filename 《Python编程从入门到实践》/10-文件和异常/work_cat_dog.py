#coding = utf-8

class CatAndDog(object):
    def __init__(self, file1, file2):
        """将文件的名字放在一个空的列表中储存起来"""
        self.files = []
        self.files.append(file1)
        self.files.append(file2)
        
    

    def read_file(self, num = 1):
        for file in self.files:
            try:
                with open(file) as file_object:
                    contents = file_object.read()
            except FileNotFoundError:
                print("Sorry,The File " + file + " Has't Not Yet Found!")
            else:
                print("这是第 " + str(num) + " 文件的内容。")
                print(contents)
                num +=1
                

    def judge_num(self):
        """这个方法判断选择文件的位置，只能是0或者1"""
        msg = input("The File which you'll have to decide to move from:\n")
        try:
            num = int(msg)
        except ValueError:
            print("Please give a numbe instead of words.")
        else:
            if num > 1 or num < 0:
                print("Please give a number which is neither '1' or '0'")
            else:
                #测试代码，看看num的类型是否是int型
                #print(type(num))
                return num
                

    def move_file(self, num):
        """这个文件决定将文件A中的内容移动到文件B中去"""
        if num == 0:
            try:
                with open(self.files[0]) as file_object:
                    lines = file_object.readlines()
            except FileNotFoundError:
                pass
            else:
                try:
                    with open(self.files[1], 'a') as file_object2:
                        for line in lines:
                            file_object2.write( "\n" + line.strip())      
                except FileNotFoundError:
                    print("FILE NOT FOUND")
                else:
                    print("contents in file " + self.files[0] + " moved away!")
                    
        else:
            
            try:
                with open(self.files[1]) as file_object:
                    lines = file_object.readlines()
            except FileNotFoundError:
                pass
            else:
                try:
                    with open(self.files[0], 'a') as file_object2:
                        for line in lines:
                            file_object2.write("\n" + line.strip())
                        
                except FileNotFoundError:
                    print("FILE NOT FOUND")
                else:
                    print("contents in file " + self.files[1] + " moved away!")
                    
            
                        
                
        
                
            
        
cd = CatAndDog("cat.txt", "dog.txt")

cd.read_file()
num = cd.judge_num()
cd.move_file(num)


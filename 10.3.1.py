#coding = utf-8

print("give me two numbers,and i'll divide them")
print("enter 'q' to qiut.\n")

class ExceptionCatch():
    
    def __init__(self, name = 'This', score = 100):
        self.name = name
        self.score = score
        self.fileName = 'alice.txt'
        
    def divideNum(self):
        while True:
            first_num = input("\nyour first num: ")
            if first_num == 'q':
                break
            second_num = input("your second num: ")
            if second_num == 'q':
                break
            try:
                answer = int(first_num) / int(second_num)
            except ZeroDivisionError:
                print("you can't divide by zero\n")
            else:
                print(answer)

    def fileRead(self):
        try:
            with open(self.fileName) as file:
                content = file.read()
        except FileNotFoundError:
            print("the file "+ self.fileName+ " is't found.")
        else:
            words = content.split()
            num_words = len(words)
            print("ths file "+self.fileName+" contains words as many as "+str(num_words))
            
        

ec = ExceptionCatch()
ec.fileName = "D:\\1etrip系统\\临时.txt"
ec.fileRead()


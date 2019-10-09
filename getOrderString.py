#coding = utf-8

import base64

class base64_decrypt():
    """
        这个加解密的类还有很多的问题：
        1、针对数字加解密没有问题，但是在写入文件的时候，遇到了"\n"这个符号问题，导致解密读取文件的时候需要截取；
        2、针对普通字符串的时候，需要将原数据origin.encode('utf-8')；
        3、待完善
    """

    def __init__(self):
        """
            默认两个文件路径：
            filename1是源数据文件路径
            filename2是Base64加密后的文件路径
            filename3是Base64解密内容
        """
        self.filename1 = "D:\\base64_origin.txt"
        self.filename2 = "D:\\base64_encrypt.txt"
        self.filename3 = "D:\\base64_decrypt.txt"

    def num_range(self, x, y):
        """
            确认源数据的起讫点
        """
        nums = range(x, y+1)
        print("********源数据写入中********")
        try:
            for num in nums:
                with open(self.filename1,'a') as f:
                    
                    """
                        这里的nums类型是int型，需要转化为str型,
                        所以需要str(num)写入文件
                    """
                    f.write(str(num) + '\n')
                    
            print("********数据写入完毕********")
        except FileNotFoundError:
            print("File's Not Found,Please Check That Again!")
        else:
            pass
        
    def num_base64_encrypt(self):
        """
            将加密后的文件写入到文件中去，这里有几个问题
            1、base64.b64encode()函数返回的byte类型，不能直接写入文件
            2、需要将返回至numBase64通过str(numBase64)转化为字符串形式
            3、写入的文件待有字节格式，如 "b'MjAxODA5MTkyOA=='"
            4、所以需要使用字符串截取str(numBase64[2:-1])，截取后格式如"MjAxODA5MTkyOA=="
        """
        try:
            with open(self.filename1) as f:
                print("********Base64加密数据写入中********")
                for num in f:
                    
                    #numBase64_origin = base64.b64encode(num.encode('utf-8'))
                    #这里不需要进行utf-8加密，所以也不需要截取
                    numBase64_origin = base64.b64encode(num)
                    
                    #这里 我也不知道为什么也要做一次转换工作，才能写入正常的格式
                    #numBase64 = str(numBase64_origin[2:-1])
                    numBase64 = str(numBase64_origin)
                    with open(self.filename2, 'a') as f2:
                        #f2.write(numBase64[2:-1] + '\n')
                        f2.write(numBase64 + '\n')
                print("********Base64加密数据写入完毕********")
        except FileNotFoundError:
            print("File's Not Found,Please Check That Again!")
        else:
            pass

    def num_base64_decrypt(self):
        """
            解密Base64字符串
        """
        try:
            with open(self.filename2) as f:
                print("********Base64解密数据写入中********")
                for num in f:
                    try:
                        numBase64_origin = base64.b64decode(num.encode('utf-8'))
                        numBase64 = str(numBase64_origin)
                    except Exception:
                        print("********解密异常**********")
                    else:
                        with open(self.filename3, 'a') as f3:
                            # 由于之前写入数据的时候有换行符号，所以这里截取需要更多
                            f3.write(numBase64[2:-3] + '\n')
                print("********Base64解密数据写入完毕********")
        except FileNotFoundError:
            print("File's Not Found,Please Check That Again!")
        else:
            pass
        

base64_num = base64_decrypt()
nums = base64_num.num_range(2016010000, 2016129999)
base64_num.num_base64_encrypt()
base64_num.num_base64_decrypt()



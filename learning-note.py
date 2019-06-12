#encoding: utf-8
#上面那句不加就不能写中文
#python learning note
#索引
#字符串"abcdef"
#从后往前索引   -6  -5  -4  -3  -2  -1
#从前往后索引    0   1   2   3   4   5
#             | a | b | c | d | e | f |
#从前往后截取  :   1   2   3   4   5   :
#从前往后索引  :  -5  -4  -3  -2  -1   :
#字符串用+相连，用*重复
#截取时,0就是:，只有:时代表全员
#第一个参数是起始编号，第二个是终止编号，第三个是步长，可省。

s="abcdef"
print s            #abcdef
print s[:]         #abcdef  
print s[3]         #d (单纯索引)
print s[-5]        #b
print s[2:]        #cdef
print s[-2:]       #ef  
print s[1:4]       #bcd
print s[0:-1:2]    #ace 
print s[1::2]      #bdf
print s * 2        #abcdefabcdef
print s + ", " + s #abcdef, abcdef

#关于input，python2.x
#input()可输入数字和字符串，输入string需要加引号，否则无法识别
#raw_input()只能输入字符串，得到的字符串后有\r
#使用raw_input()得到的字符串需要用.rstrip()
name = input("input your name?")         #"ahem"
name                                     #'ahem'
name = raw_input("rawinput your name?")  # ahem
name                                     #'ahem\r'
print("hello, " + name.rstrip() + "!")
'''age = input("how old are you?")
age = int(age)
pi = input("pi?3.14 or 3.141")
pi = float(pi)'''
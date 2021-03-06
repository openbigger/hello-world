#encoding: utf-8
#上面那句不加就不能写中文
#python learning note
#风格规范
#https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/

#布尔
#0， None, [], {}, “” 都被认为是false.
#if x: 表示的是 if x is not None
#不要使用if x == false:，使用if not x:

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

#input，python2.x
#input()可输入数字和字符串，输入string需要加引号，否则无法识别
#raw_input()只能输入字符串，得到的字符串后有\r
#使用raw_input()得到的字符串需要用.rstrip()
'''name = input("input your name with \"\":")         #"ahem"
name                                               #'ahem'
name = raw_input("rawinput your name?")            # ahem
name                                               #'ahem\r'
print("hello, " + name.rstrip() + "!")
age = input("how old are you?")
age = int(age)
pi = input("pi?3.14 or 3.141")
pi = float(pi)'''

#print
sum = 7
print("sum is %d"%sum) #sum is 7
print("sum is ", sum)  #('sum is ', 7)
print("\"sum\"") #"sum"
print sum,       #句尾加‘,’不换行，空格分割
print sum
#class
#class的属性可以在实例中随时添加和删除，不用在class中声明
#built-in attr, 前后有__
class Dog(object):#大写开头，没有父类就继承自object
    def __init__(self,name):
        self.name = name
    def sit(self):#self必须的，用的时候不用写
        print(self.name + " is sitting.")
my_dog = Dog("bibi")
my_dog.sit()
if my_dog:           #==hasattr(my_dog,'age')
    my_dog.age = 0.3 #==setattr(my_dog,'age',0.3)
    the_age = my_dog.age #==getattr(my_dog,'age')
my_dog.age = 0.7 #==setattr(my_dog,'age',0.7)
del my_dog.age   #==delattr(my_dog,'age')
#直接使用，不能久存
Dog("mimi")
Dog(my_dog.name).sit
#Variables and Strings

#print("hello world")
msg = "hello world-msg"
#print(msg)
first_name = "lily"
first_name = 'ahem'
full_name = msg + " " + first_name
#print(full_name)

#Lists

bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]
#print(first_bike + ' '+ last_bike)
for bike in bikes:
    print(bike)
anther_bikes = []
for bike in bikes:
    anther_bikes.append(bike)
    print(anther_bikes)
squares = []
for i in range(1,11):
    squares.append(i**2)
   # print("%d"%(squares[i-1]))
#print(*squares, sep = ' ')   #<<<<<====星号不能用
#print str(squares)
anther_squares = [x**2 for x in range(1,10)]
#print str(anther_squares)
finishers = ['sam', 'bob', 'ada', 'bea', 'mee', 'woo']
first_two = finishers[0:2]#<<<<<====== 0可以省略
#print(first_two)
middle_two = finishers[2:4]
#print(middle_two)
last_two = finishers[4:]#<<<<=======不能写成[4:-1]
#print(last_two)
copy_of_bikes = bikes#[:]
#print("copy bike: ",copy_of_bikes)

#Tuple
dimensions = (1920,1080)

#If statements
if 'trek' in bikes:
    print("You can vote!")

#Dictionaries
alien = {'color':'green', 'point':5}
print("the alien's color is "+ alien['color'])
print(("the alien's point is %d" + "!")%alien['point'])#<<<<====数字字符串混入

alien['x_position'] = 8
fav_numbers = {'eric':17, 'kenny':'4'}
fav_string=[]
for name, number in fav_numbers.items():
    fav_string.append(name + ' loves ' + str(number))
    print(fav_string[-1])

alien_keys = alien.keys()
alien_values = alien.values()
alien_one_value = alien[alien_keys[1]] #x_postion:8

#input and raw_input
'''
name = raw_input("what's your name?")
name
print("hello, " + name.rstrip() + "!")
age = input("how old are you?")
age = int(age)
pi = input("pi?3.14 or 3.141")
pi = float(pi)
'''
#while loop
msg = 'q'
while msg != 'q':
    msg = raw_input("what's your message(q to quit):")
    msg = msg.rstrip()
    print("\"%s\""%msg)
msg

#function
def add_number(x=3,y=4):
    return x+y
sum = add_number() #用默认值不需要输入参数
sum
sum = add_number(5,6)
print("sum is %d"%sum)

def yield_test(n):  
    for i in range(n):  
        yield call(i) #返回值但并不退出函数
        print("i= %d"%i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
for j in yield_test(5):  
    print("j = %d"%j)  

#class
class Dog(object):#大写开头，没有父类就继承自object
    def __init__(self,name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting.")
my_dog = Dog("bibi")
my_dog.sit()

class SarDog(Dog):
    def __init__(self,name):
        super(SarDog,self).__init__(name)
    def search(self):
        print(self.name + " is searching.")
her_dog = SarDog("maomao")
her_dog.search()
her_dog.sit()

SarDog('mimi').search()
my_dog.age = 0.3

#working with files
filename = "txt/hellofile.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
print "print hellofile.txt 1:"
print lines
print "print hellofile.txt 2:"
for line in lines:
    print line,#加个逗号就不换行
print "print hellofile.txt 3:"
for line in lines:
    print line.rstrip()#去掉\n

with open(filename,'a') as file_object:
    file_object.write("I like you.\n")#每次运行，最后面添加一行
file_object.close()

#store data with json
import json
number = [2,3,5,7,11,13]
filename = "json/number.json"
f_ojbk = open(filename,'w')
json.dump(number,f_ojbk)
f_ojbk = open(filename)
j_num = json.load(f_ojbk)
f_ojbk.close()
print j_num


#Exception
'''
prompt = "how many tickets do you need?"
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError, Argument:
    print Argument, "\nplease try again."
else:
    print("buy successfully.")
'''
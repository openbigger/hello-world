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
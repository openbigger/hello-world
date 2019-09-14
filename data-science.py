import numpy as np
#在要看值的地方打断点F9，F5以后用F10（单步调试）看各变量的变化
'''
my_list = [1,2,3,4]
my_array = np.array(my_list)
my_array_2D = np.array([[1,2,3],[4,5,6]])
a = my_array_2D[:,0] #[rows,columns]
a = my_array > 3
#a = my_list > 3 不是np不可以

a = my_array + my_array
a = my_array.shape #(4,)
a = my_array_2D.shape #(2,3)
a = type(my_array)
# np.append(my_array,1)

temp_array = np.eye(3) #identity matrix 单位矩阵
a = temp_array[0,0]
temp_array = np.random.random(3) #1x3
temp_array = np.random.random((4,5)) #4x5
temp_array

# slicing 从矩阵中取一部分 
# 取出来的部分其实指向了原矩阵，取出来的某个元素改变了原矩阵也改变，反之亦然
# 1. 取一小块
a = my_array_2D[:,1:3] #([2,3],[5,6])
a[0,1] = 77 #([2,77],[5,6])
my_array_2D[0,2] = 88 
'''
# 2. 取一行或列
# 用行列标加行列范围将生成一维数组
# 仅仅用行列标范围才能生成二维数组
temp_array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = temp_array[1,:] #[5,6,7,8] 用行列标将生成一维
row_r2 = temp_array[1:2,:] #[5,6,7,8] shape (1,4) 用范围生成二维
col_r1 = temp_array[:,2] #[3,7,11] shape (3,) 一维
col_r2 = temp_array[:,2:3] #[3,7,11] shape (3,1) 
'''
# indexing 选取矩阵元素生成新矩阵
a = temp_array[[1,0,2],[2,1,0]] #[7,2,9] temp_array[[行号],[列号]]
b = [temp_array[1,2],temp_array[0,1],temp_array[2,0]]
# a和b效果一样

# subsetting
c = temp_array[1,2]

temp_array[1,2] = 88 #a和b是新生成的，不受影响。c是变量也不受影响。

b = [1,0,3,]
c = np.arange(3)
a = temp_array[c,b] 
a +=10

# test print
print('a')
'''
#data science np
#creating arrays
a = np.array([1,2,3])
b = np.array([(1.5,2,3),(4,5,6)], dtype = float)
c = np.array([[(1.5,2,3),(4,5,6)],[(3,2,1),(4,5,6)]],dtype = float)
d = np.zeros((3,4))
e = np.ones((2,3,4), dtype=np.int16)
d = np.arange(10,30,5) # 10~30(不含)，每5个取一个
e = np.linspace(0,2,10) # 0~2（含）,分成10个
e = np.full((2,4),8) #填8的2x3矩阵
f = np.eye(4) #4x4特征矩阵
g = np.random.random((2,2)) #random函数下面有很多功能，rand/randn/randint等，这里返回[0.0,1.0)随机数
h = np.empty((3,2))
'''
#I/O
np.save('my_array', a) #文件后缀默认npy
loadarray = np.load('my_array.npy') #这种存取的数据vscode看不见
np.savez('array.npz',a,b) #用7zip打开会看到arr_0/arr_1
loadarrays = np.load('array.npz')
loadarray = loadarrays["arr_0"] #之前存的a数组
loadtxt = np.loadtxt('txt/npfile.txt')

np.savetxt("txt/npfilesave.txt",loadtxt,delimiter=', ')
wavedata = np.genfromtxt('txt/triangularwave.txt',delimiter=',',skip_header=7)#以逗号为界，两列的二维数组，跳过前面7行文字
x = wavedata[0:3,0]#第一列的前三个数

#Data Types

xint64 = np.int64(x)
xfloat32 = np.float32(x)
xbool = np.bool(3)

#Inspecting your array
tshape = temp_array.shape
tlen = len(temp_array) #不能用·len
tdim = temp_array.ndim
tsize = temp_array.size
ttype = temp_array.dtype
tasint = temp_array.astype(int)
'''
#array mathematics
g = a-b
subab = np.subtract(a,b)
expb = np.exp(b)
s = np.sqrt(b)
sina = np.sin(a)
cosb = np.cos(b)
loga = np.log(a)
edotf=e.dot(f)
compareab = (a==b)
equalab = np.array_equal(a,b)
asum = a.sum()
bsum = b.sum()
amin = a.min()
bmax0 = b.max(axis=0)#取每列最大值
bmax1 = b.max(axis=1)#取每行最大值
bcumsum = b.cumsum(axis=1)
bstd = np.std(b)
g
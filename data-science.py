import numpy as np
#在要看值的地方打断点F9，F5以后用F10（单步调试）看各变量的变化
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
a

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
# 2. 取一行或列
# 用行列标加行列范围将生成一维数组
# 仅仅用行列标范围才能生成二维数组
temp_array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = temp_array[1,:] #[5,6,7,8] 用行列标将生成一维
row_r2 = temp_array[1:2,:] #[5,6,7,8] shape (1,4) 用范围生成二维
col_r1 = temp_array[:,2] #[3,7,11] shape (3,) 一维
col_r2 = temp_array[:,2:3] #[3,7,11] shape (3,1) 

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
a

# test print
print('a')

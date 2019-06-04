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
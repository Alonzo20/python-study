#_*_ conding:utf-8 _*_

'''
    循环

'''
# i = 0  #初始化一个变量
# while i<5 :  #进行一个条件判断
#     print('我爱你')   #条件为真要执行的部分
#     i+=1   #i变量 自增   i=i+1   i+=1
#
# print(i)  #当I自增到5 的时候不符合条件

#计算1到100 的和
# 1+2+3+4+5+6+7+。。。。+100
# i = 1 #初始化一个变量
# m = 0
# while i <=100:
#     m = m+i  #m = m+i  m =1  m = 3   m =6 m=10
#     # print(i)  #这个i在不停的迭代  就是不停的自增
#     i+=1   #2 3 4 5 6 7.....
# print(m)  #最后输出m的结果  就是将1到100累加起来的最后结果


'''
   总结： while 循环语句 可以依据条件来重复做一件事情
'''

'''
    while循环嵌套
'''
# i = 0
# while i < 5:
#     print('这个是外面循环i的第%d遍'%i)  #格式化输出
#     m = 0
#     while m <5:
#         print('这个是里面的循环m第%d遍'%m)
#         m+=1
#     i+=1
#     print('_'*20)


i = 0
while i < 5:  #控制行数
    m = 0
    while m <= i: #控制个数
        print('*',end = '') #表示print的结束符为空格 默认是换行
        m+=1
    i+=1
    print() #每行输出完毕之后输出一个换行 print默认是换行结尾


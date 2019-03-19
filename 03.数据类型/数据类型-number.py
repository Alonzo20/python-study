#_*_ coding:utf8 _*_

'''
    int
'''

# a = 1
# print(type(a)) #type是python中一个用来查看数据类型的函数

'''
    布尔类型
    对TRUE 不为零   错FALSE 0
'''
# a = True
# print(type(a))

'''
    字符串  string
    单引号或者双引号
'''
# a = '刘德华'
# name = "黎明"
# print(type(a))
# print(type(name))

# num = '1'
# num2 = 'True'  #带上引号的全部都是字符串
# print(type(num))
# print(type(num2))

# str1 = '"nihao"' #双引号成了字符串本身
# str1 = "'nihao'" #单引号成了字符串本身

# str1 = 'aaa\'bbbb'   #最外面的单引号是一对  里面的单引号通过 \ 转义
# print(str1)

str = 'abcdfeg'  #从0开始 下标
# print(str)
# print(str[0])
# print(str[1])
# print(str[2])

#截取字符串
# print(str[1:5])  #
# print(str[-2])  #
# print(str[2:])
# print(str[:2])

# print(str[1:5:2]) #步长
print(str[5:2:-1]) #步长
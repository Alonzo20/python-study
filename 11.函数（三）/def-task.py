#-*- conding:utf-8 -*-
''''''
'''
    函数，计算传入字符串的个数
'''
# def getLen(s):
#     if isinstance(s,str): #args1: 数据 args2：数据类型
#         return  len(s)
#     else:
#         return '类型错误'
# num = getLen('sdfdsf sdf')
# print(num)


'''
    函数，判断用户传入的字符串、列表、元组长度是否大于5
'''
# def getLen2(args):
#     if isinstance(args,(str,list,tuple)):
#         if len(args) > 5:
#             print('传入的对象长度大于5')
#         else:
#             print('传入的对象长度小于5')
#     else:
#         print('类型有误')
#
# getLen2(['a','b',1,2])


'''
    写入不定个数的字符串拼接第一个和最后一个字符串
'''
# def getStr(*args):
#     return args[0]+args[-1]
#
# print(getStr('1','2','3'))

'''
    传入多个参数，以list返回
'''
# def getList(*args):
#     li = []
#     for i in args:
#         li.append(i)
#     return li
#
# list01 = getList(1,2,3,4,5)
# print(list01)

'''
    定义一个函数，输入不定个数的数字，返回所有数字的和
'''
# def getSum(*args):
#     x = 0
#     for i in args:
#         x+=i
#     return x
#
# num = getSum(1,2,3,4,5)
# print(num)



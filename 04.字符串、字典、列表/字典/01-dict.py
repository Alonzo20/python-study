#_*_ conding:utf-8 _*_
'''
    创建字典

'''
# dict01 = {'name':'joe','age':18,'address':'上海'}
# print(dict01)


'''
    访问字典
'''
dict01 = {'name':'joe','age':18,'address':'上海'}
print(dict01)
print(dict01['name'])
#修改字典元素  通过找到指定 的 KEY 进行修改
dict01['name'] = 'jack'
print(dict01)
#增加元素
dict01['hobby'] = '足球'
print(dict01)

'''
    删除字典
'''
#del
# del dict01['address']
# del dict01   #从内存中删除
# print(dict01)

# dict01.clear()  #清空字典中的元素
# print(dict01)

'''
    字典函数
'''
#str
str1 = str(dict01)
print(type(str1))

dict02 = {'name':'joe','age':18,'address':'上海','sex':'女'}
print(dict02.get('sex','男'))
#如果字典用右该key对应的元素 就输出原来的 ， 如果没有则输出你指定的

print(dict02.keys())
print(dict02.values())
print(dict02.items())


#定义一个字典
aa = {'张三':['a','b','c'],'李四':['d','e','f']}
name = input('请输入姓名：')
print(aa[name])

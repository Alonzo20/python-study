#-*- conding:utf-8 -*-
''''''
'''
    自定义模块
'''
# import test   #引入同级目录中的test模块
# print(test.test_add(2,3))

# from test import test_add
# print(test_add(2,3))


'''
    跨模块引入1
'''
# import study.test2  #模块名.函数名
# print(study.test2.test2_add(2,3))

# from study import test2
# print(test2.test2_add(2,3))

# from study.test2 import test2_add
# print(test2_add(2,3))

'''
    跨模块引入2
'''
# import sys   #查看路径变量
# print(sys.path)
# 添加目标路径导当前环境中
# sys.path.append('..\\') #返回上一级目录

# print(sys.path)
# import msg.send
# msg.send.sendMsg()

# from msg import send,recv
# send.sendMsg()
# recv.recvMsg()

# import math as m  #引入的是标准模块
# print(m.ceil(1.1))  #向上取整
# print(m.floor(1.1))


#覆盖标准模块
# from msg import math   #自定义的模块
# print(math.ceil(1.1))  #向上取整
# print(math.floor(1.1))
# math.getInfo()

'''
    dir
    用于按模块名搜索模块定义，它返回一个字符串类型的存储列表
    该列表列出了所有类型的名称：变量，模块，函数，等等
'''
# print(dir())
# print(dir(math))

'''
    python中的包
'''
import sys   #查看路径变量
# print(sys.path)
# 添加目标路径导当前环境中
sys.path.append('..\\') #返回上一级目录

#通过import 方式 逐个导入模块
# import msg.send
# msg.send.sendMsg()
# import msg.recv
# msg.recv.recvMsg()

#通过from一次性导入所有的模块
#做一个包一定要创建一个__init__.py  这么文件中一定要设置 __all__ = ['允许导入的模块名']
# from msg import *
# send.sendMsg()
# recv.recvMsg()
# math.getInfo()



'''
    重新加载
'''
import test
# import test  #引入两边只输出一句hahaha
import imp
imp.reload(test)  #重新导入test模块

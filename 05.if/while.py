#_*_ conding:utf-8 _*_

'''
    while 条件表达式： 当条件为True的时候进入循环
        要执行的代码块   #执行完里面的代码块则回到条件表达式 进行条件判断
'''
i = 1  #初始化变量为1
while i<=100:  #对初始化条件信息判断 判断成立则进入循环体
    print('i love u')
    i+=1 #这里对变量进行一个累加 i = i+1
print(i)
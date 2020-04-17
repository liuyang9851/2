import turtle,time,random  # 导入库
zhuixun = turtle.Turtle()  # 新建对象，命名为 zhuixun
chuangkou = turtle.Screen  # 新建窗口，命名为 窗口
turtle.setup(2000,1015,0,0)# 设置窗口大小，即长，宽，距左距离，距右距离
turtle.bgcolor('black')    # 设置背景颜色
zhuixun.pencolor('white')  # 设置画笔颜色
zhuixun.hideturtle()       # 隐藏画笔
weizhi = 400               # 设置位置变量
if True:                   # 设置位置
    zhuixun.penup()            # 抬起画笔
    zhuixun.setpos(-200,weizhi)# 移动画笔至
    zhuixun.pendown()          # 放下画笔
zhuixun.write('按键以开始，',font=('times',20,'bold'))
if True:
    weizhi -= 100
    zhuixun.penup()            # 抬起画笔
    zhuixun.setpos(-200,weizhi)# 移动画笔至
    zhuixun.pendown()          # 放下画笔
zhuixun.write('请在弹出终端中输入内容',font=('times',15,'bold'))
caidan1 = input()  # 彩蛋1
if True:
    weizhi -= 100
    zhuixun.penup()
    zhuixun.setpos(-100,weizhi)
    zhuixun.pendown()
zhuixun.write('''眼前是黑暗
有人醒来''',font=('times',20,'bold'))
if True:
    weizhi -= 100
    zhuixun.penup()
    zhuixun.setpos(-100,weizhi)
    zhuixun.pendown()
zhuixun.write('''黑暗下静的出奇，似乎有厚重的幕布层层包裹
————“你看见了吗？”
————“看到了”
————“这是……”
————“为什么是这样。”
————“对了，你叫什么名字？''',font=('times',20,'bold'))
if True:  # 彩蛋2
    caidan2 = input()
    if True:
        weizhi -= 100
        zhuixun.penup()
        zhuixun.setpos(-100,weizhi)
        zhuixun.pendown()
    while caidan2.isspace():
        if True:
            weizhi -= 100
            zhuixun.penup()
            zhuixun.setpos(-100,weizhi)
            zhuixun.pendown()
        zhuixun.write('''“不，这不是，你……？”
        …………………………\n''',font=('times',15,'bold'))
        caidan2 = input()
    if caidan2 == '刘扬':
        zhuixun.write('',font=('times',20,'bold'))
    elif caidan2 == '':
        zhuixun.write('',font=('times',20,'bold'))
    else:
        zhuixun.write('“哦，',caidan2,'你好”',font=('times',20,'bold'))
turtle.exitonclick()  # 点击关闭窗口
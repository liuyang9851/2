import turtle  # 导入模块
zhufu = turtle.Turtle() # 创建Turtle对象，命名为zhufu
chuangkou = turtle.Screen  # 创建窗口
turtle.screensize(400,300,"green")  # 设置窗口长宽，背景色
zhufu.pencolor("green")  # 设置画笔颜色
zhufu.hideturtle()  # 隐藏箭头
zhufu.setpos(-150,50)  # 移动画笔至坐标  处
zhufu.pencolor("red")  # 设置画笔颜色
if True:  # 输入5
    zhufu.pensize(15)
    zhufu.left(180)
    zhufu.forward(50)
    zhufu.left(90)
    zhufu.forward(50)
    zhufu.left(90)
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(50)
if True:  # 输入2
    zhufu.penup()  # 抬起画笔
    zhufu.setpos(-50,50)  # 移动画笔至坐标  处
    zhufu.pendown()  # 放下画笔
    zhufu.left(180)
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(50)
    zhufu.left(90)
    zhufu.forward(50)
    zhufu.left(90)
    zhufu.forward(50)
zhufu.penup()
zhufu.setpos(100,50)
zhufu.pendown()
if True:  # 输入0
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(100)
    zhufu.right(90)
    zhufu.forward(50)
    zhufu.right(90)
    zhufu.forward(100)
zhufu.penup()
zhufu.setpos(-75,-150)
zhufu.pendown()
zhufu.write('I love you ',font=('times',20,'bold'))  # 输入文本
turtle.exitonclick()
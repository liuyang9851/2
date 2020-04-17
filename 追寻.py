import random,time  # 导入库
print('----------追寻----------')
caidan1 = input('按键以开始')  # 彩蛋1
print('''眼前是黑暗
有人醒来''')
print('黑暗下静的出奇，似乎有厚重的幕布层层包裹')
print('''   ————“你看见了吗？”
————“看到了”
————“这是……”
————“为什么是这样。”
————“对了，你叫什么名字？''')
if True:  # 彩蛋2
    caidan2 = input()
    while caidan2.isspace():
        caidan2 = input('''“不，这不是，你……？”
        …………………………\n''')
    if caidan2 == '刘扬':
        print('')
    elif caidan2 == '王钰翡':
        print('')
    else:
        print('“哦，',caidan2,'你好”')
print('————“这，我想说，我还在，我不好…”')
print('————“你看到的，这不是我，我不想在这样……”')
print('他的手似乎握的更紧了。')
while True:  # 选择a
    a = input("1.你到底是谁? 2.你在干什么？！")
    if a.isdigit():
        if int(a) == 1:
            print('''额，这不，
            谢谢你。''')
            break
        elif int(a) == 2:
            print('没什么，就是…')
            break
        else:
            print('请输入 1 或 2')  
    else:
        print('请输入 1 或 2')
print('静的出奇，没什么。')
print('这时，粗糙的声音不经意触动。')
while True:  # 选择b
    b = input('1.不，这，你在做什么，停下！2.嗯？你不会是，你现在感觉不好吗？')
    if b.isdigit():
        if int(b) == 1:
            print('“不，这是无意义的。”')
            print('“结束了，再见。”')
            print('你看到了，看到他的选择，他的未来，但没看到他所经历的。')
            print('他的选择，生命本由他，但他已无力改变……')
            print('游戏结束')
            break
        elif int(b) == 2:
            print('“……嗯……”')
            break
        else:
            print('请输入 1 或 2')  
    else:
        print('请输入 1 或 2')
while int(b) == 2:  # 选择c
    c = input('1.不，你在这里，能否说说你的往事。2.这，你不要难过，这里还有我。')
    if c.isdigit():
        if int(c) == 1:
            print('“嗯……”')
            break
        if int(c) == 2:
            print('这时，声音中有种激动')
            break
        else:
            print('请输入 1 或 2')
            continue
    print('“这，我，你能帮帮我吗？”')
while int(b) == 2:  # 选择d     
    d = input('1.好的。2.不能。')
    if d.isdigit():
        if int(d) == 1:
            print('“谢谢你。”')
            break
        if int(d) == 2:
            print('“好吧，还是谢谢你。”')
            print('“再见。”')
            print('他去寻找新的希望了')
            print('你在此祝福他')
            print('愿他排除万难，终得心中所想')
            print('许多年后，愿他在上无忧无虑……')
            print('再见')
            print('游戏结束')
            break
        else:
            print('请输入 1 或 2')
while int(b) == 1 and int(d) == 2:  # 选择e
    print('“再次谢谢你。”')
    print('“我的事情，你，我还是先想怎么出去吧。”')
    
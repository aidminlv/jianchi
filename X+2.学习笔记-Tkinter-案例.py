# 1.测试tkinter包
#import tkinter
#tkinter._test()
# *****************************

# 2.hello world案例
#import tkinter
#base = tkinter.Tk()
# 消息循环
#base.mainloop()
# *****************************

# 3.Label案例
'''import tkinter

base = tkinter.Tk() # 总的面板
# 负责最大的标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text = "Python Label")
# 给相应组件指定布局
# 布局就是怎么摆放
lb.pack()

base.mainloop()
'''
# *****************************

# 4.设置Label的例子
'''
import tkinter
base = tkinter.Tk()
base.wm_title("你好，世界")
# 支持属性很多background，font, underline等
# 第一个参数，指定所属
lb1 = tkinter.Label(base, text = "Python AI")
lb1.pack()

lb2 = tkinter.Label(base, text = "绿色背景", background = "green")
lb2.pack()

lb3 = tkinter.Label(base, text = "蓝色背景", background = "blue")
lb3.pack()

base.mainloop()
'''
# *****************************

# 5.Button案例
'''
import tkinter

def showLabel():
    global baseFrame
    # 在函数中定义了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text = "显示Label")
    lb.pack()

baseFrame = tkinter.Tk()
# 生成了一个按钮
# command参数指示，当按钮被按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame, text = "ShowLabel", command=showLabel)
btn.pack()

baseFrame.mainloop()
'''
# 6.pack布局案例
'''
import tkinter
baseFrame = tkinter.Tk()
# 以下所有代码都是创建一个组件，然后布局
btn1 = tkinter.Button(baseFrame, text = "A")
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)
btn2 = tkinter.Button(baseFrame, text = "B")
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
btn3 = tkinter.Button(baseFrame, text = "C")
btn3.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE, anchor=tkinter.NE)
btn4 = tkinter.Button(baseFrame, text = "D")
btn4.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)
btn5 = tkinter.Button(baseFrame, text = "E")
btn5.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.BOTH)
btn6 = tkinter.Button(baseFrame, text = "F")
btn6.pack(side=tkinter.BOTTOM, expand=tkinter.YES)
btn7 = tkinter.Button(baseFrame, text = "G")
btn7.pack(anchor=tkinter.SE)
baseFrame.mainloop()
'''
# 7.grid案例
'''
import tkinter
baseFrame = tkinter.Tk()
lb1 = tkinter.Label(baseFrame, text="账号：").grid(row=0, sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=0, column=1, sticky=tkinter.E)
lb2 = tkinter.Label(baseFrame, text="密码：").grid(row=1, sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=1, column=1, sticky=tkinter.E)
btn = tkinter.Button(baseFrame, text="登陆").grid(row=2, column=1, sticky=tkinter.W)
baseFrame.mainloop()
'''
# 8.消息机制（事件）案例
'''
import tkinter
def baseButton(event):
    global baseFrame
    print("哈哈，我被点击了")
    lb = tkinter.Label(baseFrame, text="谢谢点击")
    lb.pack()
# 画出程序的总框架
baseFrame = tkinter.Tk()
lb = tkinter.Button(baseFrame, text="模拟按钮")
# Button绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数baseLabel
lb.bind("<Button-1>", baseButton)
lb.pack()
# 启动消息循环
# 到此，表示程序开始运行
baseFrame.mainloop()
'''
# 9.输入框案例
'''
import tkinter
# 模拟的是登陆函数
def reg():
    # 从相应输入框中，得到用户的输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        # 需要理解下面代码的含义
        lb3["text"] = "登录成功"
    else:
        lb3["text"] = "用户名或密码错误"
        # 输入框删除掉用户输入的内容
        # 注意delete的两个参数，表示从第几个删除到第几个
        e1.delete(0, t1)
        e2.delete(0, t2)
# 启动舞台
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名：")
lb1.grid(row=0, column=0, stick=tkinter.W)
e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, stick=tkinter.E)
lb2 = tkinter.Label(baseFrame, text="密码：")
lb2.grid(row=1,column=0,stick=tkinter.W)
e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, stick=tkinter.E)
e2["show"] = "*"
# Button参数command的意思时，当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame, text="登陆", command=reg)
btn.grid(row=2, column=1, stick=tkinter.E)
lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row = 3)
# 启动主Frame
baseFrame.mainloop()
'''
# 10.普通菜单案例
'''
import tkinter
baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)
baseFrame['menu'] = menubar
baseFrame.mainloop()
'''
# 11.级联菜单案例
'''
import tkinter
baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)
menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About')
baseFrame['menu'] = menubar
baseFrame.mainloop()
'''
# 12.弹出式菜单案例
import tkinter
def makeLabel():
    global baseFrame
    tkinter.Label(baseFrame, text="PHP是最好的编程语言，我用Python").pack()
baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)
for x in ['麻辣香菇', '汽锅鸡', '东坡肘子']:
    menubar.add_separator()
    menubar.add_command(label=x)
menubar.add_command(label='重庆火锅', command=makeLabel())
# 事件处理函数一定要至少有一个参数，且第一个参数表示的是系统事件
def pop(event):
    # 注意使用event.x和event.x_root的区别
    # menubar.post(event.x_root, event.y_root)
    menubar.post(event.x_root, event.y_root)
baseFrame.bind("<Button-3>", pop)
baseFrame.mainloop()

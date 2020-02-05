from tkinter import *
from tkinter.messagebox import *

class Register_Page(object):
    def __init__(self, master=None): 
        self.root = master #定义内部变量root 
        self.root.geometry('%dx%d' % (500, 420)) #设置窗口大小
        self.username = StringVar()
        self.studentId = StringVar()
        self.userpassword = StringVar()
        self.userpasswordre = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row = 0,stick = W,pady = 20)
        Label(self.page, text = '账       号：',font = ("楷体",15,"bold")).grid(row = 1,stick = W,pady = 15)
        Entry(self.page,textvariable=self.username,font = ("楷体",15,"bold")).grid(row = 1,column = 1,stick = E)
        Label(self.page, text = '学       号： ',font = ("楷体",15,"bold")).grid(row=2, stick=W, pady=15) 
        Entry(self.page, textvariable=self.studentId,font = ("楷体",15,"bold")).grid(row=2, column=1, stick=E)
        Label(self.page, text = '密       码： ',font = ("楷体",15,"bold")).grid(row=3, stick=W, pady=15) 
        Entry(self.page, textvariable=self.userpassword,font = ("楷体",15,"bold"),show = '*').grid(row=3, column=1, stick=E)
        Label(self.page, text = '重新输入密码： ',font = ("楷体",15,"bold")).grid(row=4, stick=W, pady=15) 
        Entry(self.page, textvariable=self.userpasswordre,font = ("楷体",15,"bold"),show = '#').grid(row=4, column=1, stick=E)
        Button(self.page, text='注册',font = ("楷体",15,"bold"),command = self.register_admir).grid(row = 5,stick=W,column=1, pady=20,padx = 30)
    
    def register_admir(self):
        name = self.username.get()
        id = self.studentId.get()
        password = self.userpassword.get()
        passwordre = self.userpasswordre.get()
        id_str = id[4:6]
        f = open('login_true.txt')
        temp = 0
        for line in f:
            l = line.strip().split(',')
            if l[0] == name:
                showwarning(message='输入用户名已经存在')
                temp = 1
                break
            else:
                continue
        if temp != 1 and id_str == '41' and password ==passwordre:
            fw = open('login_true.txt','a')
            fw.write(name+','+password+'\n')
            fw.close()
            showinfo(message='注册成功！')
        elif temp != 1 and password != passwordre:
            showwarning(message='两次输入密码不一致')
        elif temp != 1 and id_str != '41':
            showwarning(message='学号输入有误！')
        
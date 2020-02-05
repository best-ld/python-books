from tkinter import *
from tkinter.messagebox import *
from User_MainPage import *
from Admir_MainPage import *
from Register_Page import *

class LoginPage(object):
    def __init__(self,master = None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (300,200))#设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #创建Frame
        self.page.pack()
        Label(self.page).grid(row = 0,stick = W)
        Label(self.page,text = '账号').grid(row = 1,stick = W,pady = 10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E) 
        Label(self.page,text = '密码').grid(row = 2,stick = W,pady = 10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page,text = '用户登录',command = self.loginCheck).grid(row = 3,stick =W, pady = 5)
        Button(self.page,text = '管理员登录',command = self.admir_loginCheck).grid(row = 3,stick =E,column=1)
        Button(self.page,text = '注册',command = self.registerCheck).grid(row = 4,stick =W,column=1,padx = 20,pady = 5)
    
    def loginCheck(self):
        name = self.username.get()
        password = self.password.get()
        f = open('login_true.txt')
        for line in f:
            str = line.strip()
            str2 = ','
            user_name = str[:str.index(str2)]
            pass_word = str[str.index(str2)+1:]
            if name == user_name and pass_word == password:
                temp = 1
                break
            else:
                temp = 0
        if temp == 1 :
            self.page.destroy()
            User_MainPage(self.root) 
        elif temp == 0 :
            showinfo(title = '失败', message = '账号或密码错误，重新登录！')

    def admir_loginCheck(self):
        admir_name = self.username.get()
        admir_password = self.password.get()
        f1 = open('login_admir.txt')
        for line1 in f1:
            str = line1.strip()
            str1 = ','
            admir_name_txt = str[:str.index(str1)]
            admir_password_txt = str[str.index(str1)+1:]
            if admir_name == admir_name_txt and admir_password == admir_password_txt:
                temp = 3
                break
            else:
                temp = 4 
        if temp == 3:
            self.page.destroy()
            Admir_MainPage(self.root)
        elif temp == 4:
            showinfo(title='失败', message='账号或密码错误，重新登录！')

    def registerCheck(self):
        self.page.destroy()
        Register_Page(self.root)
from tkinter import *
from view_user import *

class User_MainPage(object):
    def __init__(self,master = None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d'%(510,475))
        self.creatPage()

    def creatPage(self):
        self.firstPage = FirstFrame(self.root)#首页
        self.queryPage = QueryFrame(self.root) #查询界面
        self.borrowPage = BorrowFrame(self.root) #借阅界面
        self.returnPage = ReturnFrame(self.root) #归还界面
        self.firstPage.pack()#默认查询界面
        menubar = Menu(self.root)
        menubar.add_command(label = '首页',command = self.firstData)
        menubar.add_command(label = '查询',command = self.queryData)
        menubar.add_command(label = '借阅',command = self.borrowData)
        menubar.add_command(label = '归还',command = self.returnData)
        self.root['menu'] = menubar #设置菜单栏

    def firstData(self):
        self.firstPage.pack()
        self.queryPage.pack_forget()
        self.borrowPage.pack_forget()
        self.returnPage.pack_forget()

    def queryData(self):
         self.firstPage.pack_forget()
         self.queryPage.pack()
         self.borrowPage.pack_forget()
         self.returnPage.pack_forget()
        
    def borrowData(self):
        self.firstPage.pack_forget()
        self.queryPage.pack_forget()
        self.borrowPage.pack()
        self.returnPage.pack_forget()

    def returnData(self):
        self.firstPage.pack_forget()
        self.queryPage.pack_forget()
        self.borrowPage.pack_forget()
        self.returnPage.pack()
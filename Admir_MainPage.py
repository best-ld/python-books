from tkinter import *
from view_admir import *

class Admir_MainPage(object):
    def __init__(self,master = None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d'%(510,475))
        self.creatPage()

    def creatPage(self):
        self.addPage = AddFrame(self.root)#录入界面
        self.deletePage = DeleteFrame(self.root) #删除界面
        self.countPage = CountFrame(self.root) #统计界面
        self.register_admirPage = Register_admirFrame(self.root) #添加新管理员界面
        self.addPage.pack()#默认录入界面
        menubar = Menu(self.root)
        menubar.add_command(label = '录入书籍',command = self.addData)
        menubar.add_command(label = '删除书籍',command = self.deleteData)
        menubar.add_command(label = '统计书籍',command = self.countData)
        menubar.add_command(label = '添加管理员',command = self.register_admirData)
        self.root['menu'] = menubar #设置菜单栏

    def addData(self):
        self.addPage.pack()
        self.deletePage.pack_forget()
        self.countPage.pack_forget()
        self.register_admirPage.pack_forget()

    def deleteData(self):
         self.addPage.pack_forget()
         self.deletePage.pack()
         self.countPage.pack_forget()
         self.register_admirPage.pack_forget()
        
    def countData(self):
        self.addPage.pack_forget()
        self.deletePage.pack_forget()
        self.countPage.pack()
        self.register_admirPage.pack_forget()

    def register_admirData(self):
        self.addPage.pack_forget()
        self.deletePage.pack_forget()
        self.countPage.pack_forget()
        self.register_admirPage.pack()
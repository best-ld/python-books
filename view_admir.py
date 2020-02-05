from tkinter import *
from tkinter.messagebox import *

class AddFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root 
        self.book_ID = StringVar()
        self.book_Name = StringVar()
        self.book_Writer = StringVar()
        self.book_Num = StringVar()
        self.book_Price = StringVar()
        self.createPage() 
    
    def createPage(self): 
        Label(self).grid(row = 0,stick = W,pady = 10)
        Label(self, text = '编    号：',font = ("楷体",15,"bold")).grid(row = 1,stick = W,pady = 15)
        Entry(self,textvariable=self.book_ID,font = ("楷体",15,"bold")).grid(row = 1,column = 1,stick = E)
        Label(self, text = '书    名: ',font = ("楷体",15,"bold")).grid(row=2, stick=W, pady=15) 
        Entry(self, textvariable=self.book_Name,font = ("楷体",15,"bold")).grid(row=2, column=1, stick=E) 
        Label(self, text = '作    者: ',font = ("楷体",15,"bold")).grid(row=3, stick=W, pady=15) 
        Entry(self, textvariable=self.book_Writer,font = ("楷体",15,"bold")).grid(row=3, column=1, stick=E) 
        Label(self, text = '数量 /本: ',font = ("楷体",15,"bold")).grid(row=4, stick=W, pady=15) 
        Entry(self, textvariable=self.book_Num,font = ("楷体",15,"bold")).grid(row=4, column=1, stick=E)
        Label(self, text = '价格 /元: ',font = ("楷体",15,"bold")).grid(row=5, stick=W, pady=15) 
        Entry(self, textvariable=self.book_Price,font = ("楷体",15,"bold")).grid(row=5, column=1, stick=E) 
        Button(self, text='录  入',font = ("楷体",15,"bold"),command = self.add_books).grid(row = 6,stick=W,column=1, pady=20,padx = 40) 

    def add_books(self):
        bookid = self.book_ID.get()
        bookname = self.book_Name.get()
        bookwriter = self.book_Writer.get()
        booknum = self.book_Num.get()
        bookprice = self.book_Price.get()
        f = open('books.txt')
        temp = 0
        for line in f:
            l = line.strip().split(',')
            if l[1] == bookname:
                temp = 1
                break
            else:
                continue
        if temp == 1:#该书已经存在，则修改其数量
            with open('books.txt','r') as fr:
                lines = fr.readlines()
            with open('books.txt','w') as fw:
                for line in lines:
                    v = line.strip().split(',')
                    if bookname == v[1]:
                        num = int(booknum)+int(v[3])
                        num_str = str(num)
                        fw.write(v[0]+','+v[1]+','+v[2]+','+num_str+','+v[4]+'\n')
                    else:
                        fw.write(line)
            fr.close()
            fw.close()
        else:#该书不存在，则添加录入信息
            fw = open('books.txt','a')
            fw.write(bookid+','+bookname+','+bookwriter+','+booknum+','+bookprice+'\n')
            fw.close()
        showinfo(message='录入成功！')
            
class DeleteFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root 
        self.book_Name = StringVar()
        self.booknum_Delete = StringVar()
        self.createPage() 
    
    def createPage(self): 
        Label(self).grid(row = 0,stick = W,pady = 10)
        Label(self, text = '书       名：',font = ("楷体",15,"bold")).grid(row = 1,stick = W,pady = 15)
        Entry(self,textvariable=self.book_Name,font = ("楷体",15,"bold")).grid(row = 1,column = 1,stick = E)
        Label(self, text = '删除数量 /本: ',font = ("楷体",15,"bold")).grid(row=2, stick=W, pady=15) 
        Entry(self, textvariable=self.booknum_Delete,font = ("楷体",15,"bold")).grid(row=2, column=1, stick=E)
        Button(self, text='删  除',font = ("楷体",15,"bold"),command = self.delete_books).grid(row = 6,stick=W,column=1, pady=20,padx = 30) 

    def delete_books(self):
        bookname = self.book_Name.get()
        book_num_delete = self.booknum_Delete.get()
        f = open('books.txt')
        temp = 0
        for line in f:
            l = line.strip().split(',')
            if bookname == l[1] and int(l[3]) > int(book_num_delete): #要删除的书数量小于库存数量
                temp = 1
                break
            elif bookname == l[1] and int(l[3]) <= int(book_num_delete):#要删除的书数量大于等于库存数量
                temp = 2
                break
            else:
                continue
        if temp == 1:
            with open('books.txt','r') as fr:
                lines = fr.readlines()
            with open('books.txt','w') as fw:
                for line in lines:
                    v = line.strip().split(',')
                    if bookname == v[1]:
                        num = int(l[3]) - int(book_num_delete)
                        str_value = str(num)
                        fw.write(l[0]+','+l[1]+','+l[2]+','+str_value+','+l[4]+ '\n')
                    else:
                        fw.write(line)
            fr.close()
            fw.close()
            showinfo(message='删除成功！')
        elif temp == 2:
            with open('books.txt','r') as fr:
                lines = fr.readlines()
            with open('books.txt','w') as fw:
                for line in lines:
                    v = line.strip().split(',')
                    if bookname == v[1]:
                        continue
                    fw.write(line)
            fr.close()
            fw.close()
            showinfo(message='删除成功！')
        else:
            showwarning(title = 'Waring',message = '您输入的图书书名有误，请重新输入！')

class CountFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root 
        self.book_Name = StringVar()
        self.createPage() 
           
    def createPage(self):
        Label(self).grid(row = 0,stick = W,pady = 40)
        Label(self, text = '书       名：',font = ("楷体",15,"bold")).grid(row = 1,stick = W,pady = 20)
        Entry(self,textvariable=self.book_Name,font = ("楷体",15,"bold")).grid(row = 1,column = 1,stick = E)
        Button(self, text='统  计',font = ("楷体",15,"bold"),command = self.count_books).grid(row = 6,stick=W,column=1, pady=20,padx = 30) 

    def count_books(self):
        bookname = self.book_Name.get()
        f = open('books.txt')
        for line in f:
            l = line.strip().split(',')
            if l[1] == bookname:
                count_remain = int(l[3])
                break
            else:
                continue
        f1 = open('book_lend.txt')
        count_lend = 0
        for line1 in f1:
            l1 = line1.strip().split(',')
            if l1[0] == bookname:
                count_lend  += 1 #!Python 中是没有 ++ 和 -- 的
            else:
                continue
        count_all = count_remain + count_lend
        countWin = Tk()
        countWin.title('统计信息')
        countWin.geometry('500x400')
        Label(countWin).grid(row = 0,stick = W,pady = 20)
        Label(countWin, text = '书    名：    '+bookname,font = ("楷体",15,"bold")).grid(row=1, stick=W, pady=10,padx = 90)
        Label(countWin, text = '总    数：    '+str(count_all),font = ("楷体",15,"bold")).grid(row = 2,stick = W,pady = 15,padx = 90)
        Label(countWin, text = '借出数量：    '+str(count_lend)+'本',font = ("楷体",15,"bold")).grid(row = 3,stick = W,pady = 15,padx = 90)
        Label(countWin, text = '剩余数量：    '+str(count_remain)+'本',font = ("楷体",15,"bold")).grid(row = 4,stick = W,pady = 15,padx = 90)

class Register_admirFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root
        self.admir_Name = StringVar()
        self.admir_Password = StringVar()
        self.admir_Password_repetion = StringVar()
        self.createPage() 
    
    def createPage(self): 
        Label(self).grid(row = 0,stick = W,pady = 20)
        Label(self, text = '账       号：',font = ("楷体",15,"bold")).grid(row = 1,stick = W,pady = 15)
        Entry(self,textvariable=self.admir_Name,font = ("楷体",15,"bold")).grid(row = 1,column = 1,stick = E)
        Label(self, text = '密       码： ',font = ("楷体",15,"bold")).grid(row=2, stick=W, pady=15) 
        Entry(self, textvariable=self.admir_Password,font = ("楷体",15,"bold"),show = '*').grid(row=2, column=1, stick=E)
        Label(self, text = '重新输入密码： ',font = ("楷体",15,"bold")).grid(row=3, stick=W, pady=15) 
        Entry(self, textvariable=self.admir_Password_repetion,font = ("楷体",15,"bold"),show = '#').grid(row=3, column=1, stick=E)
        Button(self, text='注册',font = ("楷体",15,"bold"),command = self.register_admir).grid(row = 4,stick=W,column=1, pady=20,padx = 30)

    def register_admir(self):
        admirname = self.admir_Name.get()
        admirpassword = self.admir_Password.get()
        admirpasstwo = self.admir_Password_repetion.get()
        f = open('login_admir.txt')
        temp = 0
        for line in f:
            l = line.strip().split(',')
            if l[0] == admirname:
                showwarning(message='输入用户名已经存在')
                temp = 1
                break
            else:
                continue
        if temp != 1 and admirpassword == admirpasstwo:
            fw = open('login_admir.txt','a')
            fw.write(admirname+','+admirpassword+'\n')
            fw.close()
            showinfo(message='注册成功！')
        elif temp != 1 and admirpassword != admirpasstwo:
            showwarning(message='两次输入密码不一致')

from tkinter import *
from tkinter.messagebox import *
import datetime

class FirstFrame(Frame):# 继承Frame
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()
        
    def createPage(self):
        self.photo = PhotoImage(file = "welcome.gif")#tkinter默认只显示gif图片
        Label(self,image = self.photo).grid(row=0,  column=1, stick=W, padx=3)

class QueryFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.book_Name = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10) 
        Label(self, text = '书  名： ',font = ("宋体",14,"bold")).grid(row=1, stick=W, pady=10)
        Entry(self, textvariable = self.book_Name,font = ("宋体",14,"bold")).grid(row=1, column=1, stick=E)
        Button(self,text = '查  找',font = ("宋体",14,"bold"),command = self.find_book).grid(row = 2,stick=W,column=1, pady=20,padx = 50)
    
    def find_book(self):
        bookname = self.book_Name.get()
        f2 = open('books.txt')
        for line2 in f2:
            str1 = line2.strip()
            List = str1.split(',')
            bookid_txt = List[0]
            bookname_txt = List[1]
            bookwriter_txt = List[2]
            booknum_txt = List[3]
            bookprice_txt = List[4]
            if bookname_txt == bookname:
                temp = 1
                break
            else:
                temp = 2
        if temp == 1:
            bookWindow = Tk()
            bookWindow.title('该图书信息')
            bookWindow.geometry('500x300')
            Label(bookWindow).grid(row=0, stick=W, pady=8)
            Label(bookWindow,text = '编   号：'+bookid_txt,font = ("宋体",14,"bold")).grid(row=1, stick=W, pady=10,padx = 100)
            Label(bookWindow,text = '书   名：'+bookname_txt,font = ("宋体",14,"bold")).grid(row=2, stick=W, pady=10,padx = 100)
            Label(bookWindow,text = '作   者：'+bookwriter_txt,font = ("宋体",14,"bold")).grid(row=3, stick=W, pady=10,padx = 100)
            Label(bookWindow,text = '数   量：'+booknum_txt+'  本',font = ("宋体",14,"bold")).grid(row=4, stick=W, pady=10,padx = 100)
            Label(bookWindow,text = '价   格：'+bookprice_txt+'  元',font = ("宋体",14,"bold")).grid(row=5, stick=W, pady=10,padx = 100)
            bookWindow.mainloop()
        elif temp == 2:
            showinfo(message=("您查询的书籍不存在！"))

class BorrowFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master  
        self.book_Name = StringVar()
        self.user_Name = StringVar()
        self.user_Password = StringVar()        
        self.createPage()
        
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10) 
        Label(self, text = '书  名： ',font = ("宋体",14,"bold")).grid(row=1, stick=W, pady=20)
        Entry(self, textvariable = self.book_Name,font = ("宋体",14,"bold")).grid(row=1, column=1, stick=E)
        Label(self, text = '用户名： ',font = ("宋体",14,"bold")).grid(row=2, stick=W, pady=20)
        Entry(self, textvariable = self.user_Name,font = ("宋体",14,"bold")).grid(row=2, column=1, stick=E)
        Label(self, text = '密  码： ',font = ("宋体",14,"bold")).grid(row=3, stick=W, pady=20)
        Entry(self, textvariable = self.user_Password, show='*',font = ("宋体",14,"bold")).grid(row=3, column=1, stick=E)
        Button(self,text = '借  书',font = ("宋体",14,"bold"),command = self.borrow_book).grid(row = 4,stick=W,column=1, pady=20,padx = 50)
    
    def borrow_book(self):
        f = open('books.txt')
        f1 = open('login_true.txt')
        bookname = self.book_Name.get()
        username = self.user_Name.get()
        userpassword =self.user_Password.get()
        for line in f1:
            str1 = line.strip()
            List = str1.split(",")
            username_txt = List[0]
            userpassword_txt = List[1]
            if username == username_txt and userpassword == userpassword_txt:
                temp = 1
                break
            else:
                temp = 2
        if temp == 1:
            for line2 in f:
                str1 = line2.strip()
                List1 = str1.split(",")
                bookname_txt = List1[1]
                booknum_txt = List1[3]
                if bookname == bookname_txt:
                    if int(booknum_txt) > 0:
                        temp1 = 1  
                    else:
                        temp1 =2
                    break
                else:
                    temp1 = 0
            if temp1 == 0:
                showwarning(title = 'Error',message = '该书不存在！')
            elif temp1 == 2:
                showwarning(title = 'Error',message = '该书已被借完！') 
            else:
                with open('books.txt', 'r') as fr:
                    lines=fr.readlines()
                with open('books.txt', 'w') as fw:
                    for line in lines:
                        l = line.strip().split(',')
                        if bookname == l[1]:
                            num=int(l[3])-1
                            str_value = str(num)
                            fw.write(l[0]+','+l[1]+','+l[2]+','+str_value+','+l[4]+ '\n')
                        else:
                            fw.write(line)
                fr.close()
                fw.close()
                borrow_date = datetime.datetime.now().strftime('%Y-%m-%d')
                fw1 = open('book_lend.txt','a')
                fw1.write(bookname+','+username+','+borrow_date+'\n')
                showinfo(title = 'Success',message = '借书成功！')            
        else:
            showwarning(title = 'Error', message = '账号或密码错误，重新登录！')
            

class ReturnFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.root = master
        self.book_Name_re = StringVar()
        self.user_Name_re = StringVar()
        self.user_Password_re = StringVar()
        self.createPage()
        
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10) 
        Label(self, text = '书  名： ',font = ("宋体",14,"bold")).grid(row=1, stick=W, pady=20)
        Entry(self, textvariable = self.book_Name_re,font = ("宋体",14,"bold")).grid(row=1, column=1, stick=E)
        Label(self, text = '用户名： ',font = ("宋体",14,"bold")).grid(row=2, stick=W, pady=20)
        Entry(self, textvariable = self.user_Name_re,font = ("宋体",14,"bold")).grid(row=2, column=1, stick=E)
        Label(self, text = '密  码： ',font = ("宋体",14,"bold")).grid(row=3, stick=W, pady=20)
        Entry(self, textvariable = self.user_Password_re, show='*',font = ("宋体",14,"bold")).grid(row=3, column=1, stick=E)
        Button(self,text = '还  书',font = ("宋体",14,"bold"),command = self.return_book).grid(row = 4,stick=W,column=1, pady=20,padx = 50)

    def return_book(self):
        f = open('books.txt')
        f1 = open('login_true.txt')
        bookname = self.book_Name_re.get()
        username = self.user_Name_re.get()
        userpassword =self.user_Password_re.get()
        for line in f1:
            str1 = line.strip()
            List = str1.split(",")
            username_txt = List[0]
            userpassword_txt = List[1]
            if username == username_txt and userpassword == userpassword_txt:
                temp = 1
                break
            else:
                temp = 2
        if temp == 1:
            for line2 in f:
                List1 = line2.strip().split(",")
                bookname_txt = List1[1]
                if bookname == bookname_txt:#若该书存在temp1置为1
                    temp1 = 1
                    break
                else:
                    temp1 = 0
            if temp1 == 0:
                showwarning(title = 'Waring',message = '您输入的图书书名有误，请重新输入！')
            elif temp1 == 1:
                with open('books.txt','r') as fr:
                    lines = fr.readlines()
                with open('books.txt','w') as fw:
                    for line in lines:
                        l = line.strip().split(',')
                        if bookname == l[1]:
                            num = int(l[3])+1
                            str_value = str(num)
                            fw.write(l[0]+','+l[1]+','+l[2]+','+str_value+','+l[4]+ '\n')
                        else:
                            fw.write(line)
                fr.close()
                fw.close()
                sign = 0
                with open ('book_lend.txt','r') as fr1:
                    lines1 = fr1.readlines()
                with open ('book_lend.txt','w') as fw1:
                    for line1 in lines1:
                        v = line1.strip().split(',')
                        if v[0] == bookname and v[1] == username and sign == 0:
                            list2 = v[2].strip().split('-')
                            date1 = datetime.date(year=int(list2[0]),month=int(list2[1]),day=int(list2[2]))
                            back_date = datetime.datetime.now().strftime('%Y-%m-%d')
                            list3 = back_date.strip().split('-')
                            date2 = datetime.date(year=int(list3[0]),month=int(list3[1]),day=int(list3[2]))
                            date = (date2-date1).days+1
                            sign = 1 #设置sign保证只删除1条数据
                            borrowWin = Tk()
                            borrowWin.title('借书信息')
                            borrowWin.geometry('500x300')
                            Label(borrowWin).grid(row=0, stick=W, pady=8)
                            Label(borrowWin,text = '书    名：'+bookname,font = ("宋体",14,"bold")).grid(row=1, stick=W, pady=10,padx = 100)
                            Label(borrowWin,text = '用    户：'+username,font = ("宋体",14,"bold")).grid(row=2, stick=W, pady=10,padx = 100)
                            Label(borrowWin,text = '借出日期：'+list2[0]+'年'+list2[1]+'月'+list2[2]+'日',font = ("宋体",14,"bold")).grid(row=3, stick=W, pady=10,padx = 100)
                            Label(borrowWin,text = '借出天数：'+str(date)+'  天',font = ("宋体",14,"bold")).grid(row=4, stick=W, pady=10,padx = 100)
                            continue
                        fw1.write(line1)
                fr1.close()
                fw1.close()
                showinfo(title = 'Success',message = '还书成功！')
        else:
            showwarning(title = 'Error', message = '账号或密码错误，重新登录！')
# Python图书管理系统

### 一、简介

该系统主要通过tkinter库实现图书管理系统，该项目包含对文件的操作，对字符串解析的python知识点

### 二、系统实现功能介绍及使用方法

#### 1、登录功能：

![1](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\1.png)

不同用户通过输入账号、密码再点击按钮选择登录的方式，进入对应的用户界面。

#### 2、注册功能

![2](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\2.png)

若选择注册功能，进入注册界面，用户输入新账号、新密码、学号、重新输入新密码，根据用户输入的信息，系统会判断用户名是否已经存在、两次输入的密码是否拥有、学号是否为特定格式，并弹出如下图的警告。

![3](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\3.png)

#### 3、普通用户功能

##### A、首页

![4](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\4.png)

##### B、查询功能

![5](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\5.png)

点击菜单“查询”选项，进入查询界面，在输入框输入查找的书名，点击“查找”按钮，系统访问存储书名的books.txt文件，如果该书存在，则返回该书的所有信息（如下图），若不存在，则弹出警告。

![6](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\6.png)

##### C、借阅功能

![image-20200206170645945](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\7.png)

点击菜单“借阅”选项，进入借阅界面，输入书名、用户名及密码，点击“借书”按钮，系统访问存储书籍的文件（books.txt），如果文件中存在该书且该书的数量不为0，则弹出“借书成功”的信息，并将借书的用户、书名、时间写入book_lend.txt，文件books.txt执行数量减一的操作。若输入信息错误或书籍不存在，则弹出相应的信息

##### D、归还功能

![8](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\8.png)

点击菜单“归还”选项，进入还书界面，输入书名、用户名及密码，点击“还书”按钮，系统访问存储借书信息的文件（book_lend.txt），如果文件中存在对应的书名，用户名，则在book_lend.txt中删除该条信息，并且books.txt文件中图书数量加一，同时弹出有过信息的窗口（如下图），如果不存在该条信息或其他信息有误，则弹出相应信息。

![9](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\9.png)

#### 4、管理员功能

##### A、录入书籍功能

管理员界面默认为录入界面，输入书籍的编号、书名、作者、数量及价格信息，点击”录入“按钮，系统判断文件books.txt中是否有该书，如果有该书信息，则对其数量加输入的对应数量，如果该书不存在，则新增一条该书的信息。

![10](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\10.png)

##### B、删除书籍功能

点击菜单“删除书籍”选项，进入删除书籍界面，输入书名及删除数量，点击“删除”按钮，系统判断books.txt中是否存在该书的信息，不存在则弹出警告，存在则判断该书数量是否比要删除的数量小，如比输入的数量小，则在文件books.txt中删除该书的信息，若比输入的数量大，则在该书信息后面的数量减掉相应输入的数量，弹出“删除成功”的信息。

![11](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\11.png)

##### C、统计书籍功能

点击菜单“删除书籍”选项，进入统计书籍界面，输入该书的书名，点击“统计”按钮，系统判断books.txt中是否有该书，如果没有弹出相应的提示，如果存在，则显示书的数量，借出数量，剩余数量。

![12](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\12.png)

##### D、管理员注册功能

点击菜单“管理员注册”选项，进入注册界面，输入新账号，新密码，重新输入新密码，点击“注册”按钮，系统判断该账号是否存在，重新输入密码是否一致，如出现错误，则返回相应的错误信息，否则，则显示注册成功。

![13](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\13.png)

#### 注：

##### 1、books.txt文件的格式为：

![14](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\14.png)

##### 2、book_lend.txt文件的格式为：

![15](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\15.png)

##### 3、login_admir.txt文件的格式为：

![16](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\16.png)

##### 4、login_true.txt文件的格式为：

![17](E:\寒假Py学习\books\图书管理系统\python-books\运行界面截图\17.png)

##### 5、测试账号，密码

用户账号：gu、用户密码：1111

管理员账号：admir、管理员密码：123


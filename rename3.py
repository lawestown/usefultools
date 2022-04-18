import os
import xlrd


count = 1 
path = "C:\\Users\\Administrator\\Desktop\\123" #文件所在文件夹
expath = "C:\\Users\\Administrator\\Desktop\\18.xls"#Excel表所在文件夹

x1 = xlrd.open_workbook(expath)#读取excel
sheet1 = x1.sheet_by_name("Sheet1")#读取sheet1


idlist = sheet1.col_values(0)#存放第一列
xylist = sheet1.col_values(1)#存放第二列




filelist = os.listdir(path)#读取文件目录

for files in filelist:#遍历文件目录
    Olddir = os.path.join(path,files)#旧的文件位置
    os.renames(Olddir,os.path.join(path,str(int(idlist[count]))+"   "+xylist[count]))#新的文件位置
    count = count +1#计数指针后移

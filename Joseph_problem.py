import xlrd
import os
import zipfile
import csv
class Student(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

class ReadFile(object):
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileType = os.path.splitext(self.filePath)[1] #将文件名和扩展名分开
        self.Students = []
    
    def getStudentInfo(self):
        if self.fileType == '.xls':
            file_name = xlrd.open_workbook(self.filePath)#得到文件
            table =file_name.sheets()[0]#得到sheet页
            nrows = table.nrows #总行数
            i = 1
            while i < nrows:
                name=table.row_values(i)[0]
                id = table.row_values(i)[1] 
                id=int(id) 
                self.Students.append(Student(name, id))
                print(name, '的信息已读出\n')
                i=i+1
        elif self.fileType == '.txt':
            with open(self.filePath, 'r') as f:
                for lines in f.readlines():
                    info = lines.split()
                    name = info[0]
                    id = int(info[1])
                    self.Students.append(Student(name, id))
                    print(name, '的信息已读出\n')
        elif self.fileType == '.zip':
             file_zip = zipfile.ZipFile(self.filePath) 
             file_list = file_zip.namelist()            #获得压缩文件内的所有文件命,并返回一个list
             for file_name in file_list:
                file_zip = file_zip.open(file_name,'r')
                #file_contents = file_contents.decode("UTF-8")
                file_by_lines = file_zip.readlines()
                for line in file_by_lines:
                    line_utf8 = line.decode("UTF-8")        #返回str类型的数据
                    line_list = line_utf8.split()           #以空隔为分割依据，返回list类型
                    name = line_list[0]
                    id = int(line_list[1])
                    self.Students.append(Student(name, id))
                    print(name, '的信息已读出\n')
        elif self.fileType == '.csv':
            file_csv = open(self.filePath,'r',encoding='UTF-8')
            file_by_lines = csv.reader(file_csv)
            for line in file_by_lines:
                name = line[0]
                id = int(line[1])
                self.Students.append(Student(name, id))
                print(name, '的信息已读出\n')
        return self.Students

             
                   
def Joseph(Students, step):
    
      n = len(Students)
     
      for i in range(n):
        print('Name:', Students[step%len(Students)-1].name, 'ID:', Students[step%len(Students)-1].id)
        del Students[step%len(Students)-1]
        if len(Students)==0:
            print('over')
        else:
            step = (step + step-1) % len(Students)

filePath = 'D:/Python学习/test.txt'
fileInfo = ReadFile(filePath)
Joseph(fileInfo.getStudentInfo(),2)
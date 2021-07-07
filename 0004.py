import re

fin = open('D:/Pyhton学习/11.txt', 'r')
strs = fin.read()

reObj = re.compile('\b?(\w+)\b?') #编译为一个pattern对象
words = reObj.findall(strs) #取出对象

wordDict = dict() #字典

for word in words:  #当属于对象时
    if word.lower() in wordDict: #如果是小写
        wordDict[word.lower()] += 1 #单词数+1
    else:
        wordDict[word.lower()] = 1 

for key, value in wordDict.items():
    print('%s: %s' % (key, value))

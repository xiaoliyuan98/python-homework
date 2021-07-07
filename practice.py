import re

fin = open('11.txt', 'r')
strs = fin.read()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(strs)

wordDict = dict()

for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word.lower()] = 1

for key, value in wordDict.items():
    print('%s: %s' % (key, value))
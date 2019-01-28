# -*- coding:utf-8
# __author__ : fangli
# __create_time__ : 2018/12/3

import re;

p = re.compile('INSERT INTO', re.S);
fileContent = open('/Users/fangli/Documents/log_huifu1111', 'r', encoding='utf8').read();  # 读文件内容
paraList = p.split(fileContent)  # 根据换行符对文本进行切片

fileWriter = open('/Users/fangli/Documents/0.txt', 'a', encoding='utf8');  # 创建一个写文件的句柄
for paraIndex in range(len(paraList)):  # 遍历切片后的文本列表
    fileWriter.write(paraList[paraIndex]);  # 先将列表中第一个元素写入文件中
    if ((paraIndex + 1) % 8 == 0):  # 判断是否写够3个切片，如果已经够了
        fileWriter.close();  # 关闭当前句柄
        fileWriter = open('files/' + str((paraIndex + 1) / 8) + '.txt', 'a',
                          encoding='utf8');  # 重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
fileWriter.close();  # 关闭最后创建的那个写文件句柄
print('finished')

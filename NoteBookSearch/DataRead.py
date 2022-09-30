# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:40 PM
# @Author  : William
# @FileName: DataRead.py
# @Software: PyCharm
import pandas as pd
class DataRead(object):
    def __init__(self, path):
        self.path = path

    def postfix(self, path: str):
        '''
        判断文件后缀
        '''
        suffix = path.split(".")[-1]
        sum_suffix = ['py','xlsx','xls','html','css','js','txt','csv','json']
        if suffix in sum_suffix:
            return suffix.lower()
        else:
            return "There might be an error."

    def general_read(self, path):
        '''
        Read each line of the file and put it into a list as an individual element.
        :param path:
        :return:
        '''
        with open(path, 'r', encoding = 'utf-8') as f:
            return f.readlines() #This allows us to read spacelines.

    def decide_suffix(self, path,suffix):
        '''
        判断文件后缀，使用对应函数打开文件
        :return:
        '''
        if suffix == 'py':
            content_list = self.general_read(path)
        # print(content_list)
        # print('-------------------------------------------------------')
        for line_number, content in enumerate(content_list):
            if content != '\n':
                content = str(line_number + 1) + content
                print(content, end='')
            else:
                pass






    def main(self):
        suffix = self.postfix(path=self.path)
        self.decide_suffix(self.path,suffix)


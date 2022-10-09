# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:40 PM
# @Author  : William
# @FileName: DataManager.py
# @Software: PyCharm
import pandas as pd
from uuid import uuid4
# 此库需要用到static variable
TEMPLATE_CONTENT = "FingerPrint = {uuid};Line:{index}>>>{content}"
TEMPLATE_CONTENT_WITH_PATH = "FilePath:{path}\n{content}"
class DataRead(object):
    def __init__(self, path):
        self.path = path

    # ----------------------------------搜索器----------------------------------
    def postfix(self, path: str):  # 服务于搜索器
        '''
        判断文件后缀
        '''
        suffix = path.split(".")[-1]
        sum_suffix = ['py', 'xlsx', 'xls', 'html', 'css', 'js', 'txt', 'csv', 'json']
        if suffix in sum_suffix:
            return suffix.lower()
        else:
            return "There might be an error."

    def general_read(self, path):  # 服务于搜索器
        '''
        Read each line of the file and put it into a list as an individual element.
        :param path:
        :return:
        '''
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()  # This allows us to read spacelines.

    def decide_suffix(self, path, suffix):  # 服务于搜索器
        '''
        判断文件后缀，使用对应函数打开文件
        :return:
        '''
        if suffix == 'py':
            return self.general_read(path)
        elif suffix == "txt":
            return self.general_read(path)

    # ----------------------------------搜索器----------------------------------

    # ----------------------------------检索器----------------------------------
    def parse(self, content):  # 服务于检索器
        """
        This part creates a form of data in order for us to search easier. The form is now
        a string.  This makes it easier for us to use the regx
        :param content:
        :return:
        """
        uuid = uuid4()
        line_content_str = ''
        for line_number, content in enumerate(content):
            if content != '\n':
                content = TEMPLATE_CONTENT.format(uuid = uuid, index=line_number + 1, content=content)
                line_content_str = line_content_str + content

            else:
                pass

        return TEMPLATE_CONTENT_WITH_PATH.format(path = self.path, content = line_content_str)

    # ----------------------------------检索器----------------------------------

    # ----------------------------------总体调动----------------------------------
    def main(self):
        suffix = self.postfix(path=self.path)
        content = self.decide_suffix(self.path, suffix)  # 判断文件后缀，使用对应函数打开文件
        return self.parse(content)

# ----------------------------------总体调动----------------------------------



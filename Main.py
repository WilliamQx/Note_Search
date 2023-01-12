# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:23 PM
# @Author  : William
# @FileName: Main.py
# @Software:

from NoteBookSearch import NoteBookSearch
from NoteBookSearch import DataManager
from NoteBookSearch import test
from NoteBookSearch import Search_engine
import os
import re
from uuid import uuid4

abs_path = r"C:\Users\Willi\Documents\Note_Seach\build\lib\NoteBookSearch"
d = DataManager(abs_path)
#d.run()
s = Search_engine(language='zh_cn')
s.search("断文件")
# print(type(s.json_to_dict("PATH_JSON.json")))
# print(s.json_to_dict("PATH_JSON.json"))
# print('----------------------------------------------------------------')
# print(s.match_uuid("断文件","PATH_JSON.json"))
# print(d.postfix(abs_path)) #得到后缀
# print(d.main())
# d.path_generator()
# a = uuid4()
# print(a)

# s = '''#0print("aiyc")
# #1a = 1
# #2b = 1
# #3c = 1y
# #4abc = 199
# #5print(a)'''
#
# pattern = '(\d+).*?(print).*?'
# result = re.findall(pattern,s)
# print(result)
# path_lst = d.path_generator()
# for path in path_lst:
#     r = d.main(path)
    # print(r)
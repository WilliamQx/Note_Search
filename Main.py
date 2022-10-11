# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:23 PM
# @Author  : William
# @FileName: Main.py
# @Software:

from NoteBookSearch import NoteBookSearch
from NoteBookSearch import DataManager
from NoteBookSearch import test
import re
from uuid import uuid4
abs_path = r"C:\Users\Willi\Documents\Note_Seach\build\lib\NoteBookSearch"
d = DataManager(abs_path)
d.run()
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
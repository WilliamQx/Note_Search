# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:23 PM
# @Author  : William
# @FileName: Main.py
# @Software:

from NoteBookSearch import NoteBookSearch
from NoteBookSearch import DataRead
from NoteBookSearch import test
import re
from uuid import uuid4
abs_path = r"C:\Users\Willi\Documents\Note_Seach\NoteBookSearch\DataManager.py"
d = DataRead(abs_path)
print(d.postfix(abs_path)) #得到后缀
print(d.main())
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
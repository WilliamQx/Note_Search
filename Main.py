# -*- coding: utf-8 -*-
# @Time    : 28/09/2022 6:23 PM
# @Author  : William
# @FileName: Main.py
# @Software:

from NoteBookSearch import NoteBookSearch
from NoteBookSearch import DataRead
from NoteBookSearch import test


abs_path = r"C:\Users\Willi\Documents\Note_Seach\NoteBookSearch\DataRead.py"
d = DataRead(abs_path)
print(d.postfix(abs_path)) #得到后缀
d.main()
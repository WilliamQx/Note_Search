# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 22:55
# @Author  : William
# @FileName: SEARCH_ENGINE.py
# @Software: PyCharm
import re
from pprint import pprint
from NoteBookSearch import DataManager
import json
class Search_engine():
    def __init__(self):
        with open("SEARCH_DATA_NAME.txt", "r",  encoding='utf-8') as f:
            self.search_data = f.read()

    def regex(selfself, query,  search_data):
        pattern = 'FingerPrint=(.*?);line:(\d+)>>>(.*?{query}.*)'.format(query = query)
        print(pattern, "--------------")
        result = re.findall(pattern, search_data)
        return result

    def search(self, user_search):#this is the main function
        print("Running")
        search_reseult = self.regex(user_search, self.search_data)
        path_list = self.json_to_dict()
        result_data = self.match_uuid(search_reseult, path_list)
        for path, line,  content in result_data:
            s = self.format_output()
            print(s)

    def json_to_dict(self):
        with open("PATH_JSON.json", 'r') as f:
            return json.load(f)['DictPath'] #this returns a list if dict

    def match_uuid(self,user_search,a_file):
        '''
        这里是以uuid为桥梁连接uuid_line_content的行数以及搜索内容和uuid_location的路径
        :param user_search: 用户的输入内容
        :param a_file: 搜索的大路径们也就是在这个大路径下对文件进行搜索
        :return: RETURN_FORMAT = "Location={path};Result={content};Line={line_number}"
        '''
        path_content_lineNumber = []
        uuid_line_content = self.search(user_search)
        uuid_location_dicts = self.json_to_dict(a_file)
        for uuid, line_number, content in uuid_line_content:
            for dict in uuid_location_dicts:
                if dict.get(uuid) == None:
                    continue
                path_content_lineNumber.append([dict.get(uuid)], line_number, content)
        return path_content_lineNumber

    def format_output(self, path, line, content):
        ZH_TEMPLATE = """
        --------------------Search Result--------------------
        路径：{FILE_PATH}
        第几行：{LINE}
        匹配内容：{CONTENT}
        -----------------------------------------------------
                """.format(FILE_PATH=path,
                           LINE=line,
                           CONTENT=content)
        return ZH_TEMPLATE




        # collection_list = []
        # uuid_line_content = self.search(user_search)
        # uuid_location_dicts = self.json_to_dict(a_file)
        # uuid_location_keys = []
        # for dicts in uuid_location_dicts:
        #     uuid_location_keys.append(dicts.keys())
        # print(uuid_line_content)
        # print(uuid_location_keys)
        # for location_uuids_key in uuid_location_keys:
        #     for lineNo_content in uuid_line_content:
        #         if location_uuids_key in lineNo_content:
        #             return_FORMAT = RETURN_FORMAT.format(path = uuid_location_keys[location_uuids_key], content = lineNo_content[2], line_number = lineNo_content[1])
        #             collection_list.append(return_FORMAT)
        #     return collection_list
        # for tuples in uuid_line_content:
        #     for dict in uuid_location:
        #         #collection = RETURN_FORMAT.format(path = dict[tuples[0]], content = tuples[2], line_number = tuples[1])
        #         collection_list.append(dict[tuples[0]])
        #         collection_list.append(tuples[2])
        #         collection_list.append(tuples[1])
        #     return collection_list




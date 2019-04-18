# -*- coding:utf-8 -*-

import json
import os

# 全局变量
_SESSION = None
_POST = None
_GET = None


def app():
    if _POST is not None:
        if 'db_url' in _POST.keys():
            db_url = _POST['db_url']
            if db_url == '':
                result = {'code': 400, 'result': '', 'msg': '数据库路径不能为空'}
            elif not os.path.isfile(db_url):
                result = {'code': 400, 'result': '', 'msg': '数据库不存在，请检查路径'}
            else:
                result = {'code': 200, 'result': '', 'msg': 'success'}
        else:
            result = {'code': 400, 'result': '', 'msg': '提交字段为空'}
    else:
        result = {'code': 404, 'result': '', 'msg': '404'}

    return json.dumps(result)


def test():
    s = '测试'
    print('test:%s'%s)
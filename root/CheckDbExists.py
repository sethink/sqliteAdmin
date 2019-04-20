# -*- coding:utf-8 -*-

import json
import os

class CheckDbExists():
    def __init__(self,_SESSION,_POST,_GET):
        self._SESSION = _SESSION
        self._POST = _POST
        self._GET = _GET

    def app(self):
        if self._POST is not None:
            if 'db_url' in self._POST.keys():
                db_url = self._POST['db_url']

                if db_url == '':
                    result = {'code': 400, 'result': '', 'msg': '数据库路径不能为空'}
                elif not os.path.isfile(db_url):
                    result = {'code': 400, 'result': '', 'msg': '数据库不存在，请检查路径'}
                else:
                    result = {'code': 200, 'result': '', 'msg': 'success'}
                    self._SESSION.setCookie('db_url',db_url)
            else:
                result = {'code': 400, 'result': '', 'msg': '提交字段为空'}
        else:
            result = {'code': 404, 'result': '', 'msg': '404'}
        print('json:%s'%result)
        return json.dumps(result)

    def test(self):
        print('success')
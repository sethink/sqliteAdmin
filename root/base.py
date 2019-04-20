# -*- coding:utf-8 -*-
import json
import os


def check_db_exists(_SESSION):
    db_url = _SESSION.getCookie('db_url')
    if not os.path.isfile(db_url):
        return json.dumps({'code':400,'result':'','msg':'数据库不存在，请检查路径'})
# -*- coding:utf-8 -*-

import importlib
import sqlite3
# 全局变量
_SESSION = None
_POST = None
_GET = None


def app():
    m = importlib.import_module('root.base')
    m.check_db_exists(_SESSION)


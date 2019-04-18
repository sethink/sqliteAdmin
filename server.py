# -*- coding=utf-8 -*-
import socket
import threading
import Queue
from HttpHead import HttpRequest



# 每个任务线程
class WorkThread(threading.Thread):
    def __init__(self, work_queue):
        super(WorkThread, self).__init__()
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        while True:
            func, args = self.work_queue.get()
            func(*args)
            self.work_queue.task_done()


# 线程池
class ThreadPoolManger():
    def __init__(self, thread_number):
        self.thread_number = thread_number
        self.work_queue = Queue.Queue()
        for i in range(self.thread_number):  # 生成一些线程来执行任务
            thread = WorkThread(self.work_queue)
            thread.start()

    def add_work(self, func, *args):
        self.work_queue.put((func, args))


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    request = sock.recv(1024)
    http_req = HttpRequest()
    http_req.passRequest(request)
    # sock.send(http_req.getResponse().encode('utf-8'))
    sock.send(http_req.getResponse())

    sock.close()


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(10)
    thread_pool = ThreadPoolManger(5)
    print('listen in %s:%d' % ('0.0.0.0', 9999))
    while True:
        sock, addr = s.accept()
        thread_pool.add_work(tcp_link, *(sock, addr))


# def test1():
#     # 实现功能：执行check_db_exists模块里的test()函数
#     # 因为check_db_exists模块不确定，也有可能会变成别的模块
#     m = __import__('root.check_db_exists')
#
#     print('module:%s'%m)
#     print('dir(m):%s'%dir(m))
#
#     # 成功（这样就限制了只能使用制定模块）
#     m.check_db_exists.test()
#
#     # 会报错
#     m.test()
#

if __name__ == '__main__':
    start_server()
    pass

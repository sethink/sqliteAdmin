# -*- coding=utf-8 -*-
import socket
import threading
import Queue
import importlib
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

#
# def test1():
#     file_path = 'root.CheckDbExists'
#     file_name = 'CheckDbExists'
#
#     m = __import__(file_path,fromlist=[file_name])
#     n = getattr(m,file_name)
#
#
#     print(m)
#     print(dir(m))
#     print(n)
#     n().test()



if __name__ == '__main__':
    start_server()
    # test1()
    pass

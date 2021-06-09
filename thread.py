#导入包，配合队列实现线程池
from threading import Thread
from queue import Queue
import time,threading

class MyThread:
    #线程池初始化
    def __init__(self,n):   #n  线程的数量
        self.queue = Queue()  #放任务的队列
        for i in range(n):
            #创建线程，self.worker线程执行的函数，并指定线程为守护线程
            # 1、Thread.setDaemon(True)，thread.join()(设置为True守护线程子线程需加join方法，子线程未完成任务，主线程不退出等待子线程完成任务)
            # 2、Thread.setDaemon(False)(设置为False子线程不需要加join方法，主线程完成退出，子线程在后台继续运行)
            Thread(target=self.worker,daemon=True).start()

    
    #线程执行的函数，即用来执行任务函数的函数
    def worker(self):
        while True:
            print("当前线程："+threading.current_thread().getName())
            #从队列中取任务func表示任务函数，args,kwargs是任务函数的参数
            func,args,kwargs = self.queue.get()
            #任务函数,执行此函数完成一系列功能
            func(*args,**kwargs)
            #任务函数执行完毕，表示队列的get()任务完成，需要task_done()表示任务完成
            self.queue.task_done()
     
    #往队列中放任务函数，参数func 表示任务函数，args和kwargs表示任务函数参数
    def apply_async(self,func,args=(),kwargs={}):
        #往队列中放任务
        print(args)
        self.queue.put((func,args,kwargs))
        
    #用来判断队列中的所有任务是否完成
    #worker中任务函数执行完一次就会task_done()，如果有10次任务，task_done()次数不够10次，那么join不会执行
    def join(self):
        #用来判断队列任务是否执行完毕
        self.queue.join()



# 以下为测试使用
#下载图片
def DownloadImg(img_url,dir_name,img_name):
    time.sleep(2)
    print("图片下载成功")

# 创建5个线程池
threads = MyThread(5)
# 测试用的DownloadImg方法参数
img_url,dir_name,img_name='test1','test2','test3'
# 循环往队列放数据
for x in range(1,100):
    threads.apply_async(func=DownloadImg,args=(img_url,dir_name,img_name))
threads.join()

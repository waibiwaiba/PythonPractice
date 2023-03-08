import subprocess


completed = subprocess.run(['dir', '/d'], shell=True)
print('returncode:', completed.returncode)

# safer version
completed = subprocess.run(['cmd', '/c', 'dir /d'], capture_output=True, text=True)
print(completed.stdout)
print('returncode:', completed.returncode)

completed = subprocess.run(['cmd', '/c', 'echo %USERPROFILE%'], shell=True)
print('returncode:', completed.returncode)


completed = subprocess.run(['cmd', '/c', 'dir', '/d'], capture_output=True, text=True)
print('returncode:', completed.returncode)
print('stdout:', completed.stdout)
print('stderr:', completed.stderr)


# 简单的命令行执行
completed = subprocess.run(['dir', '/d'], shell=True)
print('returncode:', completed.returncode)

# 获取命令行输出
output = subprocess.check_output(['dir'], shell=True, text=True)
print(output)


import subprocess

try:
    completed = subprocess.run(
        'dir /d', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='gbk')
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
    print('stderr:', err.stderr)

else:
    print('returncode:', completed.returncode)
    print('stdout:', completed.stdout)
    print('stderr:', completed.stderr)


import subprocess

try:
    completed = subprocess.run(['ping', 'www.baidu.com', '-t'], timeout=5)
except subprocess.TimeoutExpired:
    print('Ping timed out after 5 seconds.')


import threading

class BankAccount:
    """银行账户类"""

    def __init__(self, balance=0):
        """初始化账户余额"""
        self.balance = balance

    def withdraw(self, amount):
        """取款操作"""
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount} succeeded")
        else:
            print(f"Withdraw {amount} failed")

# 创建一个银行账户实例
account = BankAccount(balance=100)

# 创建多个线程进行取款操作
threads = []
for i in range(10):
    t = threading.Thread(target=account.withdraw, args=(10,))
    threads.append(t)

# 启动多个线程
for t in threads:
    t.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()

# 输出最终余额
print(f"Final balance: {account.balance}")


import threading
import time
balance = 0
lock = threading.Lock()

def deposit(n):
    global balance
    for i in range(1000000):
        lock.acquire()      # 获取锁
        balance += n
        lock.release()      # 释放锁

def withdraw(n):
    global balance
    for i in range(1000000):
        lock.acquire()      # 获取锁
        balance -= n
        lock.release()      # 释放锁

if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=deposit, args=(1,))
    t2 = threading.Thread(target=withdraw, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('balance:', balance)
    print('timecost:',time.time()-start_time)


import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, balance is now {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, balance is now {self.balance}")
            else:
                print(f"Insufficient balance, cannot withdraw {amount}")

def run_threads(account):
    for _ in range(10):
        account.deposit(1)
        account.withdraw(1)

if __name__ == '__main__':
    account = BankAccount(0)
    threads = [threading.Thread(target=run_threads, args=(account,)) for _ in range(10)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f"Final balance: {account.balance}")



import threading
import time
import queue

# 定义队列对象
q = queue.Queue()

# 定义生产者线程
class ProducerThread(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 5:
                for i in range(5):
                    count += 1
                    q.put('product-' + str(count))
                print('produced 5 products')
            time.sleep(2)

# 定义消费者线程
class ConsumerThread(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 0:
                product = q.get()
                print('consumed product:', product)
            time.sleep(1)

# 创建生产者线程和消费者线程，并启动它们
producer_thread = ProducerThread()
consumer_thread = ConsumerThread()
producer_thread.start()
consumer_thread.start()



import threading

def my_timer():
    print("定时器执行了！")

timer = threading.Timer(10.0, my_timer)
timer.start()

# 等待3秒后取消定时器的执行
event = threading.Event()
event.wait(3.0)
if not event.is_set():
    timer.cancel()
    print("定时器已取消！")



import logging

logging.basicConfig(level=logging.DEBUG)

def foo():
    logging.debug("Debug information")
foo()


import threading
import time

def print_time():
    while True:
        print("Current time is {}".format(time.time()))
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=print_time, daemon=True)
    t.start()

    time.sleep(5)
    print("Main thread ends")


import threading
import time

# 创建 Event 对象
event = threading.Event()

def wait_for_event():
    print("Thread {} is waiting for event...".format(threading.current_thread().name))
    event.wait()
    print("Thread {} received the event!".format(threading.current_thread().name))

def set_event():
    print("Thread {} is sleeping for 3 seconds...".format(threading.current_thread().name))
    time.sleep(3)
    event.set()
    print("Thread {} set the event!".format(threading.current_thread().name))

# 创建两个线程
t1 = threading.Thread(target=wait_for_event)
t2 = threading.Thread(target=set_event)

# 启动两个线程
t1.start()
t2.start()

# 等待两个线程结束
t1.join()
t2.join()



import queue
import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self, queue, event):
        super().__init__()
        self.queue = queue
        self.event = event

    def run(self):
        while not self.event.is_set():
            data = random.randint(0, 100)
            self.queue.put(data)
            print(f"Produced {data}")
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, queue, event):
        super().__init__()
        self.queue = queue
        self.event = event

    def run(self):
        while not self.event.is_set() or not self.queue.empty():
            try:
                data = self.queue.get(timeout=5)
                print(f"Consumed {data}")
            except queue.Empty:
                print("Queue is empty")

if __name__ == "__main__":
    queue = queue.Queue()
    event = threading.Event()

    producer = Producer(queue, event)
    consumer = Consumer(queue, event)

    producer.start()
    consumer.start()

    time.sleep(3)
    event.set()
    print("Event is set")



import threading

class Printer:
    def __init__(self):
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.num = 0

    def odd(self):
        with self.cond:
            while self.num < 10:
                if self.num % 2 == 0:
                    self.cond.wait()
                else:
                    print(self.num)
                    self.num += 1
                    self.cond.notify()

    def even(self):
        with self.cond:
            while self.num < 10:
                if self.num % 2 != 0:
                    self.cond.wait()
                else:
                    print(self.num)
                    self.num += 1
                    self.cond.notify()

p = Printer()
t1 = threading.Thread(target=p.odd)
t2 = threading.Thread(target=p.even)
t1.start()
t2.start()
t1.join()
t2.join()


import threading

def worker(barrier):
    print(f"Worker thread {threading.current_thread().name} is waiting at the barrier...")
    barrier.wait()
    print(f"Worker thread {threading.current_thread().name} passed the barrier!")

def my_action():
    print("All threads have arrived at the barrier!")

if __name__ == "__main__":
    num_threads = 5
    
    barrier = threading.Barrier(num_threads, action=my_action)

    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(barrier,), name=f"Thread-{i}")
        t.start()


import threading
import time

def counter(stop_event):
    count = 0
    while not stop_event.is_set():
        # print("stop_event hasn't been set.")
        count += 1
        print(f"Count: {count}")
        time.sleep(0.5)

def main():
    stop_event = threading.Event()
    threads = []
    for i in range(2):
        t = threading.Thread(target=counter, args=(stop_event,))
        t.start()
        threads.append(t)
    
    time.sleep(5)
    print("stop_event has been set.")
    stop_event.set()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()



"""random integer"""
import random
print(random.randint(0, 10))


"""second largest. If you want smallest, max->min"""
nums = [5, 12, 54, 87, 55, 69, 23, 17]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)


"""recursive decimal->binary"""
def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n // 2)
    print(n % 2, end="")
print("13")
dec_to_binary(13)
print("")

"""recursive reverse string print"""
def recursive_reverse_str_print(str):
    print(str[-1], end="")
    if len(str) > 1:
        recursive_reverse_str_print(str[:-1])
str1 = "abcde"
print(str1)
recursive_reverse_str_print(str1)


'''reverse str using stack'''
def reverse_stack(str):
    stack = []
    for letter in str:
        stack.append(letter)
    # stack.reverse(): reverse a list.
    while len(stack) > 0:
        print(stack.pop(), end="")
print("")
reverse_stack("abcde")
print("")


'''reverse using list.reverse()'''
str1 = "abcde"
l1 = list(str1)
print(l1)
l1.reverse()
print(l1)
for letter in l1:
    print(letter, end="")
print("")

# import threading
# import time
# import queue

# # 定义队列对象
# q = queue.Queue()

# # 定义生产者线程
# class ProducerThread(threading.Thread):
#     def __init__(self, exit_event):
#         super().__init__()
#         self.exit_event = exit_event

#     def run(self):
#         global q
#         count = 0
#         while not self.exit_event.is_set():
#             if q.qsize() < 5:
#                 for i in range(5):
#                     count += 1
#                     q.put('product-' + str(count))
#                 print('produced 5 products')
#             time.sleep(2)

# # 定义消费者线程
# class ConsumerThread(threading.Thread):
#     def __init__(self, exit_event):
#         super().__init__()
#         self.exit_event = exit_event

#     def run(self):
#         global q
#         while not self.exit_event.is_set():
#             if q.qsize() > 0:
#                 product = q.get()
#                 print('consumed product:', product)
#             time.sleep(1)

# # 创建退出事件
# exit_event = threading.Event()

# # 创建生产者线程和消费者线程，并启动它们
# producer_thread = ProducerThread(exit_event)
# consumer_thread = ConsumerThread(exit_event)
# producer_thread.start()
# consumer_thread.start()

# time.sleep(3)
# exit_event.set()
# producer_thread.join()
# consumer_thread.join()



import threading
import time
import queue

# 定义队列对象
q = queue.Queue()

# 定义生产者线程
class ProducerThread(threading.Thread):
    def __init__(self, exit_event):
        super().__init__()
        self.exit_event = exit_event
    def run(self):
        global q
        count = 0
        while not self.exit_event.is_set():
            if q.qsize() < 5:
                for i in range(5):
                    count += 1
                    q.put('product-' + str(count))
                print('produced 5 products')
            time.sleep(2)

# 定义消费者线程
class ConsumerThread(threading.Thread):
    def __init__(self, exit_event):
        super().__init__()
        self.exit_event = exit_event
    def run(self):
        global q
        while not self.exit_event.is_set():
            if q.qsize() > 0:
                product = q.get()
                print('consumed product:', product)
            time.sleep(1)
stop_event = threading.Event()
# 创建生产者线程和消费者线程，并启动它们
producer_thread = ProducerThread(stop_event)
consumer_thread = ConsumerThread(stop_event)
producer_thread.start()
consumer_thread.start()
time.sleep(3)
stop_event.set()
producer_thread.join()
consumer_thread.join()
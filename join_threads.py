import time
from threading import Thread

def child():
    print("Child thread doing work...")
    time.sleep(5)
    print("Child Thread done...")

def parent():
    t = Thread(target=child, args=([]))
    t.start()
    print("Parent thread is waiting...")
    t.join()
    print("Parent thread is unblocked...")

parent()
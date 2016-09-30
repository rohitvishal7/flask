import threading
from threading import Thread
import time
import random

class Producer(Thread):
    def __init__(self, threadName, condition, list_of_nos):
        Thread.__init__(self)
        self.name = threadName
        self.condition = condition
        self.list_of_nos = list_of_nos
        
    def run(self):
        while True:
            randomNo = random.randint(0, 100)
            print('Producer acquired lock')
            self.condition.acquire()
            self.list_of_nos.append(randomNo)
            print('Produced no ', str(randomNo))
            self.condition.notify()
            print('Producer released lock')
            self.condition.release()
            time.sleep(1)
            
class Consumer(Thread):
    def __init__(self, threadName, condition, list_of_nos):
        Thread.__init__(self)
        self.name = threadName
        self.condition = condition
        self.list_of_nos = list_of_nos
        
    def run(self):
        while True:
            print('\tConsumer acquired lock')
            self.condition.acquire()
            while True:
                print('\tConsumed: ', self.list_of_nos.pop())
                break
            print('\tConsumer released lock')
            self.condition.wait()
            self.condition.release()

def main():
    list_of_nos = []
    condition = threading.Condition()
    producerThread = Producer("PRODUCER", condition, list_of_nos)
    consumerThread = Consumer("CONSUMER", condition, list_of_nos)
    producerThread.start()
    consumerThread.start()
    producerThread.join()
    consumerThread.join()
    print('Exiting app!!')
        
if __name__ == '__main__':
    main()
    
    
    
    
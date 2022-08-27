from multiprocessing import Process

from class_code.consumers.consumer1 import Consumer1
from class_code.consumers.consumer2 import Consumer2

if __name__ == '__main__':
    consumers = [Consumer1(), Consumer2()]

    process_list = []
    for consumer in consumers:
        process = Process(target=consumer.run)
        process.start()
        process_list.append(process)

    for process in process_list:
        process.join()

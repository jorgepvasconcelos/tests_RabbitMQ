from multiprocessing import Process

from func_code.consumers.consumer1 import consumer1
from func_code.consumers.consumer2 import consumer2


if __name__ == '__main__':
    consumers = [consumer1, consumer2]

    process_list = []
    for consumer in consumers:
        process = Process(target=consumer)
        process.start()
        process_list.append(process)

    for process in process_list:
        process.join()

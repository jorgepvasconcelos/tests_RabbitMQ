import threading
import time
from multiprocessing import Process

from func_code.consumers.consumer1 import consumer1
from func_code.consumers.consumer2 import consumer2

from logging import info

def run_multiprocessing():
    consumers = [consumer1, consumer2]

    process_list = []
    for consumer in consumers:
        process = Process(target=consumer)
        process.start()
        process_list.append(process)

    for process in process_list:
        process.join()


def run_threading():
    consumers = [consumer1, consumer2]

    process_list = []
    for consumer in consumers:
        thread = threading.Thread(target=consumer)
        thread.start()
        process_list.append(thread)

    for process in process_list:
        process.join()


if __name__ == '__main__':
    print('iniciando os consumers')
    info('iniciando os consumers')
    time.sleep(10)
    run_threading()

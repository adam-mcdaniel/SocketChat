#!/usr/bin/python3
# coding: latin-1
import socket
import random
import threading
import Queue
import time
#ip = input('IP\n')
#port = input('Port\n')
#duration = input('Number of seconds\n')
#ip = '62.116.130.8'
#ip = '192.168.1.125'
#ip = '99.17.89.188'
while True:
    try:
        host = socket.gethostbyname(socket.gethostname())
        serverip = str(raw_input('Server\'s Ip:'))
        serverport = int(raw_input('Server\'s Port:'))
        port = 0
        server = (serverip,serverport)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
        break
    except Exception as e:
        print(e)

q = Queue.Queue()
def exampleJob(worker):
    while True:
        if worker == 0:
            try:
                data, addr = s.recvfrom(1024)
                data = data.decode('utf-8')
                data = str(data)
                print(data)
            except Exception as e:
                print(e)
        if worker == 1:
            try:
                time.sleep(0.25)
                message = str(raw_input(''))
                s.sendto(str.encode(message),server)
            except Exception as e:
                print(e)
##    with print_lock:
##        print(threading.current_thread().name,worker)
# The threader thread pulls an worker from the Queue and processes it
def threader():
    while True:
        # gets an worker from the Queue
        worker = q.get()
        # Run the example job with the avail worker in Queue (thread)
        exampleJob(worker)
        # completed with the job
        q.task_done()
# Create the Queue and threader 
# how many threads are we going to allow for
for x in range(2):
     t = threading.Thread(target=threader)
     # classifying as a daemon, so they will die when the main dies
     t.daemon = True
     # begins, must come after daemon definition
     t.start()
start = time.time()
# 200 jobs assigned.
for worker in range(2):
    q.put(worker)
# wait until the thread terminates.
q.join()
# with 100 workers and 200 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:',time.time() - start)

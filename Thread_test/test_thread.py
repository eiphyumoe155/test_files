import threading
from datetime import datetime

def time(start, end):
     result = end - start
     return result

threads = []
for i in range(3):
    start = datetime.now()
    for j in range(100):
        print(j)
    end = datetime.now()
    t = threading.Thread(target=time, args=(start,end))
    print("t is ", t)
    t.start()
    print("time is", end - start)
    threads.append(t)

for t in threads:
    t.join()


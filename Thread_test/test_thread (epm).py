import threading
from datetime import datetime

global result
def translate_work(data):
    userCount = 0
    for i in range(1,100000000,1):
        userCount = i
    result =  data+str(userCount)
    print(result)


def translate(data):
    result  = []
    for i in data:
        thread = threading.Thread(target=translate_work, args=(i,))
        thread.daemon = False
        thread.start()
        thread.join()
    return result

import time

start_time = time.time()
translate_work("user-1# :")
translate_work("user-2# :")
print(time.time()-start_time)

print("############# with thread ###########")
start_time = time.time()
result = translate(data=["user-1# :","user-2# :"])
print(time.time()-start_time)
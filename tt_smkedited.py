import concurrent.futures
import threading
from multiprocessing import Pool
import time

def translate_work(data):
    userCount = 0
    for i in range(1,100000000,1):
        userCount = i
    return data+str(userCount)

'''def return_callback(result):
    print(f'{result}')'''

def translate(user_data) :
    
    with Pool() as pool:
        result = []
        for p in [pool.apply_async(func=translate_work, args=(user_data[i],))for i in range(len(user_data))]:
            p.wait()
            result.append(p.get())
        return result
           

if __name__ == '__main__':
    start_time = time.time()
    print(translate_work("user-1# :"))
    print(translate_work("user-2# :"))
    print(translate_work("user-3# :"))
    print(translate_work("user-4# :"))
    print(time.time()-start_time)

    print("############# with thread ###########")
    start_time = time.time()
    result = translate(user_data=["user-1# :","user-2# :","user-3# :","user-4# :"])
    #result = translate(user_data=["user-1# :","user-2# :"])
    print(result)
    print(time.time()-start_time)
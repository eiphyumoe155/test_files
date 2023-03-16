from multiprocessing import Pool
import time

def translate_work(data):
    userCount = 0
    for i in range(1,100000000,1):
        userCount = i
    print(data+str(userCount))
def translate(user_data) :
    with Pool() as pool:
        for p in [pool.apply_async(func=translate_work, args=(user_data[i],))for i in range(len(user_data))]:
            p.wait()
if __name__ == '__main__':
    start_time = time.time()
    translate_work("user-1# :")
    translate_work("user-2# :")
    translate_work("user-3# :")
    translate_work("user-4# :")
    print(time.time()-start_time)


    print("############# with thread ###########")
    start_time = time.time()
    result = translate(user_data=["user-1# :","user-2# :","user-3# :","user-4# :"])
    print(time.time()-start_time)
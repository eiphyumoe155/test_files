import asyncio
import logging
import time


async def translate_work(data):
    userCount = 0
    for i in range(1,100000000,1):
        userCount = i
    result =  data+str(userCount)
    print(result)

def translate_work1(data):
    userCount = 0
    for i in range(1,100000000,1):
        userCount = i
    result =  data+str(userCount)
    print(result)
    
async def main(data):
    
    await asyncio.gather(*[translate_work(i,) for i in data]) # awaits completion of all tasks
  

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main(data=["user-1# :","user-2# :"]))
    print("Duration with thread is ", time.time() - start)


    s = time.time()
    translate_work1("user-1#")
    translate_work1("user-2#")
    print("Duration without thread is ", time.time() - s)
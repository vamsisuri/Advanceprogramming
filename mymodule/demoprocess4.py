from concurrent.futures import ThreadPoolExecutor
import time
import random
def study():
    for i in range(5):
        print("I am reading book")
        time.sleep(2)
def listening():
    for i in range(5):
        print("Listening to music")
        time.sleep(3)

if __name__=='__main__':
     with ThreadPoolExecutor(max_workers=2) as pool:
         pool.submit(study)
         pool.submit(listening)
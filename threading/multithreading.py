import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print("STARTING")
    time.sleep(seconds)
    print("FINISIHING")
arr=[]
def main():
    for i in range (3):
        threads=threading.Thread(target=func,args=[i])
        arr.append(threads)
        threads.start()
    for i in arr:
        i.join()    
def threadpullexecutor():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func,5)
        future = executor.submit(func,3)
        l=[5,4,3,2,1]
        x=executor.map(func,l)
        for result in x:
            print(result)
        
threadpullexecutor()   




# never name a file with same name as a build in file , it you do, it will create error when you want to import that build in file to the current file where both has same name like for eg: there is a file called threading, so if ...
import threading
import time

def work(name):
    for i in range(1,3):
        print(f"hello {name} ")
        time.sleep(1)

t1 = threading. Thread(target=work, args=(["mohan"]))
t2 = threading. Thread(target=work, args=(['kumar' ]))
t1.start()
t2.start()
t1.join()
t2.join()
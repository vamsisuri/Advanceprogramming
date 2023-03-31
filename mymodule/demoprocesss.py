import multiprocessing
def cal():
    for i in range(10):
        print(i**3)
def cal2(number):
    for i in range(number):
        print(i**4)
if __name__=='__main__':
    print(multiprocessing.cpu_count())
    p1=multiprocessing.Process(target=cal)
    p2=multiprocessing.Process(target=cal2,args=(10000,))
    print(p1.name)

    p2=multiprocessing.Process(target=cal2,args=(10,))
    print(p2.name)


    p1.start()
    print(p1.pid)
    p2.start()
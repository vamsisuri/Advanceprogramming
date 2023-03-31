import multiprocessing

def cal_square(numbers):

    for i in numbers:
        q.put(i*i)


if __name__=='__main__':
    num=[1,2,3,7,8]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=cal_square,args=(num,q))
    print(p1.name)
    p1.start()
    p1.join()
    while q.empty() is False:
        print(q.get())
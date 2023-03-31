import multiprocessing

def cal_square(numbers,res,v):
    v.value=5.6

    for i,n in enumerate(numbers):
        res[i]=n*n

    print(multiprocessing.current_process())

if __name__=='__main__':
    num=[1,2,3,7,8]
    #q=multiprocessing.Queue()
    res=multiprocessing.Array('i',5)
    v=multiprocessing.Value('d',0.0)
    p1=multiprocessing.Process(target=cal_square,args=(num,res,v))
    print(p1.name)
    print(multiprocessing.current_process())
    p1.start()
    p1.join()
    # while q.empty() is False:
    #     print(q.get()
    print(res[:],v.value)
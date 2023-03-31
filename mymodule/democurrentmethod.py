import multiprocessing
class Myclass(multiprocessing.Process):
    def demo1(self):
        print("Hello from demo1")
    def run(self) ->None:
        print("hi")
        self.demo1()

if __name__=='__main__':
    p=Myclass()
    p.start()
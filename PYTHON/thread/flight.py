from threading import Lock, RLock, Thread, current_thread
class Hotel:
    def __init__(self,t):
        self.available_sear = t 
        self.l = RLock() 

    def abcd(self):
        print("the ticket got booked")    

    def reserve(self,need_seat):
        
        self.l.acquire()
        print("AVAILABLE SEAT IS : ",self.available_sear ," requre is : ",need_seat)
        if self.available_sear>=need_seat:
            #name1 = current_thread().getname()
            print("give ",need_seat," to ")
            self.available_sear-=need_seat
        else:
            print("sorry")
        self.l.release()
        self.abcd()

f = Hotel(7)
t1 = Thread(target=f.reserve,args=(1,),name='abhay')
t2 = Thread(target=f.reserve,args=(2,),name='aman')
t3 = Thread(target=f.reserve,args=(3,),name='abha')
t4 = Thread(target=f.reserve,args=(2,),name='ama')
t5 = Thread(target=f.reserve,args=(1,),name='ama')
t6 = Thread(target=f.reserve,args=(1,),name='ama')
t7 = Thread(target=f.reserve,args=(1,),name='ama')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
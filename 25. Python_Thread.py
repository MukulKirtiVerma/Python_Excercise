# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:51:50 2018

@author: james
"""
"""
Running several threads is similar to running several different programs concurrently, but with the following benefits −

Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

It can be pre-empted (interrupted).

It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.

There are two different kind of threads −

kernel thread
user thread

Kernel Threads are a part of the operating system, while the User-space threads are not implemented in the kernel.

There are two modules which support the usage of threads in Python3 −

_thread
threading
The thread module has been "deprecated" for quite a long time. Users are encouraged to use the threading module instead. Hence, in Python 3, the module "thread" is not available anymore. However, it has been renamed to "_thread" for backwards compatibilities in Python3.

Starting a New Thread
To spawn another thread, you need to call the following method available in the thread module −

_thread.start_new_thread ( function, args[, kwargs] )
This method call enables a fast and efficient way to create new threads in both Linux and Windows.

The method call returns immediately and the child thread starts and calls function with the passed list of args. When the function returns, the thread terminates.

Here, args is a tuple of arguments; use an empty tuple to call function without passing any arguments. kwargs is an optional dictionary of keyword arguments.

Example
"""
import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time())))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")


#=================================================================
def print_time1( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
def print_time2( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))      

# Create two threads as follows
try:
   _thread.start_new_thread( print_time1, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time2, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
   

#=================================================================
l=[1,2,3,4,5,6,7,8,9,10]

def sq(l):
    for i in l:
        print(" sq: ",i*i)
        time.sleep(1)
def qu(l):
    for i in l:
        print(" qu : ",i*i*i)
        time.sleep(3)
_thread.start_new_thread(sq,(l,))
_thread.start_new_thread(qu,(l,))
   


#time comperison   ================================================
import time

l1=[]
l2=[]
def sq( ):
   for i in range(0,10000000):
       l1.append(i*i)
   print("done squer")

def qu( ):
   for i in range(0,10000000):
       l2.append(i*i*i)
   print("done qube")

# Create two threads as follows
try:
  start = time.time() 
  sq() 
  qu()
  end = time.time()
  print(end - start )
except:
   print ("Error: unable to start thread")   


#==================================================================
l1=[]
l2=[]
def sq( ):
   for i in range(0,10000000):
       l1.append(i*i)
def qu( ):
   for i in range(0,10000000):
       l2.append(i*i*i)
   print("done qube")
  

# Create two threads as follows
try:
   start = time.time() 
   _thread.start_new_thread( sq,() )
   _thread.start_new_thread( qu,() )
   end = time.time()
   print(end - start )
   
except:
   print ("Error: unable to start thread")   


"""================================================================
run() − The run() method is the entry point for a thread.

start() − The start() method starts a thread by calling the run method.

join() − The join() waits for threads to terminate.

isAlive() − The isAlive() method checks whether a thread is still executing.

getName() − The getName() method returns the name of a thread.

setName() − The setName() method sets the name of a thread.
"""



#================================================================
import time, threading, os
def f1(arg1):
    for i in range(arg1):
        time.sleep(1)
        print (threading.active_count())
        print (threading.enumerate())


t = threading.Thread(name="MyThread1", target=f1, args=(7,))
t.start()



#================================================================

import threading
import time
exitFlag = 0
class myThread ():
   def __init__(self, x, y, z):
      threading.Thread.__init__(self)
      self.threadID = x
      self.name = y
      self.counter = zthreading.Thread
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter)
      print ("Exiting " + self.name)

def print_time(threadName, counter):
    delay=5
    while delay:
      time.sleep(counter)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      delay -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
print ("Exiting Main Thread")



#.join=========================================================
import threading
import time
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


#coustom threding & isalive================================================
import threading
import time
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()

print("Thread  is alive", thread1.isAlive())
print("Thread  is alive", thread2.isAlive())
thread2.start()
thread1.join()
thread2.join()
print("Thread  is alive", thread1.isAlive())
print("Thread  is alive", thread2.isAlive())
print ("Exiting Main Thread")




#getname
import threading
import time
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print()
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)


# Start new Threads
thread1.start()

print("check tread name  ",thread1.getName())
thread1.setName("Thread-3")
print("check tread name  ",thread1.getName())

thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")
   


"""===============================================================
Synchronizing Threads
The threading module provided with Python includes a simple-to-implement 
locking mechanism that allows you to synchronize threads.
 A new lock is created by calling the Lock() method, which returns the 
 new lock.

The acquire(blocking) method of the new lock object is used to\
 force the threads to run synchronously.
 The optional blocking parameter enables you to control whether
 the thread waits to acquire the lock.

If blocking is set to 0, the thread returns immediately 
with a 0 value if the lock cannot be acquired and with a 1 if 
the lock was 
acquired. If blocking is set to 1, the thread blocks and 
wait for the lock to be released.

The release() method of the new lock object is used to release
 the lock when 
it is no longer required.
The Threading Module
"""



import threading
import time

class myThread (threading.Thread):
   threadss=[]
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      myThread.threadss.append(self.name)
      print ("Starting " + self.name)
      time.sleep(3)
      
      # Get lock to synchronize threads
      if(self.name!="Thread-5"):
         
         print_time(self.name, self.counter, 3)
         
      else:
          thread1.join()
          
          print_time(self.name, self.counter, 3)
          
      # Free lock to release next thread
      

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(1, "Thread-3", 1)
thread4 = myThread(2, "Thread-4", 2)
thread5 = myThread(1, "Thread-5", 1)
thread6 = myThread(2, "Thread-6", 2)
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")


#=================================================================
import time, threading, os
def f1(arg1):
    for i in range(arg1):
        time.sleep(1)
        print (threading.current_thread().getName())
def f2(arg1):
    for i in range(arg1):
        time.sleep(1)
        print (threading.active_count())


t = threading.Thread(name="MyThread1", target=f1, args=(3,))
t2 = threading.Thread(name="MyThread2", target=f2, args=(3,))
t3 = threading.Thread(name="MyThread3", target=f2, args=(3,))
t4 = threading.Thread(name="MyThread4", target=f2, args=(3,))
t.start()
t2.start()
t3.start()
t4.start()



import time, threading, os
def f1(arg1):
    for i in range(arg1):
        
        print (threading.current_thread())

        print()
        time.sleep(2)

t = threading.Thread(name="MyThread1", target=f1, args=(6,))
t2 = threading.Thread(name="MyThread2", target=f1, args=(6,))


t.setDaemon(True)
print(t.isDaemon())
t.start()
t2.start()
print("exit main")

import cgitb
#sDaemon()=======================================================
import time, threading, os
def f1(arg1):
   
        
        print (threading.enumerate())
        
        time.sleep(2)

t = threading.Thread(name="MyThread1", target=f1, args=(6,))
t2 = threading.Thread(name="MyThread2", target=f1, args=(6,))


t.setDaemon(True)
print(t.isDaemon())
t.start()
t2.start()
print("exit main")
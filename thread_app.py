import threading
 
class NewThreadedTask(threading.Thread):
     def __init__(self):
         super(NewThreadedTask, self).__init__()
 
     def run(self):
        # run some code here
        print('Threaded task has been completed')
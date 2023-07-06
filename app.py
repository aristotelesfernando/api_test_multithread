from flask import Flask, jsonify
import threading

app = Flask(__name__)

class NewThreadedTask(threading.Thread):
     def __init__(self):
         super(NewThreadedTask, self).__init__()
 
     def run(self):
        my_list = [i for i in range(10000000)]
        total = sum(my_list)
        print(total)        
        print('Threaded task has been completed')

@app.route('/')
def index():
    new_thread = NewThreadedTask()
    new_thread.start()
    # opcionalmente, aguarda a thread terminar a execução para continuar
    # new_thread.join()    
    return jsonify({'name': 'alice','email': 'alice@outlook.com'}), 200

def processa_lista():
    my_list = [i for i in range(1000000)]
    total = sum(my_list)  
    print(total)  

# execute a app com o comando $ gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:ap
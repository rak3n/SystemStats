import psutil
from datetime import datetime
import time
import os
import elasticSearch

def get_processes_info(indexer):
    """
    Getting process info in the system, with details like CPU and Memory Usage in percent, along with extra details
    """

    processes = {
        'pid':'',
        'name': '', 
        'create_time': '',
        'cores': '', 
        'cpu_usage': '', 
        'status': '', 
        'priority': '',
        'memory_usage': '',
        'n_threads': '',
    }

    for process in psutil.process_iter():
        with process.oneshot():
            pid = process.pid
            if pid == 0:
                continue

            #Process Name
            name = process.name()
            if name == "":
                continue 

            #Precess creation time
            try:
                create_time = datetime.fromtimestamp(process.create_time())
            except OSError:
                create_time = datetime.fromtimestamp(psutil.boot_time())
            
            #number of cores.
            try:
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = -1

            #cpu usage in percent    
            cpu_usage = process.cpu_percent()
            #current status of system
            status = process.status()
            if status=="":
                continue
            #priority of the process
            try:
                nice = int(process.nice())
            except psutil.AccessDenied:
                nice = 0
            except:
                nice=0

            #Memory usage in percent    
            try:
                memory_usage = process.memory_percent()
            except psutil.AccessDenied:
                memory_usage = 0
            except:
                continue
            #number of threads
            n_threads = process.num_threads()
            
        processes['pid']=pid
        processes['name']=name
        processes['create_time']=create_time
        processes['cores']=cores
        processes['cpu_usage']=cpu_usage
        processes['status']=status
        processes['priority']=nice
        processes['memory_usage']=memory_usage  #percentage
        processes['n_threads']=n_threads

        #index the data in the elasticsearch, with pid as index id
        indexer.update_index(processes, pid)

    return processes

if __name__ == "__main__":
    live_update = True
    indexer = elasticSearch.Index() #creating an elastic search indexer object
    processes = get_processes_info(indexer)
    print("Indexing Started")
    while live_update:
        #continually repaeat to get the process info and index it
        processes = get_processes_info(indexer)
        time.sleep(0.7) #waiting for some n time. 
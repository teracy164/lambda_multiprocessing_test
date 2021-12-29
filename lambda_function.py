import time
import lambda_multiprocessing as mp

def lambda_handler(event, context):
    print('params', event)
    
    is_multiprocessing = event['multiprocess']
    start_time = time.time()
    print('start time: ', start_time)
    
    if event['multiprocess']:
        print('run multiprocess')
        events = []
        for num in range(10):
            events.append({'function': _calc, 'args': []})
            
        m = mp.Multiprocessing()
        m.run(events)
        
    else:
        print('run sequential')
        for num in range(10):
            _calc()
    
    end_time = time.time()
    print('end time: ', start_time)

    print('run time: ', end_time - start_time)
    return 'complete'

def _calc():
    print('calc start')
    for num in range(10000000):
        a = num
    print('calc end')

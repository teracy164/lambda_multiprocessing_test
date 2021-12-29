import os
import time
import multiprocessing as mp
import threading as th

class Multiprocessing:
    def __init__(self):
        self.queue = []
        # 使用可能なCPU数を並列実行可能上限とする
        # multiprocessing.cpu_count()だと使用可能なCPUではないため注意
        # 参考　https://docs.python.org/ja/3/library/multiprocessing.html#multiprocessing.cpu_count
        self.limit = len(os.sched_getaffinity(0))
        
    def run(self, events):
        print('available CPU: ', self.limit)
        threads = []
        for event in events:
            t = th.Thread(target=self._proc, args=(event,))
            t.start()
            threads.append(t)
            
        # 全スレッド終了を待つ
        for thread in threads:
            thread.join()
                
    def _proc(self, event):
        if len(self.queue) == self.limit:
            time.sleep(0.01)
            self._proc(event)
            return
        
        self.queue.append(event)
        p = mp.Process(target=event['function'], args=(event['args']))
        p.start()
        p.join()
        self.queue.remove(event)
        
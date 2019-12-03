# -*- coding:utf-8 -*-
import os
import shutil
import time
import signal
import traceback

def send_timeout_signal(seconds):
    check_path = 'check_timeout'
    current_pid = os.getpid()
    textname = str(current_pid) + '__' + str(seconds) + '.txt'
    textname = os.path.join(check_path,textname)
    with open(textname,'w') as f:
        pass
    return textname
    
def end_timeout_signal(textname,check_pre=False):
    try:
        if check_pre:
            if os.path.exists(textname):
                os.remove(textname)
        else:
            os.remove(textname)
    except:
        print('remove {} error'.format(os.path.basename(textname)))
        print(traceback.format_exc())

def get_cur_files(path):
    check_timeout_basenames = os.walk(path).__next__()[2]
    return check_timeout_basenames

def clear_dir(path):
    path = os.path.abspath(path)
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
    os.mkdir(path)

def monitor_task():
    check_path = 'check_timeout'
    clear_dir(check_path)
    while 1:
        check_timeout_basenames = get_cur_files(check_path)
        if len(check_timeout_basenames):
            time_start = time.time()
            infos = []
            for check_timeout_basename in check_timeout_basenames:
                info = os.path.splitext(check_timeout_basename)[0].split('__')
                info.append(check_timeout_basename)
                info[0] = int(info[0]) ; info[1] = int(info[1])
                infos.append(info) #[pid,timeout,...]
            infos.sort(key=lambda x:x[1])
            for info in infos:  #sort + for simulate multi-process --by rcx
                pid,timeout = info[:2]
                time_cur = time.time()
                time.sleep(max(timeout - (time_cur - time_start),0))
                cur_existed_basenames = get_cur_files(check_path)
                if info[2] in cur_existed_basenames:
                    os.kill(pid,signal.SIGINT)
                #    os.popen('taskkill.exe /F /pid:'+str(other_pid))
#                cur_existed_filename = os.path.join(check_path,info[2])
#                try:
#                    os.remove(cur_existed_filename)
#                except:
#                    print('remove {} error'.format(os.path.basename(cur_existed_filename)))
#                    print(traceback.format_exc())
                
#                restart(cmd_args)
                
                    
            time.sleep(0.1)
        else:
            time.sleep(0.1)
        
if __name__ == "__main__":
    monitor_task()
    


    
    
    
    
    
    
    
    
        
            



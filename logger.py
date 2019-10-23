#-*- coding:utf-8 -*-
'''
生成两种形式log文件：
   1. bug产生的文件
   2. 运行的文件
'''
import logging
class Logger():

    #正常处理使用的日志
    def logger_Info(self):
        # log初始化
        logger = logging.getLogger("webcrawer service")
        logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler('./log/run.log') 
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        #logger.info("Start print log")
        #logger.debug("Do something")
        #logger.warning("Something maybe fail.")
        #logger.info("Finish")  
        return logger
    
    #出现错误日志
    def logger_basicConfig(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./log/debug.log',
                        filemode='w')  
        return logging
    
        
if __name__ == "__main__" :
    logger = Logger()
    log = logger.logger_Info()
    log.info("Start print log")
   # logger.logger_basicConfig()
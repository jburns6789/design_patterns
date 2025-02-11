import logging
import threading

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance._initialize_logger()
            return cls._instance

    # Helper        
    def _initialize_logger(self):
        self.logger = logging.getLogger('joels_logger')
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('joels_log.log')
        file_handler.setLevel(logging.DEBUG)

    #create console handlers and set it to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

    #create formatter and add to handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

    # #add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


logger = SingletonLogger.get_instance().logger
print(logger.debug("DEBUG"))
print(logger.debug("Warning"))
logger.debug("Error")


#no princiapls applied
# #setup logger
# logger = logging.getLogger('joels_logger')
# logger.setLevel(logging.DEBUG)

# #create file handler
# file_handler = logging.FileHandler('joels_log.log')
#file_handler.setLevel(logging.DEBUG)

# #create console handlers and set it to info
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

# #create formatter and add to handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)

# #add the handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

# logger.debug('This is a debug message')
# logger.info('This is a infomessage')
# logger.warning('This is a warning message')
# logger.error('This is a error message')
# logger.critical('This i s a critical message')
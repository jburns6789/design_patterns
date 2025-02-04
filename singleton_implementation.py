import threading

#thread safety

class ThreadSafeSingleton:
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance
    

class Singleton(metaclass=ThreadSafeSingleton):
    pass

def get_singleton_instance():
    s = Singleton()
    print(s)

threads = [] #create 10 objects put them in a list
for i in range(0):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()


#eager loaded into memory first

class SingletonMeta(type):
    _instances = {}
    #override called during creation of subtypes
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()
        print('initializing <super>...')

    #override the __new__ mehod instantate the class at load time
    # def __new__(cls, *args, **kwargs):
        #print('initializing <super>... ')
        #new_class = super().__new__(cls, *args, **kwargs)
        #cls_instances[new_class] = super(SingletonMeta, new_class).__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print('initializing <child>...')
        self.attribute = "Im a singleton"


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1.attribute)
print(singleton2.attribute)

print(singleton1 is singleton2)


#Lazy loading

#Meta class
#base class, decorator, metaclass

class SingletonMeta(type):
    _instances = {}
    def __call__(cls):
        print('<call meta> calling..')
        if cls not in cls._instances:
            instance =  super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def business_logic(self):
        pass
        

#classic

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         print('<new> creating...')
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __init__(self):#override control initialization
#         print('<init> called...')
    

#s1 = Singleton()
#s2 = Singleton()
#print(s1 is s2)

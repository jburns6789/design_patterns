#base class
#decorator
#meataclass

#metaclass in python is a class that defines the behavior and rules for creating other classes
#classes of classes
#Python classes implicitly inherit from the type built-in class which is itself a metaclass
#metaclasses allow us to customize the class creation process and modify class attributes, methods
#or other properties before the class is actually created.

#metaclass class factory

#EAGER python implementation
# data prelaoding, connectivity pre-caching, frequnt access and needs to be fast
# initialize and laod the instance before we need it

class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
#class Singleton(metaclass=SingletonMeta):
#    def __init__(self);


#LAZY

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls.__instances[cls]
    
#class Singleton(metaclass=SingletonMeta):
#    def business logic(self):
    
#s1 = Singleton() lazy


#simple way to create singleton in python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls.instance = super().__new__(cls)
        return cls._instance
    
#s1 = Singleton()


#classic

class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance () instead')
    
    @classmethod
    def get_instance(cls):#lazy instantiation
        if not cls._instance:
            cls.__instance = cls.__new__(cls)
            #return single instance of the class
            #newly created or existing
            return cls.__instance

#s1 = ClassicSingleton.get_instance()
#lazy instantiation

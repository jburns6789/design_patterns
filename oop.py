from abc import ABC, abstractmethod

#abstract methods are buld prints in which to create classes and understand experected 
#behavior
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def description(self):
        print((f"{self.__class__.__name__} says: {self.sound()}"))

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    def description(self):
        print(f"My little dog says: {self.sound()}")#<---- can override the parent class if modified in the chidl class
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    

dog = Dog()
dog.description()

cat = Cat()
cat.description()



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def description(self):
#         print((f"{self.__class__.__name__} says: {self.sound()}"))

# class Dog(Animal):
#     def sound(self):
#         return "Woof!"
    
#     def description(self):
#         return super().description()
    
# class Cat(Animal):
#     def sound(self):
#         return "Meow!"
    
#     def description(self):
#         return super().description()
    
# dog = Dog()
# dog.description()

# cat = Cat()
# cat.description()
    
    
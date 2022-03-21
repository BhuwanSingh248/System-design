from abc import ABC, abstractmethod

class Creator(ABC):
    '''
    the creator class declaes the factory method that is supposed to return an
    object of a product class. the creator's subclassed usually provide the
    implementation of this method. 
    '''
    @abstractmethod
    def factory_method(self):
        pass


    def some_operation(self):
        product =self.factory_method()
        result = f' same creator code has just worked with {product.operation()}'
        return result

class ConcreteCreator1(Creator):
    
    def factory_method(self):
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):

    @abstractmethod
    def operation(self):
        pass 
    
class ConcreteProduct1(Product):
    def operation(self):
        return 'result of the concrete product 1'

class ConcreteProduct2(Product):
    def operation(self):
        return 'result of the concrete product 2'

def client_code(creator):
    print(f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print('app launched with the ConcreteCreator1')
    client_code(ConcreteCreator1())
    print('\n')

    print('app launched with the ConcreteCreator1')
    client_code(ConcreteCreator2())

    




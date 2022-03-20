# means class to depends on abstruction not a concrete sub-class

## currently the code interface_segregation classes are depends on SMSAuth class 
## which is voliation to dependency inversion


from abc import ABC, abstractmethod

class Order:
    items = []
    quantities =[]
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass

class SMSAuth(Authorizer):
    authorized = False
    def verify_code(self, code):
        print(f'verifying code {code}')
        self.authorized = True

    def is_authorized(self):
        return self.authorized

# lets say we wnat to add one more auth say its not a robot
class RobotVerification(Authorizer):
    authorized = False
    def not_a_robot(self):
        print('not a robot')
        self.authorized = True

    def is_authorized(self):
        return self.authorized

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass 


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code,  authorizer:Authorizer) -> None:
        self.security_code = security_code
        self.varified = authorizer

    def pay(self, order):    
        if not self.verified:
            raise Exception("not authorized")
        print('pricessing debit payment type')
        print(f'verifying security code:{self.security_code}')
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):   # does not support sms_authentication
    def __init__(self, security_code) -> None:
        self.security_code = security_code
        
    def pay(self, order):
        print('pricessing credit payment type')
        print(f'verifying security code:{self.security_code}')
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address,  authorizer:Authorizer) -> None:
        self.email_address = email_address    
        self.verified = authorizer

    def pay(self, order): 
        if not self.verified:
            raise Exception("not authorized")
        print('pricessing Paypal payment type')
        print(f'verifying email:{self.email_address}')
        order.status = "paid"         

if __name__ == "__main__":
    print("", end="\n \n \n")
    print("bill".center(40,"*"))
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)


    print(f"total : {order.total_price()}".center(40))
    autherizer = RobotVerification()
    processor = PaypalPaymentProcessor('abc@domain.com', autherizer)
    autherizer.not_a_robot()
    processor.pay(order)

    print("".center(40,"*"))
    print("", end="\n \n \n")




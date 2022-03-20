

## we wants to add 2-factor authentication with sms in the application


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

class PaymentProcessor(ABC):

    @abstractmethod
    def sms_auth(self,code):
        pass

    @abstractmethod
    def pay(self, order):
        pass 


class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code) -> None:
        self.security_code = security_code
        self.varified = False

    def pay(self, order):    
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

    def sms_auth(self, code):
        print("this method doesnot support sms authentication")   # --->> voilation of liskov substution

# Paypal uses email as a param not security code 
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address) -> None:
        self.email_address = email_address        
    def pay(self, order): 
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
    processor = PaypalPaymentProcessor('abc@domain.com')
    processor.pay(order)

    print("".center(40,"*"))
    print("", end="\n \n \n")


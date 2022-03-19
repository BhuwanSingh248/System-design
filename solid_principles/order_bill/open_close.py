# software entityes should be open for extension but closed for modification

#****************************************************
## let's take a assumption we wants to intigrate    *
## one more payment method as paypal                *
#****************************************************

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
    def pay(self, order, security_code):
        pass 

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
            print('pricessing debit payment type')
            print(f'verifying security code:{security_code}')
            order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
            print('pricessing credit payment type')
            print(f'verifying security code:{security_code}')
            order.status = "paid"


# adding paypal method without change in any existing class 
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
            print('pricessing Paypal payment type')
            print(f'verifying security code:{security_code}')
            order.status = "paid"         

if __name__ == "__main__":
    print("", end="\n \n \n")
    print("bill".center(40,"*"))
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)


    print(f"total : {order.total_price()}".center(40))
    processor = PaypalPaymentProcessor()
    processor.pay(order, "123456")

    print("".center(40,"*"))
    print("", end="\n \n \n")
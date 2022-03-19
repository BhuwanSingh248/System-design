# pay method contains two responsibility which should be avoided 


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
    
class PaymentProcessor:
    def pay_credit(self, order, security_code):
            print('pricessing debit payment type')
            print(f'verifying security code:{security_code}')
            order.status = "paid"

    def pay_debit(self, order, security_code):
            print('pricessing credit payment type')
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
    processor = PaymentProcessor()
    processor.pay_debit(order, "123456")

    print("".center(40,"*"))
    print("", end="\n \n \n")
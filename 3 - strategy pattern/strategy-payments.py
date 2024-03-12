"""
Goal is to write a payment processor that supports different payment types
credit
debit
COD
"""

from abc import ABC, abstractmethod
from enum import Enum


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order):
        print("Processing credit payment type")

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order):
        print("Processing debit payment type")

class CODPaymentProcessor(PaymentProcessor):
    def pay(self, order):
        print("Processing cod payment type")

class UPIPaymentProcessor(PaymentProcessor):
    def pay(self, order):
        print("Processing UPI payment type")

class PaymentType(Enum):
    CREDIT = CreditPaymentProcessor
    DEBIT = DebitPaymentProcessor
    COD = CODPaymentProcessor
    UPI = UPIPaymentProcessor

class Order:
    def __init__(self, total):
        self.total = total
    
    def proceed_with_payment(self, payment_processor):
        payment_processor.pay(self.total)

if __name__ == "__main__":
    order = Order(100)

    # select payment method
    # paymentMethod = PaymentType.CREDIT
    paymentMethod = PaymentType.UPI

    # process payment
    order.proceed_with_payment(paymentMethod.value())

import random
#from premium import Premium_Client
kid_bonus = 250
interest = 1.05

class Client:

    def __init__(self, name, balance, number_kids):
      self.name = name
      self.balance = balance
      self.account_number()
      self.number_kids = number_kids
      self.email = f"{name}@gmail.com"


    def account_number(self):
        self.account= f"ABN{random.randint(1000000000, 9999999999)}"
        #print(f'ABN{account}')

    def add_amount(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


    def transfer(self, receiver, amount):
        self.balance -= amount
        receiver.balance += amount

    def bonus_kids(self):
        self.balance += self.number_kids*kid_bonus

    def interest_payment(self):
        self.balance = self.balance*interest

    # def send_money(self, sender_account_number, receiver_account_number, amount):
    #     if self.balance < amount:
    #         return 'balance is not enough'
    #     else:
    #         client_list = [obj for obj in globals().values() if isinstance(obj, Client)]
    #         for sender_client in client_list:
    #             if sender_client.account_number == sender_account_number:
    #                 sender_client -= amount
    #
    #         for receiver_client in client_list:
    #             if receiver_client.account_number == receiver_account_number:
    #
    #                 receiver_client.balance += amount
    #
    #                 print(f"{amount} is transfer to the {receiver_client.name} from {sender_client.name}")

    # def send_money(self, receiver_account_number, amount):
    #     if self.balance < amount:
    #         return 'balance is not enough'
    #     else:
    #         client_list = [obj for obj in globals().values() if isinstance(obj, Client)]
    #         for receiver_client in client_list:
    #             if receiver_client.account_number == receiver_account_number:
    #                 receiver_client.balance += amount
    #                 self.balance -= amount
    #                 print(f"{amount} is transfer to the {receiver_client.name} from {self.name}")

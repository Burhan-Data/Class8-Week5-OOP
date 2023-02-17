from client import Client
from premium import Premium_Client
#from transaction import Transaction
client1=Client('ali', 1500, 3)
client2=Client('veli', 1800,2 )
client3=Client('hasan', 2000,0 )
p_client1=Premium_Client(name='mehmet', balance=5000, loyalty_point=0, number_kids=1)

client_list = [obj for obj in globals().values() if isinstance(obj, Client)]

total_balance = 0
count=0

#Adding child bonus to the client
# for i in client_list:
#     i.bonus_kids()
#     print(i.balance)

#Addiing Interest income to the client
# for i in client_list:
#     #print(i.balance)
#     i.interest_payment()
#     print(i.balance)

#CALCULATING TOTAL BALANCE AND AVARAGE BALANCE

# for i in client_list:
#     count= count+1
#     total_balance+=i.balance
#     avarage_balance = total_balance/count
# print(total_balance)
# print(avarage_balance)

# for i in client_list:
#     print(i.name)
# print(p_client1.loyalty_point)
#VIP Customers: Bonus point and Bonus Payment

p_client1.add_amount(10000)
# print(p_client1.balance)
# print(p_client1.loyalty_point)

for i in client_list:
    print(f"{i.name} has {i.balance} dollars")
    #print(f"{i.name} has {i.loyalty_point} dollars")
    #print(i.loyalty_point)

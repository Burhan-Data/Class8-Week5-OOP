from client import Client
class Premium_Client(Client):
    def __init__(self,name, balance, number_kids, loyalty_point):
        super().__init__(name, balance, number_kids)
        self.loyalty_point= loyalty_point
        # self.gold_pclient = gold_pclient
        # self.silver_pclient = silver_pclient
        # self.bronz_pclient = bronz_pclient

    def add_amount(self, amount):
        super().add_amount(amount)
        self.loyalty_point = amount*0.10

        if self.loyalty_point > 1500:
            credit_gold = amount*0.03
            self.add_amount(credit_gold)
        if self.loyalty_point > 1000:
            credit_silver = amount*0.02
            self.add_amount(credit_silver)
        if self.loyalty_point > 500:
            credit_bronz = amount * 0.01
            self.add_amount(credit_bronz)
    # def vip_client(self, loyalty_point):
    #     if self.loyalty_point > 1500:
    #         self.pclient == self. gold_pclient
    #     if self.loyalty_point > 1000:
    #         self.pclient == self. silver_pclient
    #     if self.loyalty_point > 1500:
    #         self.pclient == self. gold_pclient

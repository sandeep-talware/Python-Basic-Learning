class Banking:

    def __init__(self, name, card_no, age, balance):
        self.name=name
        self.card_no=card_no
        self.age=age
        self.balance= balance

    def withdrowamounr(self,amounttowithdraw):
        if(self.balance>amounttowithdraw):
            self.balance-=amounttowithdraw


class DebitCard(Banking):

    type="DebitCard_Type"
    def __init__(self, name, card_no, age, balance, debitnumber):
        super().__init__(self,name,card_no,age,balance)
        self.debitnumber=debitnumber


class Creditcard(Banking):

    type="Creditcard"
    def __init__(self,name, card_no, age, balance,creditnumber):
        super().__init__(self,name,card_no,age,balance)
        self.creditnumber=creditnumber



b = Banking("xyv","NHKI",682912,142639)
b.withdrowamounr(243)
print(b.balance)
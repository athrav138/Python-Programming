class Account:
  def __init__(self,account_no,balance):
    self.account_no = account_no
    self.balance = balance

  def debit(self,amount_debited):
    self.balance = self.balance - amount_debited
    self.display()
    print("after denitation")
  
  def credit(self,amount_credited):
    self.balance = self.balance + amount_credited
    self.display()
    print("after credition")

  def display(self):
    print(f"The account {self.account_no} has balance {self.balance} Rs.")

a1 = Account('A1ALKDSLK1',120000.23)
a1.display()
a1.credit(1200)
a1.debit(300)

    
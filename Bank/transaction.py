# Transaction class

# # This class will hold transaction information

# # members
# balance
# account_number_from
# account_number_to
# transaction_id

# # functions
# view_transaction()

# get_account_number_from()
# get_account_number_to()
# get_balance()
# get_transaction_id()

# set_account_number_from()
# set_account_number_to()
# set_balance()
# set_transaction_id()

class transaction:
  def __init__(self,balance,account_number_from,account_number_to,transaction_id):
    self.balance = balance,
    self.account_number_to = account_number_to,
    self.account_number_from = account_number_from,
    self.transaction_id = transaction_id
  def get_balance(self):
    return self.balance
  def get_account_number_from(self):
    return account_number_from
  def get_account_number_to(self):
    return account_number_to
  
  
    

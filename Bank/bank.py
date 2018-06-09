import json

# This class will hold accounts
class Bank:
    def __init__(self, filename):   
        self.accounts = []
        self.filename = filename
        self.load_accounts(self.filename)
        
    # load accounts into the bank
    def load_accounts(self,filename):
        # open file object
        file = open(filename,"r")
        # load json list into data
        self.accounts = json.load(file)
        # close the file
        file.close() 
    
    # add account to the bank
    def add_account(self):
        # print(self.accounts[0]['id'])
        # print(self.accounts[0]['first_name'])
        # print(self.accounts[0]['last_name'])
        # print(self.accounts[0]['email'])
        # print(self.accounts[0]['debit'])
        # print(self.accounts[0]['debit_balance'])
        # print(self.accounts[0]['credit'])
        # print(self.accounts[0]['credit_balance'])
        # print(self.accounts[0]['bank'])
        # print(self.accounts[0]['opened'])

bank = Bank("accounts.json")
bank.add_account()
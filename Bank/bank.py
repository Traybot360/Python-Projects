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
        
    # find a next account id    
    def find_next_id(self):
        # starting point
        self.next_id = 0
        # for each of the accounts
        for account in range(len(self.accounts)):
            # check if the account has the greatest id
            if self.next_id < accounts[account]['id']:
                # if it does then assign next_id a new value
                self.next_id = accounts[account]['id']
        # once the greatest id was found add 1 to it to make a new account
        self.next_id += 1

        return self.next_id


bank = Bank("accounts.json")
bank.add_account()
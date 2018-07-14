import json
from colorama import Fore, Style

__version__ = '1.0.1'
__author__ = 'Oleksii Polovyi'

class Bank:
    """This class holds and operates accounts from the given file.
    File must contain JSON list of account objects.
    """

    def __init__(self, filename):   
        """Constructor for Bank class. 
        This function is called upon object instantiation. It 
        initializes accounts as empty list. Also, it and saves 
        filename passed as an argument.
        Parameters
        ----------
        filename : str
            Filename that contains JSON list of accounts.
    	"""
        self.accounts = []
        self.filename = filename
    
    def load_accounts(self):
        """Load accounts into Bank.

        This function opens the file in the read mode.
        Then loads accounts from the filename
        and stores them into list of accounts.
        Upon completed action it closes the file.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        file = open(self.filename,"r")
        self.accounts = json.load(file)
        file.close() 

    def view_accounts(self):
        """View all Bank accounts.

        This function displays all of the accounts.
        It is using for loop together with view_account(account).

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for account in self.accounts:
            self.view_account(account)

    def search_by_id(self, account_id):
        """Search Bank account by id.This function
        searches for account using it's id. It returns 
        list of matching accounts (empty list in case none are found).
        Parameters
        ----------
        id : str
            Id of the account

        Returns
        -------
        match
            List of accounts that match
        """
        match = []
        for i in range(len(self.accounts)):
            if account_id == self.accounts[i]['id']:
                match.append(self.accounts[i])
        return match
    
    def search_by_first_name(self, first_name):
        """Search Bank accounts by first name of holder.This function
        searches for holder's accounts. It returns list of matching 
        accounts (empty list in case none are found).
        Parameters
        ----------
        first_name : str
            First name of the account holder

        Returns
        -------
        match
            List of accounts that match
        """
        match = []
        for i in range(len(self.accounts)):
            if first_name in self.accounts[i]['first_name']:
                match.append(self.accounts[i])
        return match
    
    def search_by_last_name(self, last_name):
        """Search Bank accounts by last name of holder. This function
        searches for holder's accounts. It returns list of matching 
        accounts (empty list in case none are found).
        Parameters
        ----------
        last_name : str
            Last name of the account holder
        Returns
        -------
        match
            List of accounts that match
        """
        match = []
        for i in range(len(self.accounts)):
            if last_name in self.accounts[i]['last_name']:
                match.append(self.accounts[i])
        return match

    def search_by_email(self, email):
        """Search Bank accounts by email of holder. This function
        searches for holder's accounts. It returns list of matching 
        accounts (empty list in case none are found).
        Parameters
        ----------
        email : str
            Email of the account holder
        Returns
        -------
        match
            List of accounts that match
        """
        match = []
        for i in range(len(self.accounts)):
            if email == self.accounts[i]['email']:
                match.append(self.accounts[i])
        return match

    def search_by_account_number(self, number):
        """Search Bank accounts by account number. This function
        searches for holder's accounts. It returns list of 
        matching accounts (empty list in case none are found).
        Parameters
        ----------
        number : str
            Account number 
        Returns
        -------
        match : 
            List of accounts that match
        """
        match = []
        for i in range(len(self.accounts)):
            if number == self.accounts[i]['debit']:
                match.append(self.accounts[i])
            elif number == self.accounts[i]['credit']:
                match.append(self.accounts[i])
        return match

    def search_by_balance(self, balance):
        """Search Bank accounts by account balance. This function
        searches for holder's accounts. It returns list of matching 
        accounts (empty list in case none are found).
        Parameters
        ----------
        balance : str
            Account balance
        Returns
        -------
        match
            List of accounts that match
        """
        balance = "$" + balance
        match = []
        for i in range(len(self.accounts)):
            if balance == self.accounts[i]['debit_balance']:
                match.append(self.accounts[i])
            elif balance == self.accounts[i]['credit_balance']:
                match.append(self.accounts[i])
        return match
        
    def add_account(self):
        """Add Bank account. This function opens account file in the 
        write mode, appends account to the Bank accounts, and
        then writes all of accounts in JSON format and closes the file.
        Parameters
        ----------
        None
        Returns
        -------
        None
		"""

        file = open(self.filename,"w")
        account = Account(self.find_next_id())
        self.accounts.append(account)
        file.write(json.dumps(self.accounts, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close() 
    
    def update_account(self, account):
        """Update Bank account. This function opens account file in the
        write mode, updates Bank account, and writes all of accounts 
        in JSON format and closes the file.
        Parameters
        ----------
        account : Account
            Account to update
        Returns
        -------
        None
		"""
        file = open(self.filename,"w")
        for i in range(len(self.accounts)):
            if account['id'] == self.accounts[i]['id']:
                self.accounts[i].update_account(account)

        file.write(json.dumps(self.accounts))
        file.close()

    def remove_account(self, account):
        """Remove Bank account. This function opens account file in the
        write mode, removes Bank account, and writes all of accounts 
        in JSON format and closes the file.
        Parameters
        ----------
        account : Account
            Account to remove
        Returns
        -------
        None
		"""
        file = open(self.filename, "w")
        for i in range(len(self.accounts)):
            if account['id'] == self.accounts[i]['id']:
                self.accounts.pop(i)
        
        file.write(json.dumps(self.accounts))
        file.close()

    def view_account(self, account):
        """View Bank account. This function displays information
        about specific account in the table format.
    
        Parameters
        ----------
        account : Account
            Account to view
        Returns
        -------
        None
		"""
        print("--------------------------------------------------------")
        print("| Account #      | " + Fore.RED 
            + '{:>35}'.format(str(account['id'])) 
            + Style.RESET_ALL + " |")
        print("--------------------------------------------------------")    
        print("| First name     | " 
            + '{:>35}'.format(str(account['first_name'])) + " |")
        print("--------------------------------------------------------")
        print("| Last name      | "     
            + '{:>35}'.format(str(account['last_name'])) + " |")
        print("--------------------------------------------------------")
        print("| Email          | "   + Fore.MAGENTA
            + '{:>35}'.format(str(account['email']))
            + Style.RESET_ALL + " |")
        print("--------------------------------------------------------")
        print("| Debit #        | " 
            + '{:>35}'.format(str(account['debit'])) + " |")
        print("--------------------------------------------------------")
        print("| Debit balance  | " + Fore.GREEN 
            + '{:>35}'.format(str(account['debit_balance'])) 
            + Style.RESET_ALL + " |")
        print("--------------------------------------------------------")
        print("| Credit #       | " 
            + '{:>35}'.format(str(account['credit'])) + " |")
        print("--------------------------------------------------------")
        print("| Credit balance | " + Fore.GREEN
            + '{:>35}'.format(str(account['credit_balance']))
            + Style.RESET_ALL + " |")
        print("--------------------------------------------------------")
        print("| Opened         | " 
            + '{:>35}'.format(str(account['opened'])) + " |")
        print("--------------------------------------------------------")

        print("")

    def find_next_id(self):
        """Find next Account id. This funciton looks for the highest
        id between accounts. Returns highest + 1
        
        Parameters
        ----------
        None
        Returns
        -------
        next_id
            Next account id
        """
        self.next_id = 0
        for account in range(len(self.accounts)):
            if self.next_id < self.accounts[account]['id']:
                self.next_id = self.accounts[account]['id']
        self.next_id += 1

        return self.next_id

if __name__ == '__main__':
    bank = Bank("accounts.json")
    
    # load file
    bank.load_accounts()
    
    # # view all 1000 accounts at the begining
    # bank.view_accounts()


    accounts = bank.search_by_first_name("Margaret")
    for account in accounts:
        bank.view_account(account)

    
    # accounts = bank.search_by_last_name("Batte")
    # for account in accounts:
    #     bank.view_account(account)


    # accounts = bank.search_by_email("smontelrn@weather.com")
    # for account in accounts:
    #     bank.view_account(account)


    # # Debit #   
    # accounts = bank.search_by_account_number("5242292355358052")
    # for account in accounts:
    #     bank.view_account(account)


    # # Credit #
    # accounts = bank.search_by_account_number("3570764222510716")
    # for account in accounts:
    #     bank.view_account(account)

    # # debit balance
    # accounts = bank.search_by_balance("3733.35")
    # for account in accounts:
    #     bank.view_account(account)

    # # credit balance
    # accounts = bank.search_by_balance("-1816.61")
    # for account in accounts:
    #     bank.view_account(account)    
    
    # # add account
    # bank.add_account()
    # bank.search_by_id(1001)
    
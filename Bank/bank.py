import json

__version__ = '1.0.0'
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
        Then loads accounts from the ```filename```
        and stores them into list of ```accounts```.
        Upon completed action it closes the file.
        """
        file = open(self.filename,"r")
        self.accounts = json.load(file)
        file.close() 

    def view_accounts(self):
        """View all Bank accounts.

        This function displays all of the ```accounts```.
        It is using for loop together with ```view_account(account)```.
        """
        for account in self.accounts:
            self.view_account(account)

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
        for account in self.accounts:
            if first_name == self.accounts['first_name']:
                match.append(account)
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
        for account in self.accounts:
            if last_name == self.accounts['last_name']:
                match.append(account)
        return match

    def search_by_account_number(self, number):
        """Search Bank accounts by account number. This function
        searches for holder's accounts. It returns list of 
        matching accounts (empty list in case none are found).
        Parameters
        ----------
        number : int
            Account number 
        Returns
        -------
        match : 
            List of accounts that match
        """
        match = []
        for account in self.accounts:
            if number == self.accounts['debit']:
                match.append(account)
            elif number == self.accounts['credit']:
                match.append(account)
        return match

    def search_by_balance(self, balance):
        """Search Bank accounts by account balance. This function
        searches for holder's accounts. It returns list of matching 
        accounts (empty list in case none are found).
        Parameters
        ----------
        balance : float
            Account balance
        Returns
        -------
        match
            List of accounts that match
        """
        match = []
        for account in self.accounts:
            if balance == self.accounts['debit_balance']:
                match.append(account)
            elif balance == self.accounts['credit_balance']:
                match.append(account)
        return match
        
	def add_account(self, account):
        """Add Bank account. This function opens account file in the 
        write mode, appends account to the Bank ```accounts```, and
        then writes all of accounts in JSON format and closes the file.
        Parameters
        ----------
        account : Account
            Account to add
		"""
        file = open(self.filename,"w")
        account['id'] = find_next_id()
        self.accounts.append(account)
        file.write(json.dumps(self.accounts))
        file.close() 
    
    def update_account(self, account):
		"""Update Bank account. This function opens account file in the
        write mode, updates Bank account, and writes all of accounts 
        in JSON format and closes the file.
        Parameters
        ----------
        account : Account
            Account to update
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
		"""
        file = open(self.filename, "w")
        for i in range(len(self.accounts)):
            if account['id'] == self.accounts[i]['id']:
                self.accounts.pop(i)
        
        file.write(json.dumps(self.accounts))
        file.close()

    def view_account(self, account):
        """View Bank account. This function displays information
        about specific account in the following format:
        ***********************************************
        * Account #      *                          1 *
        * First name     *                   Waverley *
        * Last name      *                    Blankau *
        * Email          *        wblankau0@google.ca *
        * Debit #        *        6331100508468193564 *
        * Debit balance  *                   $3029.86 *
        * Credit #       *           5010124139863265 *
        * Credit balance *                  $-1002.65 *
        * Opened         *              June 19, 2002 *
        ***********************************************

        Parameters
        ----------
        account : Account
            Account to view
		"""
        print("***********************************************")
        print("* Account #      * " + account['id'] + " *")
        print("* First name     * " + account['first_name'] + " *")
        print("* Last name      * " + account['last_name'] + " *")
        print("* Email          * " + account['email'] + " *")
        print("* Debit #        * " + account['debit'] + " *")
        print("* Debit balance  * " + account['debit_balance'] + " *")
        print("* Credit #       * " + account['credit'] + " *")
        print("* Credit balance * " + account['credit_balance'] + " *")
        print("* Opened         * " + account['opened'] + " *")
        print("***********************************************")

    def find_next_id(self):
        """Find next Account id. This funciton looks for the highest
        id between accounts. Returns highest + 1
        Returns
        -------
        next_id
            Next account id
        """
        self.next_id = 0
        for account in range(len(self.accounts)):
            if self.next_id < accounts[account]['id']:
                self.next_id = accounts[account]['id']
        self.next_id += 1

        return self.next_id

if __name__ == '__main__':
    main()
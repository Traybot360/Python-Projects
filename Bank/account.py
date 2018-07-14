# Account class

# # This class will hold account information

# # members
# balance
# account_number
# user
# pin
# transactions[]

# update_account()
# # functions
# view_transactions()
# view_account()
# equals()
# deposit()
# withdraw()

# get_account_number()
# get_balance()
# get_pin()
# get_user()

# set_account_number()
# set_balance()
# set_pin()
# set_user()


# Accounts type:
# CHEKING
# SAVINGS
# GIC
# JOINT
# CREDIT

# consolidation (multiple cards statements into 1)

class Account:
    def __init__(self, account_id):
        pass
    def view_account(self):
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
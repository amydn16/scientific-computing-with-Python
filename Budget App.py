class Category(object):

    # Define attributes of each object
    # Has a description as a string
    # Has a ledger as a list
    # Has a balance as a float
    def __init__(self, category = '', ledger = [], balance = 0.0):
        self.category = category
        self.ledger = ledger
        self.balance = balance

    # Define method to get current balance
    def get_balance(self):
        return self.balance

    # Define method to check available funds, which takes amount
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        elif self.get_balance() >= amount:
            return True   

    # Define deposit method, which takes amount and description
    def deposit(self, *arg):
        amount = arg[0] # Amount is 1st argument
        if len(arg) == 2: # Description is supplied as 2nd argument
            description = arg[1]
        elif len(arg) == 1: # No description given
            description = ''
        self.balance = self.get_balance() + amount
        self.ledger = self.ledger + [{"amount": amount, "description": description}]

    # Define withdraw method, which takes amount and checks funds
    def withdraw(self, *arg):
        amount = arg[0] # Amount is 1st argument
        if len(arg) == 2: # Description is supplied as 2nd argument
            description = arg[1]
        elif len(arg) == 1: # No description given
            description = ''
        # Sufficient funds    
        if self.check_funds(amount) == True:
            self.balance = self.get_balance() - amount
            self.ledger = self.ledger + [{"amount": -1*amount, "description": description}]
            return True
        # Insufficient funds
        if self.check_funds(amount) == False: # Withdrawal does not take place
            return False

    # Define transfer mthod, which transfers funds from self to newself
    def transfer(self, amount, newself):
        description_self = "Transfer to " + newself.category
        description_newself = "Transfer from " + self.category
        # Sufficient funds
        if self.withdraw(amount, description_self) == True:
            newself.deposit(amount, description_newself)
            return True
        # Insufficient funds
        elif self.withdraw(amount, description_self) == False:
            return False

    # Define output of budget
    def __repr__(self):
        newline = ''
        if (len(self.category) % 2 == 0):
            no_stars = int((30 - len(self.category)) / 2)
            line1 = no_stars * '*' + self.category + no_stars * '*' + '\n'
        else:
            no_stars = int((30 - len(self.category) - 1) / 2)
            line1 = no_stars * '*' + self.category + no_stars * '*' + '\n'                                   
        for item in self.ledger:
            amt = "{:.2f}".format(item["amount"])
            desc = item["description"]
            if len(desc) >= 23:
                newline = newline + desc[0:23] + (7 - len(amt)) * ' ' + amt + '\n'
            elif len(desc) < 23:
                newline = newline + desc + (30 - len(desc) - len(amt)) * ' ' + amt + '\n'
        newline = line1 + newline + "Total: " + str(self.get_balance())
        return newline
    
def create_spend_chart(categories):

    # First line in string output
    line1 = "Percentage spent by category\n"

    spent_list = [] # List to hold all spending
    total = 0.0 # Total amount of money spent

    # Go through ledger of each category to calculate amount of money spent
    for cat in categories:
        spent = 0.0 # Amount of money spent for each category
        for item in cat.ledger: # Look at withdrawals only
            if (item["amount"] < 0) and ("Transfer" not in item["description"]):
                spent = spent + -1*item["amount"]
        total = total + spent
        spent_list = spent_list + [[cat.category, spent]]

    # Calculate percentage spent in each category
    for i in range(0, len(spent_list)):
        percentage = (spent_list[i][1] / total) * 100
        percentage = (percentage // 10) * 10
        spent_list[i] = spent_list[i] + [percentage]

    # Find category with longest name
    max_len = 0
    for item in spent_list:
        if len(item[0]) >= max_len:
            max_len = len(item[0])

    # Form bar chart first
    newline = ''
    for i in range(0,11): # Start at top most line
    # Fill in percentages
        per_no = (10 - i) * 10 # Percentage as integer
        per_str = str(per_no) # Percentage as string
        newline = (3 - len(per_str)) * ' ' + per_str + '| '

        for item in spent_list:
            if per_no <= item[2]: # Percentage spent in category matches
                newline = newline + 'o' + 2 * ' ' # Add o
            else:
                newline = newline + 3 * ' ' # Leave blank
        newline = newline + '\n' # 2 blank spaces at end
        line1 = line1 + newline

    # Fill in dashed line underneath chart
    line1 = line1 + 4 * ' ' + ((3*len(categories)) + 1) * '-' + '\n'

    # Form lines for categories
    newline = ''
    for i in range(0, max_len):
        newline = newline + 5 * ' '
        for item in spent_list:
            if i < len(item[0]): # Spell out names of the categories
                newline = newline + item[0][i] + 2 * ' '
            else: # Name has already been spelled out
                newline = newline + 3 * ' '
        if i < (max_len - 1):
          newline = newline + '\n'

    # Add to bar chart
    line1 = line1 + newline

    return(line1)

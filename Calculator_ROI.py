class ROI_calc():
#set methods/parameters?
    def __init__(self): 
        self.Income = []
        self.Expenses = []
        self.Investment = []
        self.Cashflow = []

#define/find income
    
    def Income(self):
        self.Income = []
        addIncome = int(input('Monthly Rental Income')) * 12
        self.Income.append(addIncome)
        addIncome1 = int(input('Monthly Parking ($0 if none)'))  * 12
        self.Income.append(addIncome1)
        addIncome2 = int(input('Laundry Room ($0 if none)'))  * 12
        self.Income.append(addIncome2)
        addIncome3 = int(input('Vending Machine ($0 if none)'))  * 12
        self.Income.append(addIncome3)
        print(f'Your total annual income is ${self.EarnedIncome}')

#define/find expenses

    def Expenses(self):
        self.Expenses = []
        addExpense1 = int(input('How much is your monthly mortgage payment?'))  * 12
        self.Expenses.append(addExpense1)
        addExpense2 = int(input('How much is your monthly home owner insurance payment?'))  * 12
        self.Expenses.append(addExpense2)
        addExpense3 = int(input('How much is your electric bill?'))  * 12
        self.Expenses.append(addExpense3)
        addExpense4 = int(input('How much do you pay for gas/heating?'))  * 12 
        self.Expenses.append(addExpense4)
        addExpense5 = int(input('How much is your water/sewage bill?'))  * 12
        self.Expenses.append(addExpense5)
        addExpense6 = int(input('If you have them, how much do you pay for HOA fees?'))  * 12
        self.Expenses.append(addExpense6)
        addExpense7 = int(input('What are your estimated home repair/maintenance fees?'))  * 12
        self.Expenses.append(addExpense7)
        addExpense8 = input("to calculate your property tax payments, please enter your territory abbreviation (ex:MA, NY, IL)  ") 
        states = {'hi':0.0028, 'al':0.0041, 'co':0.0051, 'la':0.0055, 'dc':0.0056, 'sc':0.0057, 'de':0.0057, 'wv':0.0058, 'nv':0.006, 'wy':0.0061, 
                'ar':0.0062, 'ut':0.0063, 'az':0.0066, 'id':0.0069, 'tn':0.0071, 'ca':0.0076, 'nm':0.008, 'ms':0.0081, 'va':0.0082, 'mt':0.0084, 'nc':0.0084,
                'in':0.0085, 'ky':0.0086, 'fl':0.0089, 'ok':0.009, 'ga':0.0092, 'mo':0.0097, 'or':0.0097, 'nd':0.0098, 'wa':0.0098, 'md':0.0109, 'mn':0.0112,
                'ak':0.0119, 'ma':0.0123, 'sd':0.0131, 'me':0.0136, 'ks':0.0141, 'mi':0.0154, 'oh':0.0156, 'ia':0.0157, 'pa':0.0158, 'ri':0.0163, 'ny':0.0172,
                'ne':0.0173, 'tx':0.0180, 'wi':0.0185, 'vt':0.0190, 'ct':0.0214, 'nh':0.0218, 'il':0.0227, 'nj':0.0249}
        costofproperty= int(input('\nWhat is the cost of the property? '))
        self.Expenses.append((states[addExpense8.lower()]) * costofproperty) * 12
        print(f'Your total expenses amount to ${self.Expenses}')

#determine amounts invested

    def Investment(self):
        self.Investment = []
        addInvestment1 = int(input('How much are you paying for your down payment?'))
        self.Investment.append(addInvestment1)
        addInvestment2 = int(input('What is your total Closing cost?'))
        self.Investment.append(addInvestment2)
        print(f'Your total investment is ${self.Investment}')

#cashflow (how much comes in and out)
    def Cashflow(self):
        annual= sum(self.Income) - sum(self.Expenses)
        monthlycashflow = (self.Income) - (self.Expenses)
        print(f'Your total monthly cashflow is ${monthlycashflow}')
        print(f'Your total annual cashflow is ${annual}')

        
    def calculator(self):
        annual= sum(self.Income) - sum(self.Expenses)
        findreturn = float((annual * 12) / sum(self.Investment)) * 100
        print('Your return on investment is{findreturn}%')
        

#call function  
class Main():
    def __init__(self):
        self.ROI = ROI_calc()
    def instructions(self):
        print("Bienvenudo!")
    print(f"""
    In order to calculate the ROI of your rental property, please enter your monthly income, expenses, and the total amount invested into your property:
    """)

def run(self):
    self.instructions
    while True:
        user_input = int(input(f"""
    What would you like to do?
    Enter "1" to add monthly income amounts 
    "2" to add monthly expenses 
    "3" to add the total invested in the property 
    "4" to view your cashflow 
    "5" to view your final ROI: 
    or "Quit" to exit """))
        if user_input == '1':
            self.ROI.Income()
        elif user_input== '2':
            self.ROI.Expenses()
        elif user_input == '3':
            self.ROI.Investment()
        elif user_input == '4':
            self.ROICashflow()
        elif user_input == 'calculate roi':
            self.ROI.calculator()
            break
        elif user_input == 'quit':
            print('Sayonara!')
        breakpoint

ROI_final = Main()
ROI_final.run()

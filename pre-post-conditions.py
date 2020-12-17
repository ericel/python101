# Currency converter from USD to BITCOINS
def convert_Usd_bitcoin(amount):
    # amount must be an integer and it must be greater than zero.
    if not isinstance(amount, int) or amount <= 0: #Our pre condition check..
        print('0 USD is equal to 0.0 Bitcoins') # Our pre condition print statement
        return amount
    else:
        rate = 0.00013 # Assumed rate
        bitcoin = amount * rate # Our post condition check
         # Our post condition print statement..
        print(str(amount) + ' USD is equal to ' + str(bitcoin) + ' bitcoins')
        return bitcoin
    
# Prints a statement of our conversion.
convert_Usd_bitcoin(40)




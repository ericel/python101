# Currency converter from USD to BITCOINS
def convert_Usd_bitcoin(amount):
    if amount <= 0: # Our pre condition check
        print('0 USD is equal to 0.0 Bitcoins') 
        return amount
    else:
        rate = 0.00013 # Assumed rate
        bitcoin = amount * rate # Our post condition check
        print(str(amount) + ' USD is equal to ' + str(bitcoin) + ' bitcoins')
        return bitcoin
    
# Prints a statement of our conversion.
convert_Usd_bitcoin('forty')


#not isinstance(amount, int) or 

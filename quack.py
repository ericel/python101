
# get the middle 2 characters of social security numbers
# in an array
s_n_numbers = ['738-38-4838', '638-28-3838', '538-18-2838',
               '438-08-1838', '338-48-0838']
def getMid2_digits_ssn():
    for snn in s_n_numbers:
        snn = snn[4:-5]
        print(snn)
        
getMid2_digits_ssn()



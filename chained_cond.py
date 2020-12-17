# Variable to hold student continent
studentContinent = 'America'
studentSubContinent = 'South America'

if(studentContinent == 'Africa'):
    print('You get Cookies and Cream flavor')
elif(studentContinent == 'Asia'):
    print('You get Cookies and Cream flavor')
elif(studentContinent == 'Europe'):
    print('You get Chocolate Ice Cream flavor')
elif(studentContinent == 'America' and studentSubContinent == 'North America'):
    print('You get  Vanilla Ice Cream flavor')
elif(studentContinent == 'America' and studentSubContinent == 'South America'):
    print('You get  Peanut Butter Cup flavor')
elif(studentContinent == 'Australasia'):
    print('You get  Chocolate Chip flavor')
else:
    print('We are still working on finding a continent for you!')

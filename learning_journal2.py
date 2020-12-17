
import math
# Calculate & Print volume of a sphere
def print_volume(r):
    # volume of a sphere = 4/3Cr3
    # π = pi
    pi = math.pi
    volume = 4/3 * pi * r**3
    print (volume)
    
# Printing with first value r = 2
print_volume(2)
#33.510321638291124

# Printing with first value r = 3
print_volume(3)
#113.09733552923254

# Printing with first value r = 4
print_volume(4)
#268.082573106329

# Invented Function: Calculate how much time a week on uopeople course work
def uopeople_week(number_days, hours_studying_a_day, est_hours_per_assignment, unit):
    # Number of days a week for study
    days = number_days
    # Hours spent reading(studying) a day
    hours_studying = hours_studying_a_day * days
    # Estimated number of assigments a week
    course_assignments = 4
    # Hours time spent per assignment
    time_per_assignment = est_hours_per_assignment
    # Total week hours
    week_hours =  hours_studying + (course_assignments * time_per_assignment)
    
    # 60 minutes = 1 hour
    # 60 seconds = 1 minute
    # Let's print uopeople_week depending on input unit
    if('hour' in unit):
        # concatenation: to print out a sentence, we contert measurement to string
        print('You spend ' + str(week_hours) + ' hours a week on UoPeople work')
    elif ('minute' in unit):
        print('You spend ' + str(week_hours * 60) + ' minutes a week on UoPeople work')
    elif ('second' in unit):
        print('You spend ' + str((week_hours * 60) * 60)  + ' seconds a week on UoPeople work')
    else:
        print('Input error!')
        
    

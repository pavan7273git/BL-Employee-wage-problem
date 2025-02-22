import random

def calculate_daily_wage(hours_worked, hour_rate):
    return hours_worked * hour_rate

def check_attendance(hour_rate):
    attendance = random.choice([0, 1, 2]) 

    match attendance:
        case 1:
            print('The Employee is Present, Employee is a Full-Time Employee')
            return 8
        case 2:
            print('The Employee is Present, Employee is a Part-Time Employee')
            return 4
        case _:
            print('The Employee is Absent, The Working Hours is Zero')
            return 0

hour_rate = 20
total_hours = 0
total_days = 0
total_wage = 0
max_hours = 100
max_days = 20

print('Welcome to Employee Wage Problem')

while total_hours < max_hours and total_days < max_days:
    total_days += 1
    print(f'Day: {total_days}')
    
    daily_hours = check_attendance(hour_rate)
    
    if total_hours + daily_hours > max_hours:
        daily_hours = max_hours - total_hours  # Ensure we don't exceed 100 hours

    total_hours += daily_hours
    daily_wage = calculate_daily_wage(daily_hours, hour_rate)
    total_wage += daily_wage

    print(f'The Employee worked {daily_hours} hours today. Daily Wage: {daily_wage}')
    print(f'Total Hours: {total_hours}, Total Days: {total_days}')


print(f'The total wage for the month is: {total_wage}')

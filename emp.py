
import random

def calculate_daily_wage(hours_worked, hour_rate):
    return hours_worked * hour_rate

def check_attendance():
    attendance = random.choice([0, 1, 2])  
    if attendance == 1:
        print('The Employee is Present,Employee is a Full Time Employee')
        hours_worked=8
        total_wage = calculate_daily_wage(hours_worked, hour_rate)
        print(f'The Employee daily wage for hours worked {hours_worked} is {total_wage}')
    elif attendance == 2:
        print('The Employee is Present,Employee is a Part-Time Employee')
        hours_worked=4
        total_wage = calculate_daily_wage(hours_worked, hour_rate)
        print(f'The Employee daily wage for hours worked {hours_worked} is {total_wage}')

    else:
        print('The Employee is Absent , The Working Hours is Zero ')


hour_rate = 20

if __name__ == '__main__':
    print('Welcome to Employee Wage Problem')
    check_attendance()



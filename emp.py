
import random

def check_attendance():
    print('Welcome to Employee Wage Program on Master Branch')
    attendance = random.choice([0, 1])  
    if attendance == 1:
        print('The Employee is Present')
    else:
        print('The Employee is Absent')

if __name__ == '__main__':
    check_attendance()
    print('Welcome to Employee Wage Problem')

def calculate_daily_wage(hours_worked,hour_rate):
   return hours_worked * hour_rate


hours_worked=8
hour_rate=20

total_wage=calculate_daily_wage(hours_worked,hour_rate)

print(f'The Employee daily wage for hours worked {hours_worked} is {total_wage} ')

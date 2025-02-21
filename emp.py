import random

def calculate_daily_wage(hours_worked, hour_rate):
    return hours_worked * hour_rate

def check_attendance(hour_rate):
    attendance = random.choice([0, 1, 2]) 

    match attendance:
        case 1:
            print('The Employee is Present, Employee is a Full-Time Employee')
            hours_worked = 8
        case 2:
            print('The Employee is Present, Employee is a Part-Time Employee')
            hours_worked = 4
        case _:
            print('The Employee is Absent, The Working Hours is Zero')
            return 0

    total_wage = calculate_daily_wage(hours_worked, hour_rate)
    print(f'The Employee daily wage for hours worked {hours_worked} is {total_wage}')
    return total_wage

hour_rate = 20

if __name__ == '__main__':
    print('Welcome to Employee Wage Problem')
    total_monthly_wage =0

    for i in range(1,21):
        print(f'Day : {i}')
        daily_wage=check_attendance(hour_rate)
        total_monthly_wage +=daily_wage

    print(f'The total Monthly wage is: {total_monthly_wage}')




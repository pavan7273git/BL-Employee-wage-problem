import random

def check_attendance():
    print('Welcome to Employee Wage Program on Master Branch')
    attendance = random.choice([0, 1])  # Correct way to randomly pick 0 or 1
    if attendance == 1:
        print('The Employee is Present')
    else:
        print('The Employee is Absent')

if __name__ == '__main__':
    check_attendance()
    print('Welcome to Employee Wage Problem')
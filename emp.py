import random

class EmployeeWage:
    hour_rate = 20
    max_hours = 100
    max_days = 20

    @classmethod
    def calculate_daily_wage(cls, hours_worked):
        return hours_worked * cls.hour_rate

    @classmethod
    def check_attendance(cls):
        attendance = random.choice([0, 1, 2])

        match attendance:
            case 1:
                print('The Employee is Present, Full-Time Employee')
                return 8
            case 2:
                print('The Employee is Present, Part-Time Employee')
                return 4
            case _:
                print('The Employee is Absent, Working Hours is Zero')
                return 0

    @classmethod
    def compute_employee_wage(cls):
        total_hours = 0
        total_days = 0
        total_wage = 0

        print('Welcome to Employee Wage Problem')

        while total_hours < cls.max_hours and total_days < cls.max_days:
            total_days += 1
            print(f'Day: {total_days}')

            daily_hours = cls.check_attendance()

            if total_hours + daily_hours > cls.max_hours:
                daily_hours = cls.max_hours - total_hours

            total_hours += daily_hours
            daily_wage = cls.calculate_daily_wage(daily_hours)
            total_wage += daily_wage

            print(f'Worked {daily_hours} hours today. Daily Wage: {daily_wage}')
            print(f'Total Hours: {total_hours}, Total Days: {total_days}')

        print(f'The total wage for the month is: {total_wage}')

EmployeeWage.compute_employee_wage()

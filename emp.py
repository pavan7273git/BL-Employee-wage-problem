import random

class EmployeeWage:

    @classmethod
    def calculate_daily_wage(cls, hours_worked, wage_per_hour):
        return hours_worked * wage_per_hour

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
    def compute_employee_wage(cls, company_name, wage_per_hour, max_hours, max_days):
        total_hours = 0
        total_days = 0
        total_wage = 0

        print(f'\nCalculating Wage for {company_name}')

        while total_hours < max_hours and total_days < max_days:
            total_days += 1
            print(f'Day: {total_days}')

            daily_hours = cls.check_attendance()

            if total_hours + daily_hours > max_hours:
                daily_hours = max_hours - total_hours

            total_hours += daily_hours
            daily_wage = cls.calculate_daily_wage(daily_hours, wage_per_hour)
            total_wage += daily_wage

            print(f'Worked {daily_hours} hours today. Daily Wage: {daily_wage}')
            print(f'Total Hours: {total_hours}, Total Days: {total_days}')

        print(f'Total wage for {company_name} is: {total_wage}')

companies = []
num_companies = int(input("Enter the number of companies: "))

for i in range(num_companies):
    print(f"\nEnter details for Company {i + 1}:")
    company_name = input("Company Name: ").strip()
    wage_per_hour = int(input("Wage per Hour: ").strip())
    max_hours = int(input("Maximum Hours: ").strip())
    max_days = int(input("Maximum Working Days: ").strip())

    companies.append((company_name, wage_per_hour, max_hours, max_days))

for company in companies:
    EmployeeWage.compute_employee_wage(*company)



def calculate_daily_wage(hours_worked,hour_rate):
   return hours_worked * hour_rate


hours=float(input('Enter the hours worked by Employee: '))
hour_rate=20

total_wage=calculate_daily_wage(hours,hour_rate)

print(f'The Employee daily wage for hours worked {hours} is {total_wage} ')

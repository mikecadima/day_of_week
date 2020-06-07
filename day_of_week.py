#day of the week with 0-6
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def dayNameFromWeekday(weekday):
    if weekday>6:
        print('error');
        return 'not a day'
    return days[weekday]

day_printed = int(input('Enter weekday number [0 - 6]: '))
print('today is: ' + dayNameFromWeekday(day_printed))
print('thank you')
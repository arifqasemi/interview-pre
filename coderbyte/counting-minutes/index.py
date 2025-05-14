def get_minutes(t):
    hour, minute = map(int, t[:-2].split(':'))
    if 'pm' in t and hour != 12:
        hour += 12
    if 'am' in t and hour == 12:
        hour = 0
    return hour * 60 + minute

def CountingMinutes(str):
    start, end = str.split('-')
    start_minutes = get_minutes(start)
    print(start_minutes)
    end_minutes = get_minutes(end)
    print(end_minutes)
    diff = end_minutes - start_minutes
    return diff if diff > 0 else diff + 1440


print(CountingMinutes('1:00pm-11:00am'))
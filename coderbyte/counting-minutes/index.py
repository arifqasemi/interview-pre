def CountingMinutes(t):
    time= t.split('-')
    time_1 = [s for s in time[0].split(':')]
    time_2 = [s for s in time[1].split(':')]
    hour_2,minute_2 =int(time_2[0]),time_2[1]
    hour_1,minute_1 =int(time_1[0]),time_1[1]
    if 'pm' in minute_1:
        hour_1 +=12
    if 'pm' in minute_2:
        hour_2 +=12
    total_hour = abs(hour_2-hour_1)
    return total_hour * 60 + int(minute_1[:-2]) +int(minute_2[:-2])
    


print(CountingMinutes('1:00pm-11:00am'))
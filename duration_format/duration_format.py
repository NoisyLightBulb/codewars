def format_duration(duration):
    #set duration values
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365


    #initialize values
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    years = 0


    while duration > 0:
        #check for years
        if duration >= year:
            years = duration // year
            duration = duration % year

        #check for days
        elif duration >= day:
            days = duration // day
            duration = duration % day

        #check for hours
        elif duration >= hour:
            hours = duration // hour
            duration = duration % hour

        #check for minutes
        elif duration >= minute:
            minutes = duration // minute
            duration = duration % minute

        #check for seconds
        else:
            seconds = duration
            duration = 0


    #create output string
    time_units = []
    if years:
        time_units.append(f"{years} year{'s' if years != 1 else ''}")
    if days:
        time_units.append(f"{days} day{'s' if days != 1 else ''}")
    if hours:
        time_units.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes:
        time_units.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds:
        time_units.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    if len(time_units) == 0:
        return "now"
    elif len(time_units) == 1:
        return time_units[0]
    else:
        return ', '.join(time_units[:-1]) + f" and {time_units[-1]}"


#TEST CASES
print(format_duration(62))
print(format_duration(3662))
print(format_duration(3600))

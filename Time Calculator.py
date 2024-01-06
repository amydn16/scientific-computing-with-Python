def add_time(*arg):

    # List of days of the week
    days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    thedays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    # Time & duration are 1st & 2nd args, day is optional 3rd
    time_str = arg[0]
    dur_str = arg[1]
    if len(arg) == 3:
        day_str = arg[2].lower()

    # Split time into time & AM/PM, then time into hours & minutes
    the_time = time_str.split(' ')
    the_time[0] = the_time[0].split(':')
    the_time = [item for item in the_time[0]] + [the_time[1]]
    
    # Split duration into hours & minutes
    the_dur = dur_str.split(':')

    # Add minutes first & compute change in hours
    new_min = int(the_time[1]) + int(the_dur[1])
    new_hr = int(the_time[0])
    if new_min > 60: # Hour must change
        new_hr = int(the_time[0]) + (new_min // 60) # Update hour
        new_min = new_min - 60 # Update minute

    # Add hours
    new_hr = new_hr + int(the_dur[0])

    # Check if AM/PM needs to be changed
    new_AMPM = the_time[2]
    how_many_days = 0
    if (int(the_time[0]) < 12) and (new_hr >= 12):
        while new_hr >= 12:
            new_hr = new_hr - 12
            if new_AMPM == "AM":
                new_AMPM = "PM"
            elif new_AMPM == "PM":
                new_AMPM = "AM"
                how_many_days = how_many_days + 1 # 1 day has passed

    # Check if it is 12 o'clock
    if new_hr == 0:
        new_hr = new_hr + 12

    # Check if day needs to be changed
    if len(arg) == 3:
        which_day = days.index(day_str) # Index of old day in days
        if how_many_days > 0:
            no_days = how_many_days
            while no_days > 0:
                no_days = no_days - 1
                which_day = which_day + 1 # Index of new day in days
        if which_day >= len(days): # Start a new week
            which_day = which_day % len(days)

    # Write new time into a string
    if new_min < 10:
        new_time = str(new_hr) + ":0" + str(new_min) + " " + new_AMPM
    else:
        new_time = str(new_hr) + ":" + str(new_min) + " " + new_AMPM

    # How many days have passed
    if len(arg) == 2:
        if how_many_days == 1:
            new_time = new_time + " (next day)"
        elif how_many_days > 1:
            new_time = new_time + " (" + str(how_many_days) + " days later)"
    elif len(arg) == 3:
        if how_many_days == 0:
            new_time = new_time + ", " + arg[2]
        elif how_many_days == 1:
            new_time = new_time + ", " + thedays[which_day] + " (next day)" 
        elif how_many_days > 1:
            new_time = new_time + ", " + thedays[which_day] + " (" + str(how_many_days) + " days later)" 

    return(new_time)

    # https://repl.it/@AmyNgo/PlumWingedSoftwareagent#time_calculator.py
                
            
        

    
        

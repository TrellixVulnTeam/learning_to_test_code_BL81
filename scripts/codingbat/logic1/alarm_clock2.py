"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""

def alarm_clock(day, vacation):
    mappings = {
    0 : "Sunday",
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    }

    if vacation:
        print(f"on vacation")

        if (mappings[day] == "Saturday") or (mappings[day] == "Sunday"):
            wakeup = "off"
            return wakeup
        else:
            wakeup = "10:00"
            return wakeup
    
    else:
        print(f"not on vacation")
        if (mappings[day] == "Saturday") or (mappings[day] == "Sunday"):
            wakeup = "10:00"
            return wakeup
        else:
            wakeup = "7:00"
            return wakeup

print(alarm_clock(0, False))
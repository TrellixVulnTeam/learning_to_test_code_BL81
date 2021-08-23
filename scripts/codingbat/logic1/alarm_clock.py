"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""
mappings = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
}

vacation = True
day = mappings[6]

if vacation:
    if (day != mappings[0]) and (day != mappings[6]): # not in
        wakeup = "10:00"
    else:
        wakeup = "off"
elif not vacation:
    print("Not on vacation")
    if (day != mappings[0]) and (day != mappings[6]):
        wakeup = "7:00"
    else:
        wakeup = "10:00"

print(f"You should wakeup at: {wakeup}")

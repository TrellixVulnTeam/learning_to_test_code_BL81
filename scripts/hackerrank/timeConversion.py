from datetime import datetime

# test = datetime(2021, 10, 12, 8, 40, 0)
# print(test.strftime("%H:%M:%S"))


s = "12:01:00PM"
# should return "12:01:00"

# print(datetime.strptime(s, "%H:%M:%S%p").strftime("%I:%M%p"))

# print(datetime.today().strftime("%I:%M%p"))

def timeConversion(s):
    check_am_pm = s[-2:]
    print(check_am_pm)

    if check_am_pm == "PM":
        if s[:2] == "12":
            military_time = s[:-2]
        else:
            military_time = str(int(s[:2]) + 12) + s[2:8]
    else:
        if s[:2] == "12":
            military_time = str('00' + s[2:8])
        else:
            military_time = s[:-2]

    return military_time

if __name__ == "__main__":
    s = "12:01:00PM"
    print(timeConversion(s))
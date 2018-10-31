from datetime import datetime

# Warband start times in hours
sundayTimes = [5, 12, 19]
mondayTimes = [2, 9, 16, 23]
tuesdayTimes = [6, 13, 20]
wednesdayTimes = [3, 10, 17]
thursdayTimes = [0, 7, 14, 21]
fridayTimes = [4, 11, 18]
saturdayTimes = [1, 8, 15, 22]

timesPerDay = []
timesPerDay.append([i * 60 for i in sundayTimes])
timesPerDay.append([i * 60 for i in mondayTimes])
timesPerDay.append([i * 60 for i in tuesdayTimes])
timesPerDay.append([i * 60 for i in wednesdayTimes])
timesPerDay.append([i * 60 for i in thursdayTimes])
timesPerDay.append([i * 60 for i in fridayTimes])
timesPerDay.append([i * 60 for i in saturdayTimes])

def getTimeTillNextWarband():
    now = datetime.utcnow()
    currentDay = int(now.strftime('%w'))
    currentMinutes = now.minute + now.hour * 60

    for time in timesPerDay[currentDay]:
        if currentMinutes <= time:
            minutesLeft = time - currentMinutes
            return minutesLeft // 60, minutesLeft % 60

    minutesLeft = (24 * 60) - currentMinutes + timesPerDay[(currentDay + 1) % 7][0]
    return minutesLeft // 60, minutesLeft % 60

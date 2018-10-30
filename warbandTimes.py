from datetime import datetime

sundayTimes = [5, 12, 19]
mondayTimes = [2, 9, 16, 23]
tuesdayTimes = [6, 13, 20]
wednesdayTimes = [3, 10, 17]
thursdayTimes = [0, 7, 14, 21]
fridayTimes = [4, 11, 18]
saturdayTimes = [1, 8, 15, 22]

timesPerDay = []
timesPerDay.append(sundayTimes)
timesPerDay.append(mondayTimes)
timesPerDay.append(tuesdayTimes)
timesPerDay.append(wednesdayTimes)
timesPerDay.append(thursdayTimes)
timesPerDay.append(fridayTimes)
timesPerDay.append(saturdayTimes)


def getTimeTillNextWarband():
    now = datetime.datetime.now()
    currentDay = now.strftime("%w")
    currentHour = now.hour
    currentMinute = now.minute

    for time in timesPerDay[currentDay]:
        if currentHour < time:
            return calculateTimeTill(currentHour, currentMinute, time)

    return calculateTimeTill(currentHour, currentMinute, 24) +

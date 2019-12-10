import json
import time
import datetime
from . import sensor_data
from firebase_admin import db

ref = sensor_data.get("temperature")
target = 0.0
#current = {}

#######################     TEST VARIABLES      ########################

#temperature = 0.0       # current temperature
avgTemperature = 1.0    # the average temp of the day
currentTime = 29494015
currentDate = 2019-10-21
currentYear = 2019
currentMonth = 9
currentDay = 29
dateDifference = 0
currentHour = 20    # test time. year month day hour minute
currentMinute = 57
timeDifference = 5      # 한 시간 단위

#######################     TEST VARIABLES      ########################

output = ""
# return String value.

def getTemperatureValue( ref, requestDate, requestTime ):  # the time request
    tmp = time.localtime(time.time())

    if len(requestDate) != 0:
        year = int(requestDate.split('-', 3)[0])
        month = int(requestDate.split('-', 3)[1])
        day = int(requestDate.split('-', 3)[2])
    else:
        year = int(tmp.tm_year)
        month = int(tmp.tm_mon)
        day = int(tmp.tm_wday)

    if len(requestTime) != 0:
        hour = int(requestTime.split(':', 2)[0])
        minute = int(requestTime.split(':', 2)[1])
    else:
        hour = int(tmp.tm_hour)
        minute = int(tmp.tm_min)

    dt = datetime.datetime(year, month, day, hour, minute)

    #global current
    #current = ref.end_at()
    if db.reference("temperature/" + str(dt)) is not None:
        target = db.reference("temperature/" + str(dt))
    elif db.reference("temperature/" + str(dt+1)) is not None:
        target = db.reference("temperature/" + str(dt+1))
    else:
        target = db.reference("temperature/" + str(dt + 2))

    return target


def temperatureNLG( data ):     # data are the request intent and value(time)
    currentTimeStr = time.localtime(time.time())
    year = ""
    month = ""
    day = ""
    hour = ""
    minute = ""
    # second = ""
    avgTemperatureFlag = 1

    date = ""
    timeVal = ""

    global output
    # this is the global variable for return
    # entityTime = {}
    # entityDate = {}
    #print("temperatureNLG In")

    if data["intent"] == "Date":
        date = data["value"]
        year = date.split('-', 3)[0]
        month = date.split('-', 3)[1]
        day = date.split('-', 3)[2]

        output = output + year + "년 " + month + "월 " + day + "일   "
        print(output)

        dateDifference = int(month)*30 + int(day) - (int(currentTimeStr.tm_mon)*30 + int(currentTimeStr.tm_mday))      # /***/ NEED CORRECTION !!!
        #   positive => future, zero => now, negative => past

        if dateDifference == 0:     # today
            dateWordFlag = 1
            output = output + date + "  "

        elif dateDifference < 0:    # past
            dateWordFlag = 1
            currentDateFlag = 0
            pastDateFlag = 1
            output = output + date + "  "

        elif dateDifference > 0:    # future
            dateWordFlag = 1
            currentDateFlag = 0
            futureDateFlag = 1
            output = output + date + "  "
        else:
            pass
    #print("Date Done")

    if data["intent"] == "Time":
        avgTemperatureFlag = 0
        timeVal = data["value"]
        hour = timeVal.split(':', 2)[0]
        minute = timeVal.split(':', 2)[1]
        output = output + hour + "시 " + minute + "분  "
        timeDifference = int(hour) - int(currentTimeStr.tm_hour)    # NEED CORRECTION !!!    I only consider the hour-difference
        #   positive => future time, zero => now, negative => past time

        if timeDifference > 0:      # future
            currentTimeFlag = 0
            futureTimeFlag = 1
            if int(hour) <= 9 and int(hour) > 6:  # 6~9시 아침
                output = output + "아침 예상 기온은 "
            elif int(hour) >= 11 and int(hour) <= 14:  # 11~14시 점심
                output = output + "점심 예상 기온은 "
            elif int(hour) >= 17 and int(hour) <= 20:  # 17~20시 저녁
                output = output + "저녁 예상 기온은 "
            elif int(hour) > 20 and int(hour) < 24:  # 20~24시 밤
                output = output + "밤 예상 기온은 "
            elif int(hour) >= 0 and int(hour) <= 6:  # 0~6시 새벽
                output = output + "새벽 예상 기온은 "
            else:
                output = output + "예상 기온은 "  # default

        elif dateDifference < 0:    # past
            currentTimeFlag = 0
            pastTimeFlag = 1
            if hour <= 9 and hour > 6:              # 6~9시 아침
                output = output + "아침 기온은 "
            elif hour >= 11 and hour <= 14:         # 11~14시 점심
                output = output + "점심 기온은 "
            elif hour >= 17 and hour <= 20:         # 17~20시 저녁
                output = output + "저녁 기온은 "
            elif hour > 20 and hour < 24:           # 20~24시 밤
                output = output + "밤 기온은 "
            elif hour >= 0 and hour <= 6:           # 0~6시 새벽
                output = output + "새벽 기온은 "
            else:
                output = output + "기온은 "          # default

        else:                       # today !!
            if abs(timeDifference) < 2:             # right now
                currentTimeFlag = 1
                output = output + "현재 기온은 "
            else:
                output = output + "오늘 "
                if hour <= 9 and hour > 6:  # 6~9시 아침
                    output = output + "아침 기온은 "
                elif hour >= 11 and hour <= 14:  # 11~14시 점심
                    output = output + "점심 기온은 "
                elif hour >= 17 and hour <= 20:  # 17~20시 저녁
                    output = output + "저녁 기온은 "
                elif hour > 20 and hour < 24:  # 20~24시 밤
                    output = output + "밤 기온은 "
                elif hour >= 0 and hour <= 6:  # 0~6시 새벽
                    output = output + "새벽 기온은 "
                else:
                    output = output + "기온은 "  # default

        temperature = getTemperatureValue(ref, date, timeVal)
        print(output)
        print(temperature.get())

        if temperature.get() is not None:
            output = output + temperature.get() + "입니다."
        else:
            print("데이터를 받아오는데 실패했습니다!")

    return output


        # if time == "현재" or "아까":
        #     if dateWordFlag == 0:
        #         output = output + time
        #     else:                       # 어제 현재 온도??? 오늘 현재 온도??? no no
        #         pass
        # elif time == "아침":
        #     if currentTimeFlag == 1:    # if the date is today
        #         if hour < 9:            # currentTime - date > 0 이면 과거, 오늘 아침이라고 하면?
        #
        #             pass
        #         pass
        #     output = output + time
        # elif time == "점심":
        #
        #     pass
        # elif time == "저녁":
        #
        #     pass
        # elif time == "밤":
        #
        #     pass
        # elif time == "새벽":
        #
        #     pass
        # else:
        #     hour = time.split(':', 2)[0]
        #     minute = time.split(':', 2)[0]
        #     output = output + hour + "시 " + "분 "



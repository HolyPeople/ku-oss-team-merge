import json
from . import sensor_data

#######################     TEST VARIABLES      ########################

temperature = 0.0       # current temperature
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

def temperatureNLG( data ):

    #data = {}        # JSON Decode to Dictionary


    timeWord = "현재"
    dateWord = "오늘"
    year = ""
    month = ""
    day = ""
    hour = ""
    minute = ""
    # second = ""
    dateWordFlag = 0
    avgTemperatureFlag = 1

    currentDateFlag = 1
    pastDateFlag = 0
    futureDateFlag = 0
    currentTimeFlag = 1
    pastTimeFlag = 0
    futureTimeFlag = 0

    global output
    # entityTime = {}
    # entityDate = {}

    if data["intent"] == "Date":
        date = data["value"]
        year = date.split('-', 3)[0]
        month = date.split('-', 3)[1]
        day = date.split('-', 3)[2]

        output = output + year + "년 " + month + "월 " + day + "일   "

        dateDifference = date - currentDate        # /***/ NEED CORRECTION !!!
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


    if data["intent"] == "Time":
        avgTemperatureFlag = 0
        time = data["value"]
        hour = time.split(':', 2)[0]
        minute = time.split(':', 2)[0]
        output = output + hour + "시 " + minute + "분  "

        timeDifference = hour - currentHour    # NEED CORRECTION !!!    I only consider the hour-difference
        #   positive => future time, zero => now, negative => past time

        if dateDifference > 0:      # future
            currentTimeFlag = 0
            futureTimeFlag = 1
            if hour <= 9 and hour > 6:  # 6~9시 아침
                output = output + "아침 예상 기온은 "
            elif hour >= 11 and hour <= 14:  # 11~14시 점심
                output = output + "점심 예상 기온은 "
            elif hour >= 17 and hour <= 20:  # 17~20시 저녁
                output = output + "저녁 예상 기온은 "
            elif hour > 20 and hour < 24:  # 20~24시 밤
                output = output + "밤 예상 기온은 "
            elif hour >= 0 and hour <= 6:  # 0~6시 새벽
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

    if avgTemperatureFlag == 1:
        output = output + str(avgTemperature) + "입니다."
    else:
        output = output + str(temperature) + "입니다."

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



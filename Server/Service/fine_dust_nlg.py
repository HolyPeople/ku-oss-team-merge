from Service.take_sensor_value import fine_dust

fineDust = fine_dust()[0]['pm10Value']
output = ""

def fineDustNLG( data ):

    global output


    if data["intent"] == "Date":
        date = data["value"]
        year = date.split('-', 3)[0]
        month = date.split('-', 3)[1]
        day = date.split('-', 3)[2]

        output = output + year + "년 " + month + "월 " + day + "일   "


    if data["intent"] == "Time":
        time = data["value"]
        hour = time.split(':', 2)[0]
        minute = time.split(':', 2)[0]
        output = output + hour + "시에 측정한"

        output = output + "미세먼지 농도는"
        output = output + fineDust + "입니다."

    return output
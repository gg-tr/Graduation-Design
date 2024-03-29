from .utils import *
import datetime


def getYearDate():
    timeList = list(df['time'].map(lambda x: int(x[:4])))
    timeList.sort();
    timeObj = {}
    for i in timeList:
        if timeObj.get(i, -1) == -1:
            timeObj[i] = 1
        else:
            timeObj[i] = timeObj[i] + 1
    return list(timeObj.keys()), list(timeObj.values())


def getMovieTimeData():
    movieTime = list(df['moveiTime'])
    movieTimeDate = [{
        'name': '短',
        'value': 0,
    }, {
        'name': '中',
        'value': 0,
    }, {
        'name': '长',
        'value': 0,
    }, {
        'name': '特长',
        'value': 0,
    }]
    for i in movieTime:
        i = i[2:-2]
        if len(i) > 1 and int(i) <= 80:
            movieTimeDate[0]['value'] = movieTimeDate[0]['value'] + 1; 
        elif len(i) > 1 and int(i) <= 120 and int(i) >=80:
            movieTimeDate[1]['value'] = movieTimeDate[1]['value'] + 1;
        elif len(i) > 1 and int(i) <= 150 and int(i) >=120:
            movieTimeDate[2]['value'] = movieTimeDate[2]['value'] + 1;
        elif len(i) > 1 and int(i) >=150:
            movieTimeDate[3]['value'] = movieTimeDate[3]['value'] + 1;
        else:
            pass
    return movieTimeDate

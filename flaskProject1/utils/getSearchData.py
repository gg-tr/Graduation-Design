from .utils import *

def getMovieDetailByid(movieId):
    tableDate =df.values;
    resultData = []
    for i in tableDate:
        if i[0]==movieId:
             i[17]=i[17].split(sep="'")[1:-1]
             # print(i[17])
             resultData.append(list(i))
    return resultData
def getMovieDetailBySearchWord(searchWord):
    tableData = df.values
    resultData = []
    flag =[]
    for i in tableData:
        if i[3].find(searchWord) !=-1 and i[3] not in flag:
            i[17] = i[17].split(sep="'")[1:-1]
            flag.append(i[3])
            print(i[0])
            resultData.append(i)
    return resultData
# getMovieDetailByid(1)
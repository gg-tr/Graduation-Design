from  .utils import *

def getDerectorsDataTop():
    directorList=typeList('directors')
    directorObj = {}
    for i in directorList:
        j = i.split('/');
        for k in j:
            k = k.strip()
            if directorObj.get(k, -1) == -1:
                directorObj[k] = 1
            else:
                directorObj[k] += 1
    directorObj=sorted(directorObj.items(),key=lambda x:x[1],reverse=True)[:20]
    row=[]
    columns=[]
    for i in directorObj:
        row.append(i[0])
        columns.append(i[1])
    return row,columns
def getCastsDataTop():
    castList = typeList('cover')

    castObj = {}
    for i in castList:
        j = i.split(',');
        for k in j:
            k = k.strip()
            if castObj.get(k, -1) == -1:
                castObj[k] = 1
            else:
                castObj[k] += 1
    castObj = sorted(castObj.items(), key=lambda x: x[1], reverse=True)[:20]
    row = []
    columns = []
    for i in castObj:
        row.append(i[0])
        columns.append(i[1])
    return row, columns
from .utils import *

def getTypeData():
    typesList = typeList('types')
    typesObj = {}
    for i in typesList:
        j = i.split(',');
        for k in j:
            k = k.strip()
            if typesObj.get(k, -1) == -1:
                typesObj[k] = 1
            else:
                typesObj[k] += 1
    typeData =[]
    for key,item in typesObj.items():
        typeData.append({
            'name':key,
            'value':item
        })
    return  typeData



from .utils import *
def getMapData():
    mapList=typeList('country')
    mapObj={}
    for i in mapList:
        j=i.split('/');
        for k in j:
            k=k.strip()
            if mapObj.get(k,-1)==-1:
               mapObj[k]=1
            else:
              mapObj[k]+=1
    return list(set(mapObj.keys())),list(mapObj.values())
def getLangData():
    langList = typeList('lang')
    langObj = {}
    for i in langList:
        j = i.split('/');
        for k in j:
            k = k.strip()
            if langObj.get(k, -1) == -1:
                langObj[k] = 1
            else:
                langObj[k] += 1
    return list(set(langObj.keys())), list(langObj.values())
from .utils import *

def getHomeData():
    maxMovieLen = len(df.values) # 电影的个数
    maxRate =df['rate'].max() # 电影的评分
    castsList=typeList('cover')
    maxCasts='弗雷德·威拉德' #最多演员出场
    countryList=typeList('country')
    maxCountry=max(countryList,key=countryList.count) #最多电影国家
    typeLists=typeList('types')#电影类型
    maxType=len(set(typeLists))
    langList = typeList('lang')
    maxlang = max(langList, key=langList.count)  # 最多语言国家
    return maxlang,maxCountry,maxRate,maxCasts,maxMovieLen,maxType

def getTypeEchartDate():
    typesList = typeList('types')
    unique_genres = [genre.split(',') for genre in set(typesList)]

    # 打印去重后的元素
    res=[];
    for genre in unique_genres:
        for genres in genre:
            # if genres  not in res:
               res.append(genres)
            # print(genres)
    # print(typesList)
    typesList=res;
    # typesList =unique_genress
    typeObj ={}
    for i in typesList:
        if typeObj.get(i,-1) == -1:
            typeObj[i]=1
        else:
            typeObj[i]=typeObj[i]+1;
    typeEchartData=[]
    for key,value in typeObj.items():
        typeEchartData.append({
            'name':key,
            'value':value
        })
    return typeEchartData

def getRateEcharData():
    rateList=df['rate'].map(lambda x:float(x)).values
    rateList.sort()
    rateObj={}
    for i in rateList:
        if rateObj.get(i, -1) == -1:
            rateObj[i] = 1
        else:
            rateObj[i] =rateObj[i] + 1;
    return list(rateObj.keys()),list(rateObj.values())
def getTableData():
    tableData =df.values
    for i,item in enumerate(tableData):
        item[17] =item[17].split(sep=',')
    return tableData
getHomeData()
